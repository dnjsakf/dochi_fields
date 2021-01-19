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
 