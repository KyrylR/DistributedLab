
# Theory
Keccak (SHA-3) is a variable-bit hashing algorithm. The hash function is based on a cryptographic sponge construction,
in which data is first "absorbed" into the sponge, with the original message M being subjected to multirandom 
permutations f, and then the result Z being "squeezed" out of the sponge. In the "soak" phase, the message blocks are 
summed modulo 2 with a subset of the state, after which the entire state is transformed using the permutation function f. 
In the "squeeze" phase, the output blocks are read from the same state subset modified by the permutation function f. 
The basis of the squeeze function of the algorithm is the function f, which performs the shuffling of the internal state 
of the algorithm. State A is represented as a 5×5 array whose elements are 64-bit words initialized with zero bits (i.e.,
the state size is 1600 bits). The function f performs 24 rounds, in each of which stepwise transformations θ, ρ, π, χ, ι 
are performed.

At the beginning of the transformation padding (fill/add) is performed. Padding is needed to reduce the original message 
to a fixed-length string. Then the Absorb function is executed. This function is intended for splitting the input 
(passed through padding) string into components that will be sequentially used for the following conversions:
* θ transformation;
* ρ and π transformations;
* χ transformation;
* ι transformation.
    This is followed by the Squeezing procedure. This procedure is necessary to compute the final hash value.

Pseudo-code:
```
Keccak[r,c](Mbytes || Mbits) {
  # Padding
  d = 2^|Mbits| + sum for i=0...|Mbits|-1 of 2^i*Mbits[i]
  P = Mbytes || d || 0x00 || ... || 0x00
  P = P xor (0x00 || ... || 0x00 || 0x80)
 
  # Initialization
  S[x,y] = 0, for (x,y) in (0...4,0...4)
 
  # Absorbing phase
  for each block Pi in P
    S[x,y] = S[x,y] xor Pi[x+5*y], for (x,y) such that x+5*y < r/w
    S = Keccak-f[r+c](S)
 
  # Squeezing phase
  Z = empty string
  while output is requested
    Z = Z || S[x,y], for (x,y) such that x+5*y < r/w
    S = Keccak-f[r+c](S)
 
  return Z
}
```

Constant values for RC[i]:
RC[0] 0x000000000000000001 RC[12] 0x000000008000808B
RC[1] 0x0000000000008082 RC[13] 0x8000000000008B
RC[2] 0x800000000000808A RC[14] 0x8000000000008089
RC[3] 0x8000000080008000 RC[15] 0x8000000000008003
RC[4] 0x000000000000808B RC[16] 0x8000000000008002
RC[5] 0x0000000080000001 RC[17] 0x8000000000000080
RC[6] 0x8000000080008081 RC[18] 0x00000000000000800A
RC[7] 0x8000000000008009 RC[19] 0x800000008000000A
RC[8] 0x000000000000008A RC[20] 0x8000000080008081
RC[9] 0x0000000000000088 RC[21] 0x8000000000008080
RC[10] 0x0000000080008009 RC[22] 0x0000000080000001
RC[11] 0x000000008000000A RC[23] 0x8000080008008

Pseudo-code of Keccak-f:
 ```
Keccak-f[b](A) {
  for i in 0...n-1 // n=24
    A = Round[b](A, RC[i])
  return A
}
 
Round[b](A,RC) {
  # θ step
  C[x] = A[x,0] xor A[x,1] xor A[x,2] xor A[x,3] xor A[x,4], for x in 0...4
  D[x] = C[x-1] xor rot(C[x+1],1), for x in 0...4
  A[x,y] = A[x,y] xor D[x], for (x,y) in (0...4,0...4)
 
  # ρ and π steps
  B[y,2*x+3*y] = rot(A[x,y], r[x,y]), for (x,y) in (0...4,0...4)
 
  # χ step
  A[x,y] = B[x,y] xor ((not B[x+1,y]) and B[x+2,y]), for (x,y) in (0...4,0...4)
 
  # ι step
  A[0,0] = A[0,0] xor RC
 
  return A
}
```
Constant values r[x,y]:

You can find the text of the standard itself and the test vectors at the following 
[link](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)


