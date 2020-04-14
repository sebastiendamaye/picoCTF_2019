# Based
## Question
>To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc 2019shell1.picoctf.com 29594`.

## Hint
>I hear python can convert things.

>It might help to have multiple windows open

# Solution
Connect with `nc 2019shell1.picoctf.com 29594` and fire up a python shell in another window.

## Question 1
**Question**
~~~~
Please give the 01100011 01101000 01100001 01101001 01110010 as a word.
~~~~

**Answer**
```python
>>> a = "01100011 01101000 01100001 01101001 01110010"
>>> ''.join([chr(int(i,2)) for i in a.split(' ')])
'chair'
```

## Question 2
**Question**
~~~~
Please give me the  164 141 142 154 145 as a word.
~~~~

**Answer**
```python
>>> a = "164 141 142 154 145"
>>> ''.join([chr(int(i,8)) for i in a.split(' ')])
'table'
```

## Question 3
**Question**
~~~~
Please give me the 736f636b6574 as a word.
~~~~

**Answer**
```python
>>> a = "736f636b6574"
>>> ''.join([chr(eval('0x'+a[i:i+2])) for i in range(0,len(a), 2)])
'socket'
```

# Flag
`picoCTF{learning_about_converting_values_e67b1990}`

