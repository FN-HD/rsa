from Mods.PublicKeyCryptography.Receiver import Receiver
from Mods.PublicKeyCryptography.Sender import Sender
from Mods.RSA.RSA import RSA
import time


print('start\n')
ob = RSA
data = (1013, 1031)

start = time.time()
receiver_a = Receiver(ob, data)
print('受信側を生成:'+str(time.time()-start)+'\n'+str(receiver_a)+'\n')

start = time.time()
sender_b = Sender(ob, receiver_a.get_public_key())
print('送信側を生成:'+str(time.time()-start)+'\n'+str(sender_b)+'\n')

str1 = 'The quick onyx goblin jumps over the lazy dwarf.'
#str1 = input('please input message.')
print('メッセージ:\n    '+str1+'\n')

start = time.time()
c = sender_b.crypt(str1)
print('暗号化:'+str(time.time()-start)+'\n    '+str(c)+'\n')

start = time.time()
m = receiver_a.decrypt(c)
print('複合化:'+str(time.time()-start)+'\n    '+m+'\n    '+str(str1 == m))
