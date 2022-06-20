# RC4 algorithm

RC4 generates a pseudorandom stream of bits (a key-stream). As with any stream cipher,
these can be used for encryption by combining it with the plaintext using bit-wise exclusive-or;
decryption is performed the same way (since exclusive-or with given data is an involution).
This is similar to the one-time pad except that generated pseudorandom bits, rather than a prepared stream, are used.

To generate the key-stream, the cipher makes use of a secret internal state which consists of two parts:
A permutation of all 256 possible bytes (denoted "S" below).
Two 8-bit index-pointers (denoted "i" and "j").

The permutation is initialized with a variable length key, typically between 40 and 2048 bits,
using the key-scheduling algorithm (KSA). Once this has been completed, the stream of bits is
generated using the pseudo-random generation algorithm (PRGA).

### Algorithm

The algorithm operates on a user-selected variable-length key(K) of 1 to 256 bytes (8 to 2048 bits), typically between 5
and 16 bytes. To generate a 256-byte state vector S, the master key is used.
The first step is the array initialization. It is a character array of size 256 i.e. S[256]. After that, for every
element of the array, we initialize S[i] to i.

```
Code for array initialization:
Char S[256];
int i;
for(i=0;i<256;i++)
S[i] = i
The array will look like -
S[] = {0, 1, 2, 3, ------, 254, 255}
```


After this, we will run the KSA algorithm-

KSA is going to use the secret key to scramble this array. KSA is a simple loop, in which we are having two variable i
and j. We are using these variables to rearrange the array. Rearranging the array is done by using a secret key.

```
Code for KSA (Key Scheduling Algorithm ) :
int i, j=0;
for(i=0;i<256;i++)
{
j=( j + S[i] + T[i]) mod 256;
Swap(S[i], S[j]);
}
```

KSA has been scrambled, S[256] array is used to generate the PRGA(Pseudo Random Generation Algorithm). This is the
actual Keystream.

```
Code for PRGA ( Pseudo Random Generation Algorithm ):
i=j=0;
while(true)
{
i = ( i + 1 ) mod 256;
j = ( j + S[i] ) mod 256;
Swap( S[i], S[j] );
t = ( S[i] + S[j] ) mod 256 ;
k = S[t];
}
```

This is the next step of scrambling.

---
[What is RC4 Encryption?](https://www.geeksforgeeks.org/what-is-rc4-encryption/)
