from COMP import *
import sys
def execute(original):
    try:
        original_code = open(original, 'r').readlines()
        original_code = "".join(original_code)
        pycode = edupy_comp(original_code)
        exec(pycode)
    except:
        print("Error when process")

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])