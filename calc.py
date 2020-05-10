import logging

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

x = add(8,2)
y = subtract(6,5)
z = multiply(7,7)
u = divide(12,3)
print("sum: ",x)
print("diff: ",y)
print("multiply: ",z)
print("multiply: ",u)
logging.basicConfig(filename="logFile.txt", filemode='a', format='%(asctime)s %(levelname)s-%(message)s', datefmt='%Y-%m-%d %H:%M:%S',level=logging.DEBUG)
logging.info(x)
logging.info(y)
logging.info(z)
logging.info(u)
