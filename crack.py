import hashlib 
from difflib import SequenceMatcher
import difflib
from Crypto.Hash import MD4
# initializing string 
str1 = "GeeksforGeeks"
f = open("pass.txt", 'r')
pas = f.read()
pas = pas.split()

# encoding GeeksforGeeks using encode() 
# then sending to md5() 
quer = 'edcc589a5f93d845f6e3d784839de9c4'
k = 0
for i in pas:
    result = hashlib.md5(i.encode())
    # if k == 0:
    #     print(i)
    #     print((result.hexdigest()))
    #     k+=1
   
   
    if( result.hexdigest() == quer ) :
        print(i)
        break
  
