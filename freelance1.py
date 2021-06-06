import os,sys
import time as T

#print ("file name")
# print (sys.argv[1])

def intime():
    path = os.getcwd()
    size = os.path.getsize(path)
    time = os.path.getmtime("natas29.py")
    print("Size (In bytes) of '%s':" %path, size)
    T.sleep(2.4)
    print(time)
    return 0
    
def main():
    print ("system initialized")
    intime()
    return 0

main()
