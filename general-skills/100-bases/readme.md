# bases
## Question
>What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

## Hint
>Submit your answer in our competition's flag format. For example, if you answer was `hello`, you would submit `picoCTF{hello}` as the flag.

# Solution
$ echo "picoCTF{"$(echo -n "bDNhcm5fdGgzX3IwcDM1" | base64 -d)"}"
picoCTF{l3arn_th3_r0p35}

# Flag
`picoCTF{l3arn_th3_r0p35}`
