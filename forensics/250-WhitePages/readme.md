# WhitePages
## Question
>I stopped using YellowPages and moved onto WhitePages... but [the page they gave me](files/whitepages.txt) is all blank!

## Hint
>NA

# Solution
Opening the file in a standard text editor won't show anything. However, a hex editor will reveal a serie of `e2 80 83` and `20`:
~~~~
$ xxd whitepages.txt | head
00000000: e280 83e2 8083 e280 83e2 8083 20e2 8083  ............ ...
00000010: 20e2 8083 e280 83e2 8083 e280 83e2 8083   ...............
00000020: 20e2 8083 e280 8320 e280 83e2 8083 e280   ...... ........
00000030: 83e2 8083 20e2 8083 e280 8320 e280 8320  .... ...... ... 
00000040: 2020 e280 83e2 8083 e280 83e2 8083 e280    ..............
00000050: 8320 20e2 8083 20e2 8083 e280 8320 e280  .  ... ...... ..
00000060: 8320 20e2 8083 e280 83e2 8083 2020 e280  .  .........  ..
00000070: 8320 20e2 8083 2020 2020 e280 8320 e280  .  ...    ... ..
00000080: 83e2 8083 e280 83e2 8083 2020 e280 8320  ..........  ... 
00000090: e280 8320 e280 8320 e280 83e2 8083 e280  ... ... ........
~~~~

As only 2 patterns are available, we can assume this is binary. Let's try this:
* `e2 80 83` = 0
* `20` = 1

Let's write a python [script](files/flag.py) that will take care of these replacements:
```python
#!/usr/bin/env python3
from pwn import *

with open('whitepages.txt', 'rb') as f:
    data = bytearray(f.read())
    data = data.replace(b'\xe2\x80\x83', b'0')
    data = data.replace(b'\x20', b'1')
    data = data.decode("ascii")
    print(unbits(data))
```

Let's run the script:
~~~~
$ python flag.py 
b'\n\t\tpicoCTF\n\n\t\tSEE PUBLIC RECORDS & BACKGROUND REPORT\n\t\t5000 Forbes Ave, Pittsburgh, PA 15213\n\t\tpicoCTF{not_all_spaces_are_created_equal_178d720252af1af29369e154eca23a95}\n\t\t'
~~~~

# Flag
`picoCTF{not_all_spaces_are_created_equal_178d720252af1af29369e154eca23a95}`
