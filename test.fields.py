# test.fields.py
from fields import BaseField
from datetime import datetime
    
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
TestBaseField()
