# models.py
from uuid import uuid4
from datetime import datetime

from fields import BaseField, StringField, IntegerField, DatetimeField
from errors import ValidateError

class BaseModel(object):
  def __init__(self, data=None, many=False):
    self.__many = many
    
    if data is not None:
      self.dump(data)
  
  def getField(self, field_name, field_type=None):
    '''
    특정 필드 조회
    * BaseField 타입의 필드를 조회하기위한 함수
    '''
    if hasattr(self, field_name):
      attr = getattr(self, field_name)
      if field_type is None:
        return attr
      elif isinstance(attr, field_type):
        return attr
      
      raise TypeError("Expected data type '%s', but '%s'." %( field_type.__name__, attr.__class__.__name__ ))
    raise ValueError("'%s' is not defined field." % ( field_name ))

  def getFields(self):
    '''
    필드 목록 조회
    * BaseField 타입의 필드 목록을 조회하기위한 함수
    '''
    fields = list()
    for field_name in dir(self):
      try:
        field_value = self.getField(field_name, BaseField)
        if not callable(field_value) and not field_name.startswith("_"):
          fields.append((field_name, field_value))
      except:
        pass
    return fields
  
  def __mapp(self, datas, validate=True):
    '''
    데이터 매핑
    * 각 필드에 데이터를 매핑하는 함수
    * 옵션에 따라 유효성검사를 실시
    '''
    data = dict()
    errors = dict()
    
    # 입력값 매핑
    for field_name, value in datas.items():
      try:
        field_class = self.getField(field_name, BaseField)
        field_class.setValue(value, validate=validate)
        data[field_name] = field_class.getValue()
        
      except Exception as e:
        errors[field_name] = str(e)
        
    # 기본값 매핑
    for field_name, field_class in self.getFields():
      # 입력값 매핑을 시도한 필드는 제외
      if field_name in datas:
        continue
      
      try:
        default = field_class.getOption("default", None)
        
        # 기본값이 문자열이면 현재 객체에 정의된 메소드 중 이름이 일치하는 메소드 조회
        if isinstance(default, str) and hasattr(self, default):
          default = getattr(self, default)
          
        # 기본값이 메소드면 실행한 결과값을 저장하고 아니면 그냥 저장
        value = default if not callable(default) else default(field_name)
        
        # 필드에 저장된 데이터 
        field_class.setValue(value, validate=validate)
        data[field_name] = field_class.getValue()
        
      except Exception as e:
        errors[field_name] = str(e)
    
    # 값매핑 결과 반환
    return ( data, errors )
  
  def dump(self, data=None):
    '''
    단일 데이터 Dumping
    * 입력받은 데이터를 각 필드에 매핑
    * @data:Optional[Dict]
      - data가 None이면 dump 데이터로 처리(dump가 먼저 실행되어야함)
    '''
    __data = data if data is not None else self.__dump_data
    dumped, errors = self.__mapp(__data, validate=False)
    
    self.__dump_data = dumped
    self.__errors = errors
    
    return dumped

  def load(self, data=None):
    '''
    단일 데이터 Loading
    * 입력받은 데이터를 각 필드에 매핑
    * 유효성검사 실시, 유효하지 않은 필드는 ValidateError를 발생시켜 반환
    * @data:Optional[Dict]
      - data가 None이면 dump 데이터로 처리(dump가 먼저 실행되어야함)
    '''
    __data = data if data is not None else self.__dump_data
      
    loaded, errors = self.__mapp(__data, validate=True)
    
    self.__load_data = loaded
    self.__errors = errors
    
    if len(errors) > 0:
      raise ValidateError(errors)
      
    return loaded
    
  def dumps(self, datas):
    pass
    
  def loads(self, datas):
    pass
    
  def __str__(self):
    return str(self.__data)
    
  def __repr__(self):
    return "<models.{self.__class__.__name__}>".format(self=self)
  

class UserModel(BaseModel):
  id = StringField(required=True, maxlength=50, default=lambda info: str(uuid4()))
  name = StringField(maxlength=10)
  role = StringField(required=True, default="user")
  age = IntegerField(required=True, min=0, max=200)
  hire_date = DatetimeField(required=True, format="%Y%m%d%H%M%S", default="getNowDate")

  def getNowDate(self, name):
    return datetime.now()
