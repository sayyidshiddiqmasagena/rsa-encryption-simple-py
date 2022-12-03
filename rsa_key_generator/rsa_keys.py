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

#RSA Modulus ---> mencari nilai n yg menjadi 'missing puzzle' untuk menyelesaikan p dan q
n = p * q
print("RSA modulus n = ",n)
 
'''
Eulers Toitent ---> r atau Φ(n) atau phi function, 
gunanya untuk menghitung "ketidaksamaan" faktor angka n 
dan kebetulan jika dia prima maka cukup Φ(n) = a-1 di mana a == prima
'''
r= (p-1)*(q-1)
print("Eulers Toitent Φ(n) = ",r)
 
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
 
 
#Extended Euclidean Algorithm --> optional tapi ini membuktikan bahwa e dan r faktornya = 1
def eea(a,b):
    #cek lagi jika  e dan Φ(n) atau r bukan prima
    if(a%b==0):
        return(b,0,1)

    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    # di sini variabel _ dipakai untuk simpan passingan dari 
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
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
print("Nilai e = ",e)


#d, Private and Public Keys
# '''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''

print("EUCLID'S EXTENDED ALGORITHM:")
d = mult_inv(e,r)
print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
print("The value of d is:",d)
print("*****************************************************")
public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public)
print("*****************************************************")

input('Press ENTER to exit') 