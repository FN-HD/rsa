from Mods.PublicKeyCryptography.Receiver import Receiver
from Mods.PublicKeyCryptography.Sender import Sender
from Mods.RSA.RSA import RSA
import time


object = RSA
data = (1013, 1031)

start = time.time()
receiver_a = Receiver(object, data)
sender_b = Sender(object, receiver_a.get_key())

print('message:'+str(time.time()-start))
str1 = 'The quick onyx goblin jumps over the lazy dwarf.'
print(str1+'\n')

print('Crypt:'+str(time.time()-start))
c = sender_b.crypt(str1)
print(c)
print('')

print('Decrypt:'+str(time.time()-start))
m = receiver_a.decrypt(c)
print(m+'\n')

print('finished:'+str(time.time()-start))
