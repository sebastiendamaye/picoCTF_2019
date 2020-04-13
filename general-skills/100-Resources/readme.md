# Resources
## Question
>We put together a bunch of resources to help you out on our website! If you go over there, you might even find a flag! `https://picoctf.com/resources` ([link](https://picoctf.com/resources))

## Hint
>NA

# Solution
The flag can be found directly on the page. Let's extract it:
~~~~
$ curl -s https://picoctf.com/resources | grep 2019 | grep -o "picoCTF{.*}"
picoCTF{r3source_pag3_f1ag}
~~~~

# Flag
`picoCTF{r3source_pag3_f1ag}`
