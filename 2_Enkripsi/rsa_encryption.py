'''
SAYYID SHIDDIQ MASAGENA (D121191014)
A. MUH RAYYAN EKA PUTRA (D121191074)
'''
 
'''
rsa_encryption merupakan aplikasi yang berfungsi untuk mengenkripsi data plaintext (teks/angka) yakni melakukan rekayasa data
sehingga data tersebut berubah menjadi sandi (ciphertext) yang berupa sederetan bit. Proses pengenkripsian ini dapat dilaksanakan
selama pihak encryptor memiliki dua komponen enkripsi yakni gembok (n) dan public key (e) yang didapatkan dari pihak key generator.
Algoritma utama dari enkripsi rsa adalah (m^e mod n ≡ c), dimana m (pesan plain text) dipangkatkan dengan e (public key) mod n (gembok)
akan menghasilkan c (ciphertext).
'''

import math
from pickle import FALSE
 
print("=== RSA Enkripsi ===")
 
print("Masukkan public key 'e' dan gembok 'n'-mu!")
e = int(input("public key 'e': "))
n = int(input("gembok 'n': "))

public = (e,n)

#Algoritma Enkripsi
def encrypt(pub_key,n_text): #(public, message)
    e,n=pub_key
    x=[] #pesan dalam bentuk string
    m=0 #pesan dalam bentuk integer
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65 #codepoint utk unicode 65 --> A 
            c=(m**e)%n #algoritmanya
            # x = 'terbaca sbg text/char capslock'
            x.append(c)
        elif(i.islower()):         
            m= ord(i)-97 #codepoint utk unicode 97 --> a
            c=(m**e)%n
            # x = 'terbaca sbg text/char lowercase'
            x.append(c)
        elif(i.isspace()):
            spc=400
           # x = 'terbaca sbg text/char spasi
            x.append(400)
        else:
            # x = 'terbaca sebagai angka'
            m = ord(i)-48 #codepoint utk unicode 48 --> 0
            c=(m**e)%n
            x.append(c)
         
            
    return x
 
def main():
    message = input("Pesan yang ingin dienkripsi (untuk saat ini hanya bisa text):  ")
    print("Pesanmu adalah:",message)
    enc_msg=encrypt(public,message)
    print("\nPesan kamu yang terenkripsi:")
    print(*enc_msg, sep = ', ', end="\n")
    return enc_msg
    
main()

'''
kesimpulan dari rsa_encryption adalah pesan yang ingin ditransformasi menjadi ciphertext membutuhkan dua variabel dasar yakni
gembok (n) dan public key (e). Idealnya, data plain text (m) yang ingin dienkripsi dapat berupa gabungan dari string, integer,
simbol, dan sebagainya. Namun, pada kasus saat ini aplikasi rsa_encryption hanya dapat memilih antara menggunakan full string
atau full integer. Hal ini dikarenakan kami belum menemukan proses komputasi yang tepat dalam penggabungan semua tipe data tersebut.
Jika ingin menggunakan tipe data full text, maka diperlukan algoritma for-loop yang mengenkripsi tiap char melalui percabangan if-else
dan mendeteksi apakah char tersebut upper, lower, atau blank space. Untuk memudahkan proses enkripsi dan dekripsi, tiap char/int
dipisah menggunakan simbol koma (,) meskipun tentunya akan lebih mudah bagi pihak lain untuk menerka pola dari ciphertext.
Semakin panjang plaintext, maka proses komputasi enkripsi akan relatif lebih lama tetapi tidak selama proses dekripsi.
'''
