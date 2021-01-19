# fields.py
class BaseField(object):
  def __init__(
      self,
      valtype,
      required=False,
      **kwargs):
 
    self.__value = None
    self.__type = valtype
    self.__required = required
    self.__options = dict(kwargs)
  
  # 값 설정
  def setValue(self, value, validate=True):
    self.__value = None
    
    if validate:
      # 유효성검사: 필수값
      if value is None and self.required:
        raise ValueError("This value was Required, but it is None.")
      
      # 유효성검사: 데이터 타입
      if value is not None and not isinstance(value, self.__type):
        raise TypeError("Expected data type '%s', but '%s'." %( self.__type.__name__, value.__class__.__name__ ))
      
      # 유효성검사
      self.validate(value)
    
    self.__value = value
    
  def getValue(self):
    return self.__value
 
  def getOption(self, optkey, defaultvalue=None):
    return self.__options.get(optkey, defaultvalue)
    
  @property  
  def type(self):
    return self.__type
 
  @property
  def required(self):
    return self.__required
  
  # Override
  def validate(self, value=None):
    pass
  
  def __str__(self):
    return str(self.__value)

    
# 문자열 필드
class StringField(BaseField):
  def __init__(self, maxlength=None, **kwargs):
    super(StringField, self).__init__(str, **kwargs)
    
    # 유효성검사 옵션값
    self.__maxlength = maxlength
  
  # Overriding: 유효성검사
  def validate(self, value=None):
    exists = value is not None
    value = value if exists else self.getValue()
    length = len(value) if exists else 0
    messages = self.getOption("messages", dict())
    
    # 유효성검사: 필수값
    if bool(self.required) and not exists:
      msg = "This value was Required, but it is None."
      msg = messages.get("required", msg)
      raise ValueError(msg)
    
    # 유효성검사: 최대길이
    if bool(self.__maxlength) and exists and length > self.__maxlength:
      msg = "Expacted value length %d, but %d." % ( self.__maxlength, length )
      msg = messages.get("maxlength", msg)
      raise ValueError(msg)

# 정수형 필드
class IntegerField(BaseField):
  def __init__(self, min=None, max=None, **kwargs):
    super(IntegerField, self).__init__(int, **kwargs)

    # 유효성검사 옵션값
    self.__min = min
    self.__max = max
  
  # Overriding: 유효성검사
  def validate(self, value=None):
    exists = value is not None
    value = value if exists else self.getValue()
    messages = self.getOption("messages", dict())
    
    # 유효성검사: 필수값
    if bool(self.required) and not exists:
      msg = "This value was Required, but it is None."
      msg = messages.get("required", msg)
      raise ValueError(msg)
    
    # 유효성검사: 최소값
    if bool(self.__min) and exists and value < self.__min:
      msg = "Expacted minimum %d, but %d." % ( self.__min, value )
      msg = messages.get("min", msg)
      raise ValueError(msg)

    # 유효성검사: 최댓값
    if bool(self.__max) and exists and value > self.__max:
      msg = "Expacted maximum %d, but %d." % ( self.__max, value )
      msg = messages.get("max", msg)
      raise ValueError(msg)

      

from datetime import datetime   

# 날짜형 필드
class DatetimeField(BaseField):
  def __init__(self, format="%Y-%m-%d %H:%M:%S", *args, **kwargs):
    super(DatetimeField, self).__init__(datetime, *args, **kwargs)

    self.__value = None
    self.__format = format

  # 값 설정
  def setValue(self, value, format=None, validate=True):
    # 값이 문자열인 경우, datetime으로 변환
    if isinstance(value, str):
      value = datetime.strptime(value, format or self.__format)

    self.__value = None
    
    if validate:
      # 값이 있는 경우 타입체크
      if value is not None and not isinstance(value, self.type):
        raise TypeError("Expacted data type '%s', but '%s'." %( self.type.__name__, value.__class__.__name__ ))
      
      # 유효성검사
      self.validate(value)
    
    self.__value = value
