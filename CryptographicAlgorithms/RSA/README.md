# RSA algorithm

RSA is an asymmetric encryption algorithm. 
It is very commonly used today to create a secure channel between users 
(forming a shared secret and encrypting it with RSA). 
Sequence of steps of RSA algorithm (key generation):
1. Two large prime numbers p and q are chosen;
2. Calculate: n = p ⋅ q, m = (p - 1) ⋅ (q - 1);
3. A random number d, mutually prime with m, is chosen;
4. Determine a number e for which the following expression is true: (e ⋅ d) mod (m) = 1;
5. The numbers e and n are the public key, and the numbers d and n are the private key.

The public key encrypts the message and the private key decrypts it. 
The pair of numbers of the private key is kept secret.

Information encrypting and decrypting using RSA algorithm:
1. The source text is split into blocks, each of which can be represented as a number M(i);
2. The text is encrypted as follows: C(i) = (M(i)e) mod n;
3. The decryption of the message is performed as follows: M(i) = (C(i)d) mod n.

### Pseudo-code:
```
KeyGen(){
P and Q <= primary big numbers.
n = P*Q.
     e <= integer value, not be a factor of n, 1<e<Φ(n), Φ(n) = (P-1)(Q-1)    
d = (k*Φ(n) + 1) / e , for some integer k
 
    PrivateKey (d, n)
    PublicKey (e, n)
}
 
Encrypt(message, PublicKey){
    return powmod(message, e, n)
}
 
Decrypt(ciphertext, PrivateKey){
    return powmod(ciphertext, d, n)
}
``` 

---
[Text of the standard itself and test vectors](https://datatracker.ietf.org/doc/html/rfc3447)
