'''
WELCOME TO THE RSA DECRYPTION. THIS IS AN INTERACTIVE TOOL USED TO DECRYPT A MESSAGE USING THE FAMOUS RSA ALGORITHM.
 
SAYYID SHIDDIQ MASAGENA (D121191014)
A. MUH RAYYAN EKA PUTRA (D121191074)
'''
 
import math
from pickle import FALSE
 
print("RSA DECRYPTION")
print("*****************************************************")
 
print("PLEASE ENTER THE 'd' AND 'n' VALUES BELOW:")
d = int(input("Enter the value of private key 'd': "))
n = int(input("Enter the value of number 'n': "))

print("*****************************************************")
print("PRIVATE KEY")
private = (d,n)
print("Private Key is:",private)
print("*****************************************************")
 
'''DECRYPTION ALGORITHM.'''
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',') #string dalam list harus diconvert jdi int
    x=''
    m=0
    for i in txt:
        if(int(i)== 400):
            x+=' '
        else:
            m=(int(i)**d)%n #enkripsi^private key mod n, utk mendekripsi

            m+=65 #supaya semuanya mulai dari 0
            c=chr(m) #int --> char
            x+=c #membentuk string tiap char tanpa list
    return x
 
message = input("What message would you like to be decrypted?:  ")
print("Your message is:", message)

enc_msg=decrypt(private,message)
print("Your decrypted message is:",enc_msg)
print("Thank you for using the RSA Decryptor. Goodbye!")

input('Press ENTER to exit') 