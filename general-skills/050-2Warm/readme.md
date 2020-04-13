# 2Warm 
## Question
>Can you convert the number `42` (base 10) to binary (base 2)?

## Hint
>Submit your answer in our competition's flag format. For example, if you answer was `11111`, you would submit `picoCTF{11111}` as the flag.

# Solution
~~~~
$ echo "picoCTF{"$(python -c "print(bin(42)[2:])")"}"
picoCTF{101010}
~~~~

# Flag
`picoCTF{101010}`
