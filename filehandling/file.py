""" file=open('filehandling/file.txt','r')
print(file.read()) """
import os

file=open('filehandling/abi.txt','a')
file.write("GEt job soon")

os.remove('filehandling/file.txt')