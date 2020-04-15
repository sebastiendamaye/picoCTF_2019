# whats-the-difference
## Question
>Can you spot the difference? [kitters](files/kitters.jpg) [cattos](files/cattos.jpg). They are also available at `/problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a` on the shell server

## Hint
>How do you find the difference between two files?

>Dumping the data from a hex editor may make it easier to compare.

# Solution
We are provided with 2 pictures that look the same:
~~~~
$ file *.jpg
files/cattos.jpg:  JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 4032x1960, components 3
files/kitters.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 4032x1960, components 3
~~~~

However, they are different:
~~~~
$ sha256sum *.jpg
2f0143052f6b8935a2fb0578ac9dee0a6b8dcd536a9c5131d2f916068ad0353e  files/cattos.jpg
40457490f16be29843b75e83571307ec9fce81633dfb2aea8569ae39861d120c  files/kitters.jpg
~~~~

You can hexdump both files and compare the differences (see the `pico` part?):
~~~~
$ xxd cattos.jpg > cattos.hex
$ xxd kitters.jpg > kitters.hex
$ diff cattos.hex kitters.hex 
3109c3109
< 0000c240: 21d3 6da6 4b70 6963 6f60 1b95 41e8 b93d  !.m.Kpico`..A..=
---
> 0000c240: 21d3 6da6 4b99 9d98 c860 1b95 41e8 b93d  !.m.K....`..A..=
5479c5479
< 00015660: e57c 4779 71fd a114 5e64 7e4b 0662 4390  .|Gyq...^d~K.bC.
---
> 00015660: e57c 4779 71fd a114 5e64 7e4b 0662 0a90  .|Gyq...^d~K.b..
10166c10166
< 00027b50: 5b5b 3ed2 d142 a003 dc54 c1f4 ff00 eb53  [[>..B...T.....S
---
> 00027b50: 5b5b 3ed2 d142 a003 dcf4 c1f4 ff00 eb53  [[>..B.........S
10952c10952
< 0002ac70: 72df 452d a476 c259 0101 88fe f71d 467b  r.E-.v.Y......F{
---
[SNIP]
~~~~

Now, I know that there are only a few bytes that differ from both files, let's write a python script that will compare each bytes of the 2 files and will extract the ones that differ.

```python
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
```

# Flag
`picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}`
