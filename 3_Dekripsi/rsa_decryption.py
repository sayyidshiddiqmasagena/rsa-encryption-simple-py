'''
SAYYID SHIDDIQ MASAGENA (D121191014)
A. MUH RAYYAN EKA PUTRA (D121191074)
'''
 
'''
rsa_decryption merupakan aplikasi yang berfungsi untuk mendekripsi data ciphertext (sandi berupa sederetan bit) yakni melakukan
rekayasa data (inverse dari enkripsi) sehingga data tersebut bertransformasi kembali menjadi plaintext pengirim. Proses pendekripsian 
ini dapat dilaksanakan selama pihak decryptor memiliki dua komponen dekripsi yakni gembok (n) dan private key (d) yang disimpan dan
dirahasiakan dari pihak public semejak proses key generator berlangsung. Algoritma utama dari enkripsi rsa adalah (c^d mod n ≡ m),
dimana c (ciphertext) dipangkatkan dengan d (private key) mod n (gembok) akan menghasilkan m (pesan awal pengirim (plaintext)).
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
    x='' #pesan dalam bentuk string
    m=0 #pesan dalam bentuk integer
    for i in txt:
        if(int(i)== 400):
            x+=' '
        else:
            m=(int(i)**d)%n #enkripsi^private key mod n, utk mendekripsi ada di buku
            m+=65 #supaya semuanya mulai dari 0
            c=chr(m) #int --> char
            x+=c #membentuk string tiap char tanpa list --> karena c != [] tapi c = ''
    return x

def main(): 
    message = input("Pesan yang ingin dekripsi (masukkan dengan koma (,)):  ")
    print("Pesanmu kini adalah:",message)
    enc_msg=decrypt(private,message)

    print("\nPesan kamu yang telah terdekripsi:")
    print(enc_msg, end="\n")

    return enc_msg

main()