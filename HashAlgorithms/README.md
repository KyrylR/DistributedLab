# Solutions to the Hash functions exercise

Distributed Lab Course in Spring of 2022.

## Task: 

In this lab work I have implemented the following hash function algorithms:
1. SHA-1 
2. Keccak.

---

### Executing program

* To run the tests, you must activate hash_lib_venv:
```
cd .\HashAlgorithms
.\hash_lib_venv\Scripts\activate
```

* Alternatively, if you wish, you can install the hash-lib library:
```
cd .\HashAlgorithms
pip3 install .\dist\hash_lib-0.0.1-py3-none-any.whl 
```

#### After performing one of the steps above, execute the following command sequences to execute appropriate algorithms:
* SHA1 test:
```
cd .\HashAlgorithms\tests\     
python .\test_SHA1.py
```
    
* Keccak test:
```
cd .\HashAlgorithms\tests\     
python .\test_Keccak.py
```
### Test result

##### SHA1
```
To ensure that the algorithm is implemented correctly, you can use this website: 
https://emn178.github.io/online-tools/sha1.html
--------------------
Message:        Keccak
My hash:        34a663a04dabe538f7e6b01cb2e4727d55d1364b
Expected hash:  34a663a04dabe538f7e6b01cb2e4727d55d1364b
--------------------
.--------------------
Message:        SHA1 and other hash functions ...(see string in code)
My hash:        7e16b5527c77ea58bac36dddda6f5b444f32e81b
Expected hash:  7e16b5527c77ea58bac36dddda6f5b444f32e81b
--------------------
.--------------------
Message:        123123123
My hash:        88ea39439e74fa27c09a4fc0bc8ebe6d00978392
Expected hash:  88ea39439e74fa27c09a4fc0bc8ebe6d00978392
--------------------
.
----------------------------------------------------------------------
Ran 3 tests in 0.003s

OK
```

##### Keccak
```
To ensure that the algorithm is implemented correctly, you can use this website: 
https://emn178.github.io/online-tools/keccak_256.html
--------------------
Message:        Keccak
My hash:        868c016b666c7d3698636ee1bd023f3f065621514ab61bf26f062c175fdbe7f2
Expected hash:  868c016b666c7d3698636ee1bd023f3f065621514ab61bf26f062c175fdbe7f2
--------------------
.--------------------
Message:        123123123
My hash:        250f78769f22a8c43a2b767fde4b093fbbcdc28bd7ecac4bad883a4b0fcf30e3
Expected hash:  250f78769f22a8c43a2b767fde4b093fbbcdc28bd7ecac4bad883a4b0fcf30e3
--------------------
.--------------------
Message:        Lorem ipsumLorem ipsumLorem ip...(see string in code)
My hash:        6cc288d3b960a14fae795e2899957d61ba6a4067ac2c727cbb2b03192a346113
Expected hash:  6cc288d3b960a14fae795e2899957d61ba6a4067ac2c727cbb2b03192a346113
--------------------
.
----------------------------------------------------------------------
Ran 3 tests in 0.494s

OK
```

## Purpose of the work

To study the principles of hashing algorithms and to implement them.

### Theoretical background

The development of cryptography goes back to ancient times, and its history goes back more than 4 thousand years. 
At first, cryptography had only one job - to ensure confidentiality during the transfer and storage of data. Today, 
cryptography is also used to ensure the integrity and authenticity of data.
Today, cryptography is based on mathematical operations, which are defined in sections of mathematics such as number 
theory, group theory, rings, fields, etc.
Modern cryptography consists of symmetric and asymmetric encryption schemes, data hashing schemes, digital signature 
schemes, key management methods, zero disclosure proof schemes, methods of cryptanalysis and post-quantum cryptography, 
etc.

The main objective of information security is to ensure:
* data confidentiality,
* data integrity,
* availability of data,
* data confidentiality, data integrity, data availability, data authenticity.

Confidentiality implies that unauthorised persons cannot access data that is stored or transmitted. This security 
service can be ensured through the use of encryption algorithms. 
Integrity implies that the data has not been altered during transmission or operation of the data. Hash functions 
are used to check the integrity of the data.
Accessibility implies that subjects who are entitled to access the information are guaranteed access to it. This 
security service cannot be provided by the use of cryptographic methods.
Authenticity implies that it is possible to prove that the data really came from a specific author. Data authenticity 
is verified using a digital signature mechanism (or MAC codes).

### Hash functions

A hash function converts arbitrarily-length data into a fixed-length string. Due to the properties of hash 
functions it is impossible to obtain the original data with only its hash value. If even a small change is made 
to the original value, the resulting value will be significantly different.

![image](https://user-images.githubusercontent.com/89979281/171890997-38202c4d-4acf-4c8e-9888-026d17bdf3cc.png)

Figure 1.1 - How a hash function works