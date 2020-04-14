# plumbing
## Question
>Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `2019shell1.picoctf.com 18944`.

## Hint
>Remember the flag format is `picoCTF{XXXX}`

>What's a pipe? No not that kind of pipe... This kind

# Solution
When you connect, you will get a lot of such sentences:
~~~~
$ nc 2019shell1.picoctf.com 18944
This is defintely not a flag
This is defintely not a flag
Again, I really don't think this is a flag
Not a flag either
I don't think this is a flag either
Again, I really don't think this is a flag
This is defintely not a flag
I don't think this is a flag either
Not a flag either
Again, I really don't think this is a flag
I don't think this is a flag either
Not a flag either
This is defintely not a flag
This is defintely not a flag
This is defintely not a flag
Not a flag either
I don't think this is a flag either
Again, I really don't think this is a flag
~~~~

Instead of waiting for manually looking for our flag, we can filter the output directly:
~~~~
$ nc 2019shell1.picoctf.com 18944 | grep picoCTF
picoCTF{digital_plumb3r_1d5b7de7}
~~~~

# Flag
`picoCTF{digital_plumb3r_1d5b7de7}`
