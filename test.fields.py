# test.fields.py
from fields import BaseField, StringField, IntegerField, DatetimeField
from datetime import datetime, timedelta
    
# BaseField 테스트
class TestBaseField(object):
  
  #문자열 필드
  string_field = BaseField(str, required=True)
  
  #숫자형 필드
  integer_field = BaseField(int, required=True)
  
  #날짜형 필드
  datetime_field = BaseField(datetime, required=True)
  
  def __init__(self):
    print("BaseField 테스트")
    print("="*30)
    for attrname in dir(self):
      testcase = getattr(self, attrname)
      if attrname.startswith("test") and callable(testcase):
        print("=========", attrname, "========")
        try:
          testcase()
        except Exception as e:
          print("Error: "+str(e))
        print("="*30)
        
  def test_case_1(self):
    print("문자열 필수값 오류 확인")
    print("Input: None")
    self.string_field.setValue(None)
    print("Value: "+str(self.string_field.getValue()))
      
  def test_case_2(self):
    print("문자열 타입 오류 확인")
    print("Input: 1234")
    self.string_field.setValue(1234)
    print("Value: "+str(self.string_field.getValue()))
  
  def test_case_3(self):
    print("문자열 정상")
    print("Input: 'Hello!!'")
    self.string_field.setValue("Hello!!")
    print("Value: "+str(self.string_field.getValue()))
        
  def test_case_4(self):
    print("정수형 필수값 오류 확인")
    print("Input: None")
    self.integer_field.setValue(None)
    print("Value: "+str(self.integer_field.getValue()))
      
  def test_case_5(self):
    print("정수형 타입 오류 확인")
    print("Input: '1234'")
    self.integer_field.setValue('1234')
    print("Value: "+str(self.integer_field.getValue()))
  
  def test_case_6(self):
    print("정수형 정상")
    print("Input: 1234")
    self.integer_field.setValue(1234)
    print("Value: "+str(self.integer_field.getValue()))
        
  def test_case_7(self):
    print("날짜형 필수값 오류 확인")
    print("Input: None")
    self.datetime_field.setValue(None)
    print("Value: "+str(self.datetime_field.getValue()))
      
  def test_case_8(self):
    print("날짜형 타입 오류 확인")
    print("Input: '20200101'")
    self.datetime_field.setValue('20200101')
    print("Value: "+str(self.datetime_field.getValue()))
  
  def test_case_9(self):
    print("날짜형 정상")
    print("Input: %s" %(datetime.now()))
    self.datetime_field.setValue(datetime.now())
    print("Value: "+str(self.datetime_field.getValue()))
      
# 테스트 실행
# TestBaseField()


# Stringfield 테스트
class TestStringfield(object):
  
  # 문자열 필드
  field = StringField(required=True, maxlength=10)
  
  def __init__(self):
    print("Stringfield 테스트")
    print("="*30)
    for attrname in dir(self):
      testcase = getattr(self, attrname)
      if attrname.startswith("test") and callable(testcase):
        print("=========", attrname, "========")
        try:
          testcase()
        except Exception as e:
          print("Error: "+str(e))
        print("="*30)
        
  def test_case_1(self):
    print("문자열 필수값 오류 확인")
    print("Input: None")
    self.field.setValue(None)
    print("Value: "+str(self.field.getValue()))
      
  def test_case_2(self):
    print("문자열 타입 오류 확인")
    print("Input: 1234")
    self.field.setValue(1234)
    print("Value: "+str(self.field.getValue()))
  
  def test_case_3(self):
    print("문자열 최대길이 오류 확인")
    print("Input: '1234567890#'")
    self.field.setValue('1234567890#')
    print("Value: "+str(self.field.getValue()))
  
  def test_case_4(self):
    print("문자열 정상")
    print("Input: 'Hello!!'")
    self.field.setValue("Hello!!")
    print("Value: "+str(self.field.getValue()))

# 테스트 실행
# TestStringfield()



# IntegerField 테스트
class TestIntegerField(object):
  
  # 문자열 필드
  field = IntegerField(required=True, min=10, max=100)
  
  def __init__(self):
    print("IntegerField 테스트")
    print("="*30)
    for attrname in dir(self):
      testcase = getattr(self, attrname)
      if attrname.startswith("test") and callable(testcase):
        print("=========", attrname, "========")
        try:
          testcase()
        except Exception as e:
          print("Error: "+str(e))
        print("="*30)
        
  def test_case_1(self):
    print("정수형 필수값 오류 확인")
    print("Input: None")
    self.field.setValue(None)
    print("Value: "+str(self.field.getValue()))
      
  def test_case_2(self):
    print("정수형 타입 오류 확인")
    print("Input: '100'")
    self.field.setValue('100')
    print("Value: "+str(self.field.getValue()))
  
  def test_case_3(self):
    print("정수형 최솟값 오류 확인")
    print("Input: 3")
    self.field.setValue(3)
    print("Value: "+str(self.field.getValue()))
  
  def test_case_4(self):
    print("정수형 최댓값 오류 확인")
    print("Input: 999")
    self.field.setValue(999)
    print("Value: "+str(self.field.getValue()))
  
  def test_case_4(self):
    print("정수형 정상")
    print("Input: 100")
    self.field.setValue(100)
    print("Value: "+str(self.field.getValue()))

# 테스트 실행
# TestIntegerField()



# DatetimeField 테스트
class TestDatetimeField(object):
  
  # 문자열 필드
  field = DatetimeField(required=True, format="%Y-%m-%d %H:%M:%S", min='now', max=timedelta(hours=1))
  
  def __init__(self):
    print("DatetimeField 테스트")
    print("="*30)
    for attrname in dir(self):
      testcase = getattr(self, attrname)
      if attrname.startswith("test") and callable(testcase):
        print("=========", attrname, "========")
        try:
          testcase()
        except Exception as e:
          print("Error: "+str(e))
        print("="*30)
        
  def test_case_1(self):
    print("날짜형 필수값 오류 확인")
    print("Input: None")
    self.field.setValue(None)
    print("Value: "+str(self.field.getValue()))
      
  def test_case_2(self):
    print("날짜형 포맷 오류 확인")
    print("Input: '2021/01/19 23:59:59'")
    self.field.setValue('2021/01/19 23:59:59')
    print("Value: "+str(self.field.getValue()))
      
  def test_case_3(self):
    print("날짜형 타입 오류 확인")
    print("Input: 1000")
    self.field.setValue(1000)
    print("Value: "+str(self.field.getValue()))
  
  def test_case_4(self):
    value = datetime.now() - timedelta(minutes=5)
    print("날짜형 최소시간 오류 확인")
    print("Input: %s (현재시간 - 5분)" %( value ))
    self.field.setValue(value)
    print("Value: "+str(self.field.getValue()))
  
  def test_case_5(self):
    value = datetime.now() + timedelta(hours=2)
    print("날짜형 최댓값 오류 확인")
    print("Input: %s (현재시간 + 2시간)" %( value ))
    self.field.setValue(value)
    print("Value: "+str(self.field.getValue()))
  
  def test_case_6(self):
    value = datetime.now() + timedelta(minutes=30)
    print("날짜형 정상")
    print("Input: %s (현재시간 + 30분)" %( value ))
    self.field.setValue(value)
    print("Value: "+str(self.field.getValue()))

# 테스트 실행
TestDatetimeField()
