import sys
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
def stringbefore(string, indexof):
    if not '"' in string:
        return False
    else:
        for i in string:
            if i == '"' and string.index(i) < indexof:
                return True
        return False
def isfunction(string):
    if "(" in string and ")" in string and ("def" in string or "command" in string or "define" in string):
        return True
    return False
def isclass(string):
    if "create" in string or "class" in string:
        return True
    return False
def isloop(string):
    cond1 = "for" in string or "while" in string or "until" in string
    cond12 = (">=" in string or "<=" in string or "<" in string or ">" in string or "!=" in string or "==" in string or "est" in string or "dans" in string or "True" in string or "False" in string or "Vrai" in string or "Faux" in string)
    cond2 = ("in" in string or cond12) and cond1
    if cond2:
        return True
    return False
def iscondition(string):
    cond1 = ("if" in string or "again if" in string or "otherwise" in string)
    cond2 = (">=" in string or "<=" in string or "<" in string or ">" in string or "!=" in string or "==" in string or "est" in string or "dans" in string)
    if "otherwise" in string:
        if string == "otherwise":
            return True
        else:
            ss = string
            try:
                ss = ss.replace("\t", "")
                if ss == "otherwise":
                    return True
                else:
                    return False
            except:
                return False
    else:
        if cond1 and cond2:
            return True
        else:
            return False
def issomething(line):
    if isfunction(line) or isclass(line) or iscondition(line) or isloop(line):
        return True
    else:
        return False
def isvar(line):
    if not "=" in line:
        return False
    else:
        if len(line.split("=")) == 2:
            return True
        else:
            return False
def hasvariable(line):
    if isvar(line):
        return True
    else:
        if issomething(line):
            if ":" in line:
                nl = line.split(":")
            if "{" in line:
                nl = line.split("{")
            else:
                nl = line
            logic = []
            for s in nl:
                if isvar(s):
                    logic.append(True)
                else:
                    logic.append(False)
            if True in logic:
                return True
            else:
                return False   
        else:
            return False
def remnames(line):
    if "number" in line:
        line.replace("number ", "")
    if "object" in line:
        line.replace("object ", "")
    if "var" in line:
        line.replace("var ", "")
    if "string" in line:
        line.replace("string ", "")
    if "unchange" in line:
        line.replace("unchange ", "")
    return line
def edupy_comp(code):
    grammar = readJson("grammar.json")
    mmpcode = grammar.keys
    pycode = grammar.values
    new_code = ""
    if "\n" in code:
        code = code.split("\n")
        for line in code:
            for i in mmpcode:
                if i in line:
                    ttr = pycode[mmpcode.index(i)]
                    tryline = line.replace(r'{}'.format(i), "~"+ttr)
                    if stringbefore(tryline, tryline.index("~")):
                        line = line
                    else:
                        line = line.replace(i, ttr)
                if issomething(line) and not ":" in line and not "{" in line:
                    line += ":"
                if hasvariable(line):
                    line = remnames(line)
                else:
                    line += ""
            line+="\n"
            new_code += line

    return new_code
def pyfile(code, ofn):
    ofn = ofn.split(".")
    filename = ofn[0]+'.py'
    f = open(filename, "w")
    f.write(edupy_comp(code))
    f.close()
def execute(original):
    try:
        original_code = open(original, 'r').readlines()
        original_code = "".join(original_code)
        pycode = edupy_comp(original_code)
        exec(pycode)
    except Exception as e:
        print(e)
def shell(something=None):
    codes = []
    codes.append("")
    count = 0
    print("EduPy shell in Windows 10")
    print("EduPy Village v0.3a")
    while True:
        w = (input(">>> "))
        if not w == "script":
            x = edupy_comp(w+"\n")
        else:
            x = "script"
        if x == "exit":
            break
        if not x == "script":
            try:
                y = eval(x)
                if y: print(y)
            except:
                try:
                    exec(x)
                except Exception as e:
                    print("Erreur:", e)
        else:
            while True:
                line = input(">>> ")
                if not line == "finish":
                    codes[count] += line+"\n"
                else:
                    exec(edupy_comp(codes[count]))
                    count += 1
                    codes.append("")
                    break
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
