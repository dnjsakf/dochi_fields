
class ValidateError(Exception):
  def __init__(self, messages, code=400):
    super(ValidateError, self).__init__()
    self.messages = messages
    self.code = code
    
  def getMessages(self):
    return self.messages
  
  def __str__(self):
    return '[{code}] {messages}'.format(code=self.code, messages=self.messages)
