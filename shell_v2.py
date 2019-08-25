from COMP import *
codes = []
codes.append("")
count = 0
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
