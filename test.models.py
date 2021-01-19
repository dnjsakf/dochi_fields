# test.models.py
from models import UserModel
from pprint import pprint

class TestUserModel(object):
  def __init__(self):
    print("UserModel 테스트")
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
    user = UserModel(dict(
      name="Dochi",
      age=1004,
      role="admin",
      hire_date="20210119235959"
    ))
    user_data = user.load()
    pprint( user_data )
        
  def test_case_2(self):
    print("날짜형 필수값 오류 확인")
    user = UserModel(dict(
      name="User01",
      age=5
    ))
    user_data = user.load()

    pprint( user_data )

# 테스트실행
TestUserModel()