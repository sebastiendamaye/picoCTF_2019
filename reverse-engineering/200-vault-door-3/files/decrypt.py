#!/usr/bin/env python3

encrypted = "jU5t_a_sna_3lpm16g84c_u_4_m0r846"
decrypted = []
for i in range(32):
    decrypted.append('')

# for (i=0; i<8; i++) { buffer[i] = password.charAt(i); }
for i in range(8):
    decrypted[i] = encrypted[i]

# for (; i<16; i++) { buffer[i] = password.charAt(23-i); }
for i in range(8, 16):
    decrypted[i] = encrypted[23-i]

#for (; i<32; i+=2) { buffer[i] = password.charAt(46-i); }
for i in range(16, 31, 2):
    decrypted[i] = encrypted[46-i]

#for (i=31; i>=17; i-=2) { buffer[i] = password.charAt(i); }
for i in range(17, 32, 2):
    decrypted[i] = encrypted[i]

# show decoded message:
print(''.join([i for i in decrypted]))
