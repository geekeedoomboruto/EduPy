from COMP import *
import sys
def topy(code):
	return edupy_comp(code)
if __name__ == "__main__":
	globals()[sys.argv[1]](sys.argv[2])
