# Tapping
## Question
>Theres tapping coming in from the wires. What's it saying `nc 2019shell1.picoctf.com 21897`.

## Hint
>What kind of encoding uses dashes and dots?

>The flag is in the format `PICOCTF{}`

# Solution
Here is what we get when we connect:
~~~~
$ nc 2019shell1.picoctf.com 21897
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ---.. .---- ---.. ..--- ..--- ....- ..... --... ..... } 
~~~~

It looks like [Morse Code](https://en.wikipedia.org/wiki/Morse_code). You can use an online tool (e.g. https://morsecode.world/international/translator.html) to decode the message.

# Flag
`PICOCTF{M0RS3C0D31SFUN1818224575}`
