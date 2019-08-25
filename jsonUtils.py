import json
class ReturnValue(object):
    """
    Used for readJson
    """
    def __init__(self, keys, values, length):
       self.keys = keys
       self.values = values
       self.length = length
def readJson(filename):
    """
    Returns a list of all the objects in the .json set
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    info = str(data)
    info.split(":")
    keys = []
    for i in data:
        keys.append(i)
    obj = []
    for i in keys:
        obj.append(data[i])
    length = len(keys)
    return ReturnValue(keys, obj, length)
def createJson(filename):
    """
    Creates a json file
    """
    bey = {}
    with open(filename, 'w') as f:
        json.dump(bey, f)
def writeJson(filename, set):
    """
    Writes in a json file
    """
    with open(filename, 'w') as f:
        json.dump(set, f)
def getString(json):
    """
    json to String (dict to str)
    """
    return json.JSONEncoder().encode(json)
def getJson(string):
    """
    String to json (dict type)
    """
    return json.loads(string)
if __name__ == "__main__":
    print("All setup!")