#!/usr/bin/env python
cattos = open('cattos.jpg', 'rb')
kitters = open('kitters.jpg', 'rb')
flag = []
while 1:
    b_cattos = cattos.read(1)
    b_kitters = kitters.read(1)
    if b_cattos!=b_kitters:
        flag.append(b_cattos)
    if not b_cattos or not b_kitters:
        break
print(''.join([i.decode("utf-8") for i in flag]))
