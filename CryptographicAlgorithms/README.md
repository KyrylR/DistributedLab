# Solutions to the Cryptographic algorithms exercise

Distributed Lab Course in Spring of 2022.

## Task: 

In this lab work I have implemented the following algorithms:
1. RSA
2. RC4

---

#### After performing one of the steps above, execute the following command sequences to execute appropriate algorithms:
* RSA test:
```
cd .\CryptographicAlgorithms\RSA\   
python .\test_RSA.py
```

* RC4 test:
```
cd .\CryptographicAlgorithms\RC4\
python .\test_RC4.py 
```

### Test result

##### RSA
```
Public key: 49475
Private key: 1558884191
RSA Modulas: 2225243029
Message: Hello!
Encrypt: 1181560667 1681105360 1958978981 1958978981 2024689029 1728958010
Decrypt: Hello!
.
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
```

##### RC4

```
Your plain text is: Entered plain text
Your RC4 text is: 'çÈ#\x94}\x8fØ®[üE\x8f4zõ¦Ê+'
Decryption: Entered plain text

.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

## Purpose of the work

To study  the most common cryptographic algorithms and implement one.

### Theoretical background

The development of cryptography dates back to ancient times and its history goes back more than 4 thousand years. 
At the beginning, cryptography had only one job - to ensure confidentiality during the transfer and storage of data. 
Currently, cryptography is also used to ensure the integrity and authenticity of data.
Today, cryptography is based on mathematical operations, which are defined in sections of mathematics such as number 
theory, group theory, rings, fields, etc.
Modern cryptography consists of symmetric and asymmetric encryption schemes, data hashing schemes, digital signature 
schemes, key management methods, zero disclosure proof schemes, methods of cryptanalysis and post-quantum cryptography, etc.
The main objective of information security is to ensure:
* data confidentiality, 
* data integrity,
* data availability, 
* data authenticity.
Confidentiality implies that unauthorised persons cannot access data that is stored or transmitted. This security 
service can be ensured through the use of encryption algorithms. 
Integrity implies that the data has not been altered during transmission or operation of the data. Hash functions 
are used to check the integrity of the data.
Accessibility implies that subjects who are entitled to access the information are guaranteed access to it. 
This security service cannot be provided by the use of cryptographic methods.
Authenticity implies that it is possible to prove that the data really came from a specific author. 
Data authenticity is verified by means of a digital signature mechanism (or MAC codes).

#### Encryption 

The encryption process transforms the raw data into a byte sequence (whose contents cannot be predicted before the 
encryption is executed), the original content of which cannot be retrieved by the party who does not have the 
corresponding decryption key. Encrypted data can be converted back to its original form, provided that the appropriate
key is available. 

There are two basic types of encryption - symmetric and asymmetric.
* Symmetric encryption uses the same key for both encryption and decryption.
* Asymmetric encryption uses two different keys: one for encryption (public key) and one for decryption (private key).
