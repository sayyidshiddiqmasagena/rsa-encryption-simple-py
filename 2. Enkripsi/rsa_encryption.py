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
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
 
message = input("What message would you like to be encrypted?:  ")
print("Your message is:",message)
 
choose = input("Type 'yes' to encrypt the message or 'no' to quit: ")
if(choose=='yes'):
    enc_msg=encrypt(public,message)
    print("Your encrypted message is:",enc_msg)
    print("Thank you for using the RSA Encryptor. Goodbye!")
elif(choose=='no'):
    print("Thank you for using the RSA Encryptor. Goodbye!")
else:
    print("You entered the wrong option.")
    print("Thank you for using the RSA Encryptor. Goodbye!")

input('Press ENTER to exit') 