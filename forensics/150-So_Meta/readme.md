# So Meta
## Question
>Find the flag in this [picture](files/). You can also find the file in `/problems/so-meta_4_4e8d17dbd28e1fdfe82ba31ceb021615`.

## Hint
>What does meta mean in the context of files?

>Ever hear of metadata?

# Solution
Running `strings` against the file will reveal all the strings, including the flag:
~~~
$ strings pico_img.png | grep pico
picoCTF{s0_m3ta_9a16fd1d}
~~~~

But because we are asked to read the meta information, we can also use `exiftool` (see variable `Artist`).
~~~~
$ exiftool pico_img.png 
ExifTool Version Number         : 11.93
File Name                       : pico_img.png
Directory                       : .
File Size                       : 106 kB
File Modification Date/Time     : 2019:09:28 23:51:02+02:00
File Access Date/Time           : 2020:04:14 10:24:02+02:00
File Inode Change Date/Time     : 2020:04:14 10:24:01+02:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Warning                         : [minor] Text chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_9a16fd1d}
Image Size                      : 600x600
Megapixels                      : 0.360
~~~~

# Flag
`picoCTF{s0_m3ta_9a16fd1d}`
