# extensions
## Question
>This is a really weird text file [TXT](files/flag.txt)? Can you find the flag?

## Hint
>How do operating systems know what kind of file it is? (It's not just the ending!

>Make sure to submit the flag as `picoCTF{XXXXX}`

# Solution
We are provided with a `*.txt` file but the file is actually a `*.png`:
~~~~
$ file flag.txt 
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
~~~~

Rename the file and open the picture:
~~~~
$ mv flag.txt flag.png
$ eog flag.png
~~~~

!["flag"](files/flag.png "flag")

# Flag
`picoCTF{now_you_know_about_extensions}`
