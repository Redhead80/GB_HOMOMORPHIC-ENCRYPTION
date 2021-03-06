#Реализация функции генерации ключей
from random import randint
nkeys = 100  # размер массива публичных ключей
PublicKey = [0]*nkeys  # массив публичных ключей
PrivateKey = 0  # секретный ключ
b1 = 10**10  # нижняя граница диапазона значений ключей
b2 = b1**2  # верхняя граница диапазона значений ключей
modulo = b1  # порядок группы
def GreatestCommonDivisor(a,b):  # вычисление НОД(а,b), итеративный вариант
  while (b != 0):
    a = a % b
    a, b = b, a
  return a
def KeyGen(): # функция генерации ключей
 global nkeys, PublicKey, PrivateKey, modulo, b1, b2
 while True:
   PrivateKey = randint(b1, b2)
   if GreatestCommonDivisor(PrivateKey,modulo) == 1:
    break
   PublicKey = [(randint(b1,b2)*PrivateKey)+(modulo*randint(10,100))
    for i in range(0,nkeys)]
 return


#реализация ̮функции шифрования и дешифрования
def Encrypt(m):
 global nkeys, PublicKey
 return m+sum([PublicKey[i] for i in range(0,nkeys) if randint(0,1) == 1])
def Decrypt(c):
 global PrivateKey, modulo
 return (c % PrivateKey) % modulo