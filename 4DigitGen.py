#encode, decode hash
import hashlib

#open file of numbers, put them into a list in memory
open_file = open("numbers.txt", "r")
stri= ""
sum = 0
for line in open_file:
    stri+=line 
numberList = stri.split()
open_file.close()

#hashed md5
ade = "fe3ee0fed08037dfbb56a063d4674734"
christian = "9a982e05c8a6a7b33d61fca3aa1af17c"
elyse = "93ccd950dc65bdda2d7d72458f6fbe78"
jenny = "834c834324c7319ffee40e6c8b7ad774"
kristy = "677b60f801a3d18969c23425cb19ce4a"

#the start of password
prefixString = "FLAG-HQNT-"
passwordList = []

#append prefix to number list put in another list as full
#password
for numbers in numberList:
    passwordList.append(prefixString + numbers)
       
#increment through the password list make it a hash then match 
#the hash to find the flag
for p in passwordList:
    encrypted = hashlib.md5(p.encode('utf-8')).hexdigest()
        
    if encrypted == christian:
        print("christian = " + p)  
        
    if encrypted == elyse:
        print("elyse = " + p)
        
    if encrypted == kristy:
        print("kristy = " + p)  
        
    if encrypted == ade:
        print("ade = " + p) 
        
    if encrypted == jenny:
        print("jenny = " + p)                   
    
    

