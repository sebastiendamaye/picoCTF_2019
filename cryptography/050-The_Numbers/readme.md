# The Numbers
## Question
>The [numbers](files/the_numbers.png)... what do they mean?

## Hint
>The flag is in the format PICOCTF{}

# Solution
The numbers are the letters of the alphabet (A=1, B=2, C=3, ...).
~~~~
$ python
>>> a = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
>>> ''.join([chr(i+64) for i in a])
'PICOCTFTHENUMBERSMASON'
~~~~

# Flag
`PICOCTF{THENUMBERSMASON}`
>
