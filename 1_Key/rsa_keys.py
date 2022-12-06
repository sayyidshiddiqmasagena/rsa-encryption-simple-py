'''
SAYYID SHIDDIQ MASAGENA (D121191014)
A. MUH RAYYAN EKA PUTRA (D121191074)
'''
 
import math
from pickle import FALSE
 
print("=== Key Generator ===")
 
#Input bilangan prima
print("Masukkan angka prima: ")
p = int(input("Bilangan prima 'p': "))
q = int(input("Bilangan prima 'q': "))

#algoritma: check jika bilangan prima
def cek_bil_prim(bil_prim):
    #bil_prim passingan dari 'p' dan 'q'
    if(bil_prim==2):
        return True
    elif((bil_prim<2) or ((bil_prim%2)==0)):
        return False
    elif(bil_prim>2):
        for i in range(2,bil_prim):
            if not(bil_prim%i):
                return FALSE
    return True
 
#check jika bilangan prima
cek_bil_prim_p = cek_bil_prim(p)
cek_bil_prim_q = cek_bil_prim(q)

#kalau tidak prima, masukkan angka kembali
while(((cek_bil_prim_p==False)or(cek_bil_prim_q==False))):
    print("==! Bukan angka prima, silahkan masukkan ulang !==")
    p = int(input("Bilangan prima 'p': "))
    q = int(input("Bilangan prima 'q': "))
    cek_bil_prim_p = cek_bil_prim(p)
    cek_bil_prim_q = cek_bil_prim(q)
 
'''
Pseudocode RSA Key Generation
Referensi: "Understanding Cryptography by Christof Paar"

1. 1. Choose two large primes p and q.
2. Compute n = p · q.
3. Compute Φ(n) = (p−1)(q−1).
4. Select the public exponent e ∈ {1,2, . . . ,Φ(n)−1} such that
gcd(e,Φ(n)) = 1.
5. Compute the private key d such that: d x e ≡ modΦ(n)

penjelasan rumus: https://youtu.be/wXB-V_Keiu8

'''

#RSA Modulus ---> mencari nilai n yg menjadi 'missing puzzle' atau 'gembok' untuk menyelesaikan p dan q
n = p * q
print("RSA modulus n = ",n)
 
'''
Eulers Toitent ---> r atau Φ(n) atau phi function, 
gunanya untuk menghitung "ketidaksamaan" faktor angka n 
dan kebetulan jika dia prima maka cukup Φ(n) = a-1 di mana a == prima
'''
r= (p-1)*(q-1)
print("Eulers Toitent Φ(n) = ",r, '\n')
 
'''
GCD --> greatest common divison / faktor persekutuan terbesar 
GCD akan menentukan jika e sudah bisa dikatakan public exponent untuk menyelesaikan gcd(e,Φ(n)) = 1 terhadap Φ(n) --> Eulers Theorem
syarat utamanya adalah e dan n hanya mempunyai faktor == 1
'''

#GCD dari e dan Φ(n) atau r
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
 
'''
EEA --> extended euclidean algorithm / algoritma euclidean lanjutan 
Selain menghitung GCD, EEA juga digunakan untuk menemukan koefisien integer s dan t dengan: as + bt = gcd(a,b)
Extended Euclidean Algorithm menemukan s dan t dengan menggunakan substitusi balik untuk menulis ulang persamaan algoritma pembagian
secara rekursif hingga mendapatkan persamaan yang merupakan kombinasi linier dari bilangan awal.
''' 
 
#Extended Euclidean Algorithm
def eea(a,b):
    #cek lagi jika  e dan Φ(n) atau r bukan prima
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("EEA:  %d*(%d) + (%d)*(%d) = %d"%(a,t,s,b,gcd), )
        return(gcd,t,s)
    #proses gcd pada eea sama saja pada gcd biasa, tetapi sebagai tambahan kita mengupdate nilai s dan t pada akhir setiap recursive call
 
'''
MI --> multiplicative inverse atau lebih tepatnya modular multiplicative inverse
Modular multiplicative invers dari suatu bilangan bulat d adalah bilangan bulat e sedemikian rupa sehingga perkalian d x e kongruen dengan 1 terhadap modulus Φ(n) --> d x e ≡ 1 modΦ(n)
Untuk menentukan nilai d, maka dilakukan pengecekan modular multiplicative inverse terhadap s(hasil dari eea terhadap e,r) dan Φ(n) atau r
''' 

#Multiplicative Inverse -->
def mult_inv(e,r):
    gcd,s,_=eea(e,r) #terima input dari line 91 dan line 96, _ tidak dipakai
    if(gcd!=1):
        return None #jika nilai gcd e dan Φ(n) atau r bukan 1, maka modular multiplicative inverse tidak exist
    else: 
        if(s<0): 
            print("MI, di mana s < 0: s = %d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
        elif(s>0): 
            print("MI, di mana s > 0: s = %d."%(s))
        return s%r
 
'''
e --> public exponent/key yang menyelesaikan d x e ≡ modΦ(n)
di sini dicari i in range 1 sampai 1000 yang bisa menjadi faktor dari gcd(e,Φ(n)) = 1 atau egcd(e,r) == 1
atau dengan kata lain e dan Φ(n) co-prime, yaitu sama-sama mempunyai faktor 1

bisa juga ditentukan sembarang oleh user seperti pada buku, tapi belum tentu bisa memenuhi syarat gcd(e,Φ(n)) = 1
'''
for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i
print("Mencari Public Key e = ",e, '\n')

d = mult_inv(e,r)
print("Mencari Private Key d dengan extended euclid's algorithm = ", d, '\n')

print("Public Key kamu adalah d = '%d' dengan gembok n = %d" %(e,n))
print("Private Key kamu adalah e = '%d' dengan gembok n = %d" %(d,n), '\n')

input('Press ENTER to exit') 