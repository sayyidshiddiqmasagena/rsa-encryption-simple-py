'''
WELCOME TO THE RSA ENCRYPTION. THIS IS AN INTERACTIVE TOOL USED TO ENCRYPT A MESSAGE USING THE FAMOUS RSA ALGORITHM.
 
SAYYID SHIDDIQ MASAGENA (D121191014)
A. MUH RAYYAN EKA PUTRA (D121191074)
'''
 
import math
from pickle import FALSE
 
print("RSA ENCRYPTION")
print("*****************************************************")
 
print("PLEASE ENTER THE 'e' AND 'n' VALUES BELOW:")
e = int(input("Enter the value of public key 'e': "))
n = int(input("Enter the value of number 'n': "))

print("*****************************************************")
print("PUBLIC KEY")
public = (e,n)
print("Public Key is:",public)
print("*****************************************************")
 
'''ENCRYPTION ALGORITHM.'''
def encrypt(pub_key,n_text): #(public, message)
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            print('terbaca di isupper')
            m = ord(i)-65 #codepoint utk unicode 65 --> A 
            c=(m**e)%n
            # x = 'terbaca sbg text/char capslock'
            x.append(c)
        elif(i.islower()):      
            print('terbaca di islower')         
            m= ord(i)-97 #codepoint utk unicode 97 --> a
            c=(m**e)%n
            # x = 'terbaca sbg text/char lowercase'
            x.append(c)
        elif(i.isspace()):
            print('terbaca di isspace')
            spc=400
           # x = 'terbaca sbg text/char spasi
            x.append(400)
        else:
            # x = 'terbaca sebagai angka'
            m = ord(i)-48 #codepoint utk unicode 48 --> 0
            c=(m**e)%n
            x.append(c)
         
            
    return x
 

message = input("What message would you like to be encrypted?:  ")
print("Your message is:",message)
enc_msg=encrypt(public,message)
print("Your encrypted message is:",enc_msg)
print("Thank you for using the RSA Encryptor. Goodbye!")

input('Press ENTER to exit') 