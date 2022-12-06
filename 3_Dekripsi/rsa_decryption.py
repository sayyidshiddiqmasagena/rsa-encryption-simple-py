'''
SAYYID SHIDDIQ MASAGENA (D121191014)
A. MUH RAYYAN EKA PUTRA (D121191074)
'''
 
import math
from pickle import FALSE
 
print("=== RSA Dekripsi ===")

print("Masukkan private key 'd' dan gembok 'n'-mu!")
d = int(input("private key 'd': "))
n = int(input("gembok 'n': "))

private = (d,n)
 
#Algoritma Dekripsi
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',') #string dalam list harus diconvert jdi int
    x=''
    m=0
    for i in txt:
        if(int(i)== 400):
            x+=' '
        else:
            m=(int(i)**d)%n #enkripsi^private key mod n, utk mendekripsi ada di buku

            m+=65 #supaya semuanya mulai dari 0
            c=chr(m) #int --> char
            x+=c #membentuk string tiap char tanpa list --> karena c != [] tapi c = ''
    return x
 

message = input("Pesan yang ingin dienkripsi (untuk saat ini hanya bisa text):  ")
print("Pesanmu adalah:",message)
enc_msg=decrypt(private,message)

print("\nPesan kamu yang terenkripsi:")
print(enc_msg, end="\n")