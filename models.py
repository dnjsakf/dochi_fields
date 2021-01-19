# models.py
from uuid import uuid4
from datetime import datetime
from fields import BaseField, StringField, IntegerField, DatetimeField

class BaseModel(object):
  def __init__(self, data=None):
    if data is not None:
      self.dump(data)

  # 현재 Model 객체의 필드명 조회
  def getFields(self):
    fields = list()
    for field_name in dir(self):
      field_class = getattr(self, field_name)
      if isinstance(field_class, BaseField) and not field_name.startswith("__"):
        fields.append((field_name, field_class))
    return fields

  # 입력값 임시 저장
  def dump(self, data):
    self.__data = None

    for field_name, field_class in self.getFields():
      value = data.get(field_name, None)

      try:
        # 값매핑, 유효성검사 안함
        field_class.setValue(value, validate=False)

      except Exception as e:
        pass

    # 값매핑 결과 반환
    self.__data = dict([(field_name, field_class.getValue()) for field_name, field_class in self.getFields()])

    return self.__data

  # 입력한 데이터를 Field에 매핑, 유효성검사 진행
  def load(self, data=None):
    data = data or self.__data

    self.__errors = dict()
    self.__data = None

    for field_name, field_class in self.getFields():
      value = data.get(field_name, None)
      default_value = field_class.getOption("default_value")

      # 기본값 처리
      if value is None and default_value is not None:
        if isinstance(default_value, str) and hasattr(self, default_value):
          default_value = getattr(self, default_value)

        if callable(default_value):
          value = default_value(field_class)
        else:
          value = default_value

      try:
        # 값매핑, 유효성검사
        field_class.setValue(value)

      except Exception as e:
        # 오류 저장
        self.__errors[field_name] = str(e)

    # 값매핑 결과 반환
    self.__data = dict([(field_name, field_class.getValue()) for field_name, field_class in self.getFields()])
    self.__data["__errors"] = self.__errors

    return self.__data

  def __str__(self):
    return str(self.__data)


class UserModel(BaseModel):
  id = StringField(required=True, maxlength=50, default_value=lambda info: str(uuid4()))
  name = StringField(maxlength=10)
  role = StringField(required=True, default_value="user")
  age = IntegerField(required=True, min=0, max=200)

  hire_date = DatetimeField(required=True, format="%Y%m%d%H%M%S", default_value="getNow")

  def getNow(self, info):
    return datetime.now()
