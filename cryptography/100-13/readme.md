# TITLE_GOES_HERE
## Question
>Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}`

## Hint
>This can be solved online if you don't want to do it by hand!

# Solution
ROT13 is a specific case of the Caesar cipher, with an offset of 13. This can be easily decoded in python using the [`codecs`](https://docs.python.org/3/library/codecs.html#codecs.Codec.decode) library:
~~~~
$ python -c "import codecs; print(codecs.decode('cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}', 'rot_13'))"
picoCTF{not_too_bad_of_a_problem}
~~~~

# Flag
`picoCTF{not_too_bad_of_a_problem}`
