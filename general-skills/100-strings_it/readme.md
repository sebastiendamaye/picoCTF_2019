# strings it
## Question
>Can you find the flag in [file](files/strings) without running it? You can also find the file in `/problems/strings-it_4_e276260a1b64a734b4178a280d25b754` on the shell server.

## Hint
>[strings](https://linux.die.net/man/1/strings)

# Solution
~~~~
$ strings strings | grep pico
picoCTF{5tRIng5_1T_c611cac7}
~~~~

# Flag
`picoCTF{5tRIng5_1T_c611cac7}`
