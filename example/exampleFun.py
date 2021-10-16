from vercelDeploy.apiDecorator import api
from vercelDeploy.lambdaService import LambdaService

class MyService(LambdaService):
  """
  User will write a class which will extend a predefined class (from the library you make) called LambdaService.
  """
  @api(http_methods=["GET"])
  def predictSum(self, a: int, b: int):
      """
        Users will write methods in this class and annotate them with the decorator @api. Only some methods will be annotated
      as @api and some might not be.
      """
      sum = a + b
      return sum
    
  @api(http_methods=["POST"])
  def sendMessage(self, msg: str):

    return msg
