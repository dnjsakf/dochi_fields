# test.models.py
from pprint import pprint

from models import UserModel
from errors import ValidateError

class TestUserModel(object):
  def __init__(self):
    print("UserModel 테스트")
    print("="*40)
    for attrname in dir(self):
      testcase = getattr(self, attrname)
      if attrname.startswith("test") and callable(testcase):
        print("="*40)
        print( testcase.__doc__ )
        print("="*40)
        try:
          testcase()
        except Exception as e:
          print("Error: "+str(e))
        print("")
        print("="*40)
        
  def test_case_1(self):
    '''
    데이터 매핑 방법
    '''
    user = UserModel(dict(
      name="Dumpping_2",
      age=10,
      hire_date="20210120"
    ))
    
    data = user.dump(dict(
      id="admin",
      name="Dumpping_1",
      age=100,
      hire_date="20210120"
    ))
        
  def test_case_2(self):
    '''
    데이터 단일 Dumping 정상 / 단일 Loading 오류
    '''
    user = UserModel(dict(
      name="Dochi",
      age=1004,
      hire_date="20210120"
    ))
    print("==== Dump Result")
    dump_data = user.dump()
    pprint( dump_data, indent=2 )
    print("")
    
    try:
      print("==== Load Result")
      load_data = user.load()
      pprint( load_data, indent=2 )
    
    except ValidateError as e:
      pprint( e.getMessages(), indent=2 )
      
  def test_case_3(self):
    '''
    데이터 단일 Dumping 정상 / 단일 Loading 정상
    '''
    user = UserModel(dict(
      name="Dochi",
      age=109,
      hire_date="20210120123456"
    ))
    print("==== Dump Result")
    dump_data = user.dump()
    pprint( dump_data, indent=2 )
    print("")
    
    try:
      print("==== Load Result")
      load_data = user.load()
      pprint( load_data, indent=2 )
    
    except ValidateError as e:
      pprint( e.getMessages(), indent=2 )

# 테스트실행
TestUserModel()