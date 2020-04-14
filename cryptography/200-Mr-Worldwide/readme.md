# Mr-Worldwide
## Question
>A musician left us a [message](files/message.txt). What's it mean?

## Hint
>NA

# Solution
These are coordinates:
~~~~
$ cat message.txt 
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
~~~~

| Coordinates | Google maps information | Letter (City) |
|---|---|---|
| (35.028309, 135.753082) | Nakanocho, Kamigyo Ward, Kyoto, Japan | `K`yoto |
| (46.469391, 30.740883) | Odesa, Odessa Oblast, Ukraine, 65000 | `O`desa |
| (39.758949, -84.191605) | Dayton, OH 45402, United States | `D`ayton |
| (41.015137, 28.979530) | European Side, Hoca Paşa, 34110 Fatih/İstanbul, Turkey | `I`stanbul |
| (24.466667, 54.366669) | Hazza Bin Zayed the First St - Abu Dhabi - United Arab Emirates | `A`bu Dhabi |
| (3.140853, 101.693207) | 50480 Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia | `K`uala Lumpur |
| _ | _ | `_` |
| (9.005401, 38.763611) | Kirkos, Addis Ababa, Ethiopia | `A`ddis Ababa |
| (-3.989038, -79.203560) | Av Nueva Loja, Loja, Ecuador | `L`oja |
| (52.377956, 4.897070) | Martelaarsgracht 5, 1012 TN Amsterdam, Netherlands | `A`msterdam |
| (41.085651, -73.858467) | Sleepy Hollow, NY 10591, United States | `S`leepy Hollow |
| (57.790001, -152.407227) | 1 Chadrick Cove, Kodiak, AK 99615, United States | `K`odiak |
| (31.205753, 29.924526) | Faculty Of Engineering, Al Azaritah WA Ash Shatebi, Qism Bab Sharqi, Alexandria Governorate, Egypt | `A`lexandria |


# Flag
`picoCTF{KODIAK_ALASKA}`
