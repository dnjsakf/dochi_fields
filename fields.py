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
    
    # 유효성검사: 필수값
    if bool(self.required) and not exists:
      raise ValueError("This value was Required, but it is None.")
    
    # 유효성검사: 최대길이
    if bool(self.__maxlength) and exists and length > self.__maxlength:
      raise ValueError("Expected value length %d, but %d." % ( self.__maxlength, length ))


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
    
    # 유효성검사: 최솟값
    if bool(self.__min) and exists and value < self.__min:
      raise ValueError("Expected minimum %d, but %d." % ( self.__min, value ))

    # 유효성검사: 최댓값
    if bool(self.__max) and exists and value > self.__max:
      raise ValueError("Expected maximum %d, but %d." % ( self.__max, value ))


from datetime import datetime, timedelta

# 날짜형 필드
class DatetimeField(BaseField):
  def __init__(self, format="%Y-%m-%d %H:%M:%S", min=None, max=None, *args, **kwargs):
    super(DatetimeField, self).__init__(datetime, *args, **kwargs)

    self.__value = None
    self.__format = format
    self.__min = None
    self.__max = None

    # 제한시간 설정: 최소
    if min is not None:
      if min == 'now':
        self.__min = datetime.now()
      elif isinstance(min, str):
        self.__min = datetime.strptime(min, format)
      else:
        self.__min = min

    # 제한시간 설정: 최대
    if max is not None:
      if max == 'now':
        self.__max = datetime.now()
      elif isinstance(max, str):
        self.__max = datetime.strptime(max, format)
      else:
        self.__max = max

  # 값 설정
  def setValue(self, value, format=None, validate=True):
    self.__value = None

    # 유효성검사: 문자열 포맷 확인
    if isinstance(value, str):
      value = datetime.strptime(value, format or self.__format)

    if validate:
      # 유효성검사
      self.validate(value)
    
    self.__value = value

  # 값 반환, datetime
  def getValue(self, format=None):
    return self.__value

  # Overriding: 유효성검사
  def validate(self, value=None):
    exists = value is not None
    value = value if exists else self.getValue()

    # 유효성검사: 타입체크
    if exists and not isinstance(value, self.type):
      raise TypeError("Expected data type '%s', but '%s'." %( self.type.__name__, value.__class__.__name__ ))

    # 유효성검사: 필수값
    if bool(self.required) and not exists:
      raise ValueError("This value was Required, but it is None.")
    
    # 유효성검사: 최소시간
    if bool(self.__min) and exists:
      
      # 최소시간 데이터 형변환
      min = None
      if isinstance(self.__min, timedelta):
        min = datetime.now()+self.__min
      else:
        min = self.__min

      if value < min:
        raise ValueError("Expected datetime less than (%s), but %s." % ( min, value ))

    # 유효성검사: 최대시간
    if bool(self.__max) and exists:
      
      # 최대시간 데이터 형변환
      max = None
      if isinstance(self.__max, timedelta):
        max = datetime.now()+self.__max
      else:
        max = max
  
      if value > max:
        raise ValueError("Expected datetime greater than (%s), but %s." % ( max, value ))
