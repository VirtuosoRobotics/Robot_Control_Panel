import os

print(os.getcwd())
home_path = os.getenv("HOME")
print(home_path)
f = open(home_path+"/status.txt", "r")
print(f.read())