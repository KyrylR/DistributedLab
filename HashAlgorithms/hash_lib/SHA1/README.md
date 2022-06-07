# Theory
In fact, a feature of SHA-1 is the cyclic mixing and use of basic bitwise operations on the input data. 
Scheme of execution of one cycle of SHA-1 algorithm is as follows:


Figure 2.1 - Scheme of execution of one SHA-1 algorithm cycle

Where Kt are constants;
* Ft - variable function (changes every 20 cycles);
* Wi - modified element of incoming message (4 bytes);
* << x - cyclic shift to the left.

The text of the standard itself and test vectors can be found 
at the following [link](https://csrc.nist.gov/csrc/media/publications/fips/180/2/archive/2002-08-01/documents/fips180-2.pdf)

## Pseudo-code:
``` 
function GetSHA1Hash (message) 
    begin
h0 = 0x67452301
h1 = 0xEFCDAB89
h2 = 0x98BADCFE
h3 = 0x10325476
h4 = 0xC3D2E1F0 //variables initialization    
ml = message length in bits
 
break message into 512-bit chunks (after message processing)
for each chunk
    break chunk into sixteen 32-bit big-endian words w[i], 0 ≤ i ≤ 15
    for i from 16 to 79
w[i] = (w[i-3] xor w[i-8] xor w[i-14] xor w[i-16]) leftrot 5
    
a = h0
    b = h1
    c = h2
    d = h3
    e = h4
 
    for i from 0 to 79 {
        if 0 ≤ i ≤ 19 then
            f = (b and c) or ((not b) and d)
            k = 0x5A827999
        else if 20 ≤ i ≤ 39
            f = b xor c xor d
            k = 0x6ED9EBA1
        else if 40 ≤ i ≤ 59
            f = (b and c) or (b and d) or (c and d) 
            k = 0x8F1BBCDC
        else if 60 ≤ i ≤ 79
            f = b xor c xor d
            k = 0xCA62C1D6
 
        temp = (a leftrot 5) + f + e + k + w[i]
        e = d
d = c
        c = b leftrotate 30
        b = a
a = temp
}
    h0 = h0 + a
    h1 = h1 + b 
    h2 = h2 + c
    h3 = h3 + d
    h4 = h4 + e
 
hash = (h0 lshift 128) or (h1 lshift 96) or (h2 lshift 64) or (h3 lshift 32) or h4 // concat
```