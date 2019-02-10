from Mods.PublicKeyCryptography.Receiver import Receiver
from Mods.PublicKeyCryptography.Sender import Sender
from Mods.RSA.RSA import RSA
import time


object = RSA
data = (1013, 1031)
start = time.time()
print('start')

receiver_a = Receiver(object, data)
print('受信側を生成:'+str(time.time()-start))
print(str(receiver_a)+'\n')

sender_b = Sender(object, receiver_a.get_key())
print('送信側を生成:'+str(time.time()-start))
print(str(sender_b)+'\n')

str1 = 'The quick onyx goblin jumps over the lazy dwarf.'
print('message:'+str(time.time()-start))
print('    '+str1+'\n')

c = sender_b.crypt(str1)
print('Crypt:'+str(time.time()-start))
print(str(c)+'\n')

m = receiver_a.decrypt(c)
print('Decrypt:'+str(time.time()-start))
print('    '+m)
