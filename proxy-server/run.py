import web
import json



urls = (
    '/reset', 'reset',
    '/sync', 'sync',
    '/crossdomain.xml', 'crossdomain',
    '/update', 'update'
)

outputData = {}
inputData = {}

resetFlag = False



class reset:
  def GET(self):
    global resetFlag
    resetFlag = True
    return "Confirmed"


class sync:
  def POST(self):
    global outputData, resetFlag
    outputData = json.loads(web.input().outputData)
    outputData["reset"] = resetFlag
    resetFlag = False
    return json.dumps(inputData)


class update:
  def POST(self):
    global inputData
    inputData = json.loads(web.input().inputData)
    return json.dumps(outputData)


class crossdomain:
  def GET(self):
    with open("crossdomain.xml") as f:
      return f.read()



if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()