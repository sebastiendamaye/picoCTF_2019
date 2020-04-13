# Glory of the Garden
## Question
>This [garden](files/garden.jpg) contains more than it seems. You can also find the file in `/problems/glory-of-the-garden_3_346e50df4a37bcc4aa5f6e5831604e2a` on the shell server.

## Hint
>What is a hex editor?

# Solution
Let's use the `strings` command and filter the output to reveal the flag:
~~~~
$ strings garden.jpg | grep pico
Here is a flag "picoCTF{more_than_m33ts_the_3y35a97d3bB}"
~~~~

# Flag
`picoCTF{more_than_m33ts_the_3y35a97d3bB}`
