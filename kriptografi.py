from base64 import encode
from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key) 

pesan = input("Masukkan pesan yang ingin di-enkripsi: ").encode() # endcode() berfungsi untuk mengkonversi string ke byte

e = f.encrypt(pesan)

print("Pesan yang sudah di-enkripsi: ", e)

d = f.decrypt(e)

print("Pesan yang sudah di-dekripsi (dalam bentuk byte): ", d) 

print("Pesan yang sudah di-dekripsi (dalam bentuk string): ", d.decode())