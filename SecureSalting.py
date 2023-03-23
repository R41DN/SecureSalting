#!/usr/bin/python3

import sys
import string
import random
import hashlib
from pwn import *


#Definimos la correcta ejecución del script.
if len(sys.argv)!=2:
    print("\n[!] ERROR \n\n[*] Ejecución correcta del script : python3 hash.py contraseña")
    sys.exit(1)

#Definimos el argumento que es la contraseña
password=sys.argv[1]

#Definimos la salt
salt=''.join(random.choices(string.ascii_letters+string.digits,k=5))

#Codificaremos la salt y el password
password=password.encode('utf-8')
salt=salt.encode('utf-8')

#Generamos el hash
hash_password=hashlib.sha512(password+salt).hexdigest()

#Imprimimos nuestra contraseña
print("\nLa contraseña utilizada es:",password.decode('utf-8'))

#Imprimimos nuestra salt
print("\nLa salt utilizada es:",salt.decode('utf-8'))
print("\n",end='')
#Generamos una barra de progreso
barra=log.progress("Generando hash ...")
sleep(2)

#Imprimimos el hash
print("\nHash generado:",hash_password)
print("\n",end='')
