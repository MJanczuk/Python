import random

with open('test.txt',"a") as f:
    for i in range(1, 10):
       f.write(str(random.gauss(1, 1))+ ";" + str(random.gauss(1, 1)) + "\n")


       