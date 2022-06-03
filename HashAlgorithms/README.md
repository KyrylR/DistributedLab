# Solutions to the Hash functions exercise

Distributed Lab Course in Spring of 2022.

## General information 

Purpose of the work: to study the principles of hashing algorithms and to implement one of them.

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


Figure 1.1 - How a hash function works



## Task: 

You can use any programming language convenient for you to perform the laboratory work. The task is to 
implement one of the proposed algorithms (you can choose to implement an algorithm that is not described 
in this tutorial).

### Hash function:
1. SHA-1 
2. Keccak or any other algorithm of your choice.


Note that the choice of level for the task does not imply the need to implement all of the above algorithms.
More than 1 algorithm is encouraged, but not required.


---


### Executing program

* Do following sequence of commands to run SHA1 tests:
```
cd .\HashAlgorithms\SHA1\
python .\test.py
```

#### Test result

```
>>> running: test_similar
... test_similar: checking digest differences
... test_similar: success
.
----------------------------------------------------------------------
Ran 4 tests in 0.012s

OK
```

* Do following sequence of commands to run Keccak demo:
```
cd .\HashAlgorithms\Keccak\ 
python .\demo.py
```

#### Main program result

```
Create a Keccak function with (r=1088, c=512 (i.e. w=64))
String ready to be absorbed: 37a636d7dafdf259b7287eddca2f58099e98619d2f99bdb8969d7b14498102cc065201c8be190000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080 (will be completed by 64 x '00')
Current value of state: Before first round
        ['0x59f2fddad736a637', '0x9582fcadd7e28b7', '0xb8bd992f9d61989e', '0xcc028149147b9d96', '0x19bec8015206']
        ['0x0', '0x0', '0x0', '0x0', '0x0']
        ['0x0', '0x0', '0x0', '0x0', '0x0']
        ['0x0', '0x8000000000000000', '0x0', '0x0', '0x0']
        ['0x0', '0x0', '0x0', '0x0', '0x0']
Current value of state: Satus end of round #1/24
        ['0x4bceebf3c4c9247f', '0x5b318eed8eed4ece', '0xdc22d20acd42cfe4', '0x4b013d1793d6b7b3', '0xce8f2e8dac4e4578']
        ['0xa1919a02c723f3b9', '0x8daae56d37975ac1', '0xd58891f191e91909', '0x3715f0178ba6d3e', '0x4c6184c606352e35']
        ['0xe3b340de6426662a', '0x142b6ebf70c466af', '0xbc9fc53d2c5579d4', '0xa478fcb076c2cd45', '0xce5ddd50fe4ca45']
        ['0x13bebd3927a7331a', '0xbf505ed1228562bb', '0x272e929d845c4bb2', '0x97ac7ad1283f10ac', '0xbef8bf2a5a0d2399']
        ['0x28588d3708836c80', '0xb95a5cd52906b13e', '0xb49d02d64ef7655', '0xf25ed32d28a47424', '0xe3236cd796d2cd36']
Current value of state: Satus end of round #2/24
        ['0x18942e9a0d72311', '0x851cf4d1745a34a0', '0x3a123d295671ea1', '0xcd255f2186e503fe', '0x1e634e9dceae97df']
        ['0xbd0ee9e6673e6d1e', '0x8e0acb3ab9ab9b1', '0xe23fb65449ff5815', '0x913f1f7dfeab805e', '0x3b60f32c6b1716df']
        ['0xb77c0e424d1d1eaa', '0xa73c3f8c2f1f8a53', '0x886d9b20ad04dc40', '0x35ba3a54a1803559', '0x9c0d8779a7336ab0']
        ['0xbf155f76edbf98cc', '0xcd8fd75ab3596942', '0x93d9cd38c7d5911b', '0x7588ec05a61a78b4', '0xb5460d568f2a685b']
        ['0x82fb1a7108252611', '0x6fd3c96be89722a4', '0x47b0e4958425c6c3', '0x3875c6123c2e5b95', '0xb2d3956dd54df276']
Current value of state: Satus end of round #3/24
        ['0x2f28b1a7e4084f42', '0x4dd11d4944e5ab2', '0x5a3a05270971607', '0x7306b42fd47ee5f5', '0x11a89642bef18eab']
        ['0x4d5aaac9058014c', '0x3b7b63003e57756b', '0xf6a87fd80e8f93d2', '0xc3a94045cfe054d9', '0xcad886affa3f0418']
        ['0xe07eb53c66faafb2', '0x86c27c5946ce9104', '0x7e246e9faffeaab1', '0xa0977902c9eb73ff', '0x2af553ea3b11f529']
        ['0xd2db4ee53b90eff8', '0x1730e9a972ddaaf1', '0x76d748b6a741dba8', '0xba68f3cbfb078f7f', '0x8ff8c8a4fff49873']
        ['0x7af0faccdbe1af65', '0xc448f93f882a8a15', '0x11840b4bd0af30d', '0x90c052210e7cf1af', '0x8fc19ded8c9f5a86']
Current value of state: Satus end of round #4/24
        ['0x98ecfad785b14c5d', '0xadbd92a72c836dbd', '0x3b34f089604d873e', '0xc2ad302808f87c53', '0x44493898933cd20']
        ['0x4ebfdb8ea6c1e66c', '0x61098866a5917308', '0x6c907af67cfd957a', '0x80a15921b23a02f3', '0xe2c480947db4f327']
        ['0x3758bdc3a0fdeca0', '0x4dce30f5a0995b58', '0x5035ba5d73f35258', '0x1df808b60f78b252', '0x2d5ec44b5e16e89']
        ['0x4fe3e30a7f85d477', '0x95c5a20171929fe', '0x9c58a0cc9cea904a', '0xcdb6fcbe4be8f086', '0xb1915cd7aac4b184']
        ['0x12a75dd2528b94e6', '0xe935536ec3468216', '0xd407b07a9a812a35', '0xccfc722ef6cb1634', '0xa9ce441313a890cd']
Current value of state: Satus end of round #5/24
        ['0x218253fdd6196173', '0x7824f6b08bf4cc96', '0x3682ed621a9beea1', '0x663a50af2f5f8da2', '0xa3f2f58dc5032fff']
        ['0x311c231bffc56cd0', '0x83a582bdb3650a53', '0x4ba8cdf71236b96e', '0x3774301d63a4091', '0x83efa90fcee4f014']
        ['0x1cd1eac9d9b73ef5', '0xbf72800c04487ffd', '0x71248957d97c75e6', '0xbde3dee55b94c947', '0xd1c95084e2e47327']
        ['0x3faf223b2f937051', '0x5c94ba1118762e69', '0xa54578e8aeae2ebc', '0x287078441d77a0db', '0x987bbf99814b7925']
        ['0xc9f2c36b5b88bb1e', '0xcf48adbac3118385', '0x1c2ce4021af2f473', '0x9cb5778a9faec8d4', '0x2d91fc02fa44c342']
Current value of state: Satus end of round #6/24
        ['0xde25d9f56d2fce44', '0xaa19ed3f91392bca', '0x25da0357b5ffbbf1', '0x30a575a254bff7a', '0x920614a147d28cf7']
        ['0xe66db589078a1a1d', '0xd72acb57d4867a49', '0xb78b105864b80ab7', '0x60739c083577d242', '0x3368d20297e2270a']
        ['0x39e5cd2f003f2a6d', '0x4a1346d76f95e11', '0xe6301a7bff1172a4', '0xe5fa27b40bea6d80', '0x2a860b226670df5d']
        ['0x2f6ed59db1ddee8b', '0x2e753dadc7ddec7a', '0xdac5277105488ebf', '0x146a55a0514e915c', '0x64b086fd9fdc2a2d']
        ['0xc83e2370ed6d6085', '0x5097367f950e574a', '0x2eb7e7f0e3987665', '0x4692a70b1340a645', '0x6ed3e65231e8be0f']
Current value of state: Satus end of round #7/24
        ['0x71444f3587795742', '0x47f5273f4cf26baa', '0xb582eb5db3bda16d', '0x81332249d832efda', '0x9358e1130af6fdec']
        ['0xb992d940aa05fd06', '0x7a3e06ea29d8ae94', '0x34529d3cdb05bcfd', '0x50967915a73f4450', '0x920e1efca3d5a720']
        ['0xa12458d634b7f36a', '0x35d81eda7645593', '0xfd271b6edfcdf96a', '0x3931cebe188fbb7d', '0xf589dde2264d19d2']
        ['0xa1123298715d762c', '0xcd47350612eca0bd', '0x970177477d216ed5', '0x20c0b7ff6bb2a81', '0x348c9b1222c9afcd']
        ['0xe2934d9e9aefb9ad', '0x3f3b20c7d8e4be40', '0x2715043143fc4dab', '0x264e9a461bc082d5', '0xc4577aa988a14016']
Current value of state: Satus end of round #8/24
        ['0xac952632b7f2653f', '0x6372e0c287b144f', '0x423bb56b693b051a', '0x25d725879378fcf4', '0x842c7122fd73df90']
        ['0xa09a771d447f83b5', '0x86ccb6bd7bd8a5ff', '0xefe79491a1233876', '0xd6926fce531e97d8', '0x980effedc2491615']
        ['0xfa375499185fe03e', '0xed40deb5ac10fa98', '0x55b469dac3fe7bac', '0xd57dc20f9baa30bc', '0x9262b5b08325e78b']
        ['0x1b35ca59b95b8ab6', '0xbd60c6600cf63169', '0xba50e9182228d2df', '0xe581f30ac0e26903', '0x3b22b02117fc7555']
        ['0xb8b5144237cf279e', '0xa342be390312cde4', '0x31f431b2bc5f3e36', '0x258d91f98fb5b88d', '0x35709c74e702d7fb']
Current value of state: Satus end of round #9/24
        ['0xe9f5e9b33babaedb', '0xddbb03479da0d672', '0xb6a7ef1626927ad0', '0x310897b9547a4df9', '0x6464dc09c6f70f07']
        ['0x516a9cf8c5e3f3b1', '0x3165c454b42e54e8', '0x68b9e25528aced01', '0x71e6c54166db0052', '0xf1c1da549ebbf7bf']
        ['0xca0db9696534d76a', '0x411fe7565246aa92', '0x3b2dd101b81e26f8', '0x67cc4fa12684f274', '0xfa9c2e91011156c1']
        ['0x6d9b1a14325f5857', '0x8211cdd853034a4e', '0x60d03782d3153c76', '0x91ef5b4a8eb8ab4', '0x675260c76e236783']
        ['0x3eff95103fc6e00c', '0x7a101578a02c3612', '0xdc9054ea8768672e', '0x90a07d6a2341b12a', '0x58d3a6db5f5ceba']
Current value of state: Satus end of round #10/24
        ['0x7f420a8608eb01a3', '0xc30d9e26073a5a67', '0x33d1797ea3055275', '0xcffbde1f68c57535', '0x4a4cd1cd4c83007b']
        ['0x89220a96043078c6', '0xd6cefe17894eb34', '0x6950c6e7b389c347', '0x74ace8309f3c18ab', '0x2e4df58176928467']
        ['0x10d7ec6195bee3be', '0x327c6e37b1a96502', '0xd5072c2c135ae448', '0xa77341bce6eb750c', '0x5afeb18b7f927660']
        ['0xaad877f85e8ac76', '0xaa71e7e9e091f541', '0x32aa99006cb4a509', '0xf211b22fb058003e', '0xbb925fa6fdd55b54']
        ['0x4dd59c3f8044ac08', '0x443dc85b5a619a70', '0x2a5b9b2bf6d6ad74', '0x767c7087dd23fa42', '0xb40c80ef9acb02dd']
Current value of state: Satus end of round #11/24
        ['0xcec727166b995c17', '0x5991f86593feed77', '0xd697cab60eaecf9b', '0x9dad9ae5d8e13096', '0xa6d53fec75781a97']
        ['0xdb60a4a741e449e9', '0xff8a72253c33501c', '0x9a42b5b3f63a641', '0xc8f9e17626dc0c66', '0x5802a23d3554a6b']
        ['0x800a5c6551b6f592', '0xe4a702cfc6670ff2', '0xe4a5c8fe02d48c90', '0x440e6ebc3e8ee4e0', '0xbc700c536ebc6a5a']
        ['0xaa8b6efed4887665', '0xf5384f3983da01cc', '0xfce9654c20170635', '0x61d276c29d565830', '0xfba3d8750f13a558']
        ['0x1054aad20f9c6b36', '0x23e288c8102b5b99', '0x3c449381967468ff', '0x34e20ebed592ea8d', '0xf74757b87227be2']
Current value of state: Satus end of round #12/24
        ['0x9f118f95d075f9a', '0x99b12a4bbc6689f9', '0x856c65d8302d7b25', '0x31a21e2342b8918', '0x19f471ba9aac451f']
        ['0xec6fb730ff1932d9', '0xc4dec5d3be075e3', '0x39a3301f2f9e2a3b', '0xc4bf62b74d68957e', '0x240ec8060f18ea8b']
        ['0x8978f30af1f90ea3', '0x642d34353c82ff84', '0x8e014367921be5ba', '0x2c8ac786da1589f0', '0x4671ee987ec9bcee']
        ['0xf56dad6217f5cb5a', '0x2f7702818da82c86', '0x8e8a311977973976', '0xb9af65133cf3a22f', '0x3e0a7e39c4d98d2c']
        ['0x6284138bc02cf4d3', '0xeb7093abc69171a7', '0x7b6576f7ff2dbccd', '0x2e86851a7b891ac1', '0x66eeb216ee17c5bb']
Current value of state: Satus end of round #13/24
        ['0x1236edef29ce7d82', '0xaceb07700acfb97f', '0x73afaa0f9f4eec4e', '0x48475584b58d8a20', '0x602f5281d604396b']
        ['0xbe64b0edd9ab44eb', '0xca9c3fc6ba4a4106', '0x1958801eb12e5686', '0xeb7a0b33c840a01d', '0x564dff8b5ae9b604']
        ['0x796097e065e90f1f', '0x1f209ce57ecb9b89', '0x96b9c38a2b5ac148', '0xd26ee642ade1c1f6', '0x3c49af91d302393d']
        ['0xab65ecc5859e26c9', '0xa10de59b56560325', '0x81ff56c822661451', '0xe6c221fcba9ea3a9', '0x40a778c809bd7d98']
        ['0x9239b1bd02101e1a', '0xede9b19bbea57a2d', '0x4c30eee2162a004b', '0xfa5320f35df2f474', '0x35754c77d748bfc7']
Current value of state: Satus end of round #14/24
        ['0xb2bcb8ed9fae3fe5', '0xc9886c5f8597f88a', '0x332a3c77883cb03', '0x809131e8652d0a46', '0xffaf351107b7609a']
        ['0xa3cef1de00230496', '0x84501e1947ba35e2', '0x8bf24335cd88ff13', '0x127ab59e3a0d6653', '0xe050c7a9de5efd73']
        ['0x633367905c72fade', '0x5342ee6c5549d0fd', '0x712c7f4dea3a21bf', '0xfbee400a799c04b5', '0x47fb1af7f131ebc']
        ['0x5c2a20d1a6a18622', '0x94a7d06f85e4f355', '0x26a0742895046252', '0xe0bdb1ed8fc3b1e4', '0xf4a471370268d0a2']
        ['0x862a7a2ebfdc8d46', '0x1210cda0319d8100', '0x215c24c4a2168f80', '0xd9ae231ff2a48f95', '0xc286911e790faee0']
Current value of state: Satus end of round #15/24
        ['0x2047fa5164981eda', '0xe09c1c351b2e28d4', '0xc9e8ec9639da374', '0x3c6e837f72e9b074', '0xdb7260f6502e9000']
        ['0xd7763a54efc898c', '0x90cbc81b224e3de3', '0xb4553a213e2bca5b', '0x116ca898b75af3e4', '0xd3aba90507d5adff']
        ['0x3ad505429a95a6e3', '0xcc51f3f67acddc08', '0x275990fc5fd7899', '0x205e0cedb6b660c4', '0xaf6263faff083743']
        ['0x375b546ad773f04d', '0x9c2ae08a236511e9', '0xca062256128a8c91', '0x9d6b84c316c04f00', '0x4e7cdbab1125be2d']
        ['0xa8688bcf9e894610', '0x95a971fda748880', '0xf66e6a6a3de568c9', '0x4b450a04b508486a', '0x19d38978ad16646b']
Current value of state: Satus end of round #16/24
        ['0x18bf36b425f4ea29', '0xc18d695b5722cb50', '0xb32137bf2456cab7', '0x978a0ca3677f388e', '0x2ca4e2b803eaa593']
        ['0x8fcc66416dc731d5', '0x406353d86500d558', '0xc16ec40a59b69db4', '0xed7bc16a7c24c7e5', '0x2d0dbd8f84d8e814']
        ['0xcf9d2b03a451caf3', '0x532a3cdb02641c8e', '0x485b9aadbe856b72', '0x23304010ff554304', '0x7e39a80c9a3c3e4b']
        ['0xea37e7cb7e8d235c', '0xe44f99eab8eeb488', '0xccc0f1be1fe27030', '0x125201975ad968aa', '0x6565a2beeb59311e']
        ['0xe4c775675a0ceefb', '0xe9bbe8977b8ca8d2', '0xc98e1ef6eee588fc', '0x534336298c3c3b6c', '0x2bb8f675154b83d6']
Current value of state: Satus end of round #17/24
        ['0x82c53a3d742887d7', '0x6888b6cd0843eeaa', '0xd67fc8ae60c834c6', '0x94c7c243c349e278', '0xfa169197e09cfd7']
        ['0x29334767bc849ca3', '0x4dfa3753695b9e84', '0x454397e628297b54', '0x353b5ddc9f263648', '0x1023dbabed5bcb22']
        ['0xd24b1d4bd4a1dc05', '0x77399833c4550a5b', '0x21270d2b6ae5eb2b', '0x98c66c4bc367f7d4', '0xcec19d50484fad22']
        ['0x534637a255e70c1b', '0x71369680dec8bfa6', '0x76084ce090517bb', '0xfd2af1809c5d192a', '0x513642f79268d4d9']
        ['0x57480d702e8902d2', '0x9bd3df8a78d0bf23', '0x8c746c5020cb7b1c', '0xe093caca1554e23b', '0xac5065b71fefc903']
Current value of state: Satus end of round #18/24
        ['0x5ebd19513279c49e', '0x9a5654766014ac58', '0x99092f0c36459229', '0xdeb3564621cbcff9', '0x466bf5ee2127bd6d']
        ['0xb6dfc003ebd8259b', '0xef73131b594fece9', '0x7aae1514044c6d4c', '0xfc840fd5d93f3558', '0x869bac6161d76e60']
        ['0xa031346d1786a5e', '0x29a15001d1e04bad', '0xe48b200aa19327cf', '0x9f37ee425f9c1a96', '0xa2e576e4027c3967']
        ['0x19a656221fc335e0', '0x6b6f45de26be6aba', '0x4bdd6e929cec7de0', '0xa29cbb2b6a50fbc4', '0xfdc856b4339f635c']
        ['0x4924c2cdd387bff7', '0x8c22936f5f9074c8', '0x1597534892f326dc', '0xa69bee1d2c58b96a', '0x77f5fffe0083da96']
Current value of state: Satus end of round #19/24
        ['0xe0121dc149c3f87b', '0x9aaa906442622a0d', '0x13a5916e75a04d1b', '0xd5269a72c2276050', '0x36931802de81a8c1']
        ['0x4d36c892fd685fcc', '0x370bd1d4e683a78e', '0x9fc094674e30fdcc', '0xc9ef8978afde9a29', '0x98a3aa75a314ef3']
        ['0x34b0b8513f2555f2', '0xd30dc59683cc184c', '0x841472d8980403d5', '0x29a92e53e0c75821', '0xd75a4573da215a73']
        ['0xdb4bc87225e67173', '0x12658d2690849892', '0x312a24b858370836', '0xf70027f67e5bc14f', '0xb90baac5055af515']
        ['0x477e8ea894042a8', '0x272bd1920770cd82', '0x136ab3ad920c7015', '0xf698f9cd23e34087', '0xf3be1906a68a47a2']
Current value of state: Satus end of round #20/24
        ['0xd5012dd16f116b79', '0x2c19889ec5cf62ae', '0x9461552532e4fc4e', '0xa61cde2274437ebf', '0x92500c1b790f9289']
        ['0xd5120a68d1ab78f9', '0x5efd4e7e25fb0a2a', '0xa18dea70ee7e7b1', '0xe8f94a554ba20d9e', '0x6c2371b9742b3cf9']
        ['0x18c769e56eaa99a3', '0xf7f28e95fc0f9def', '0x6ccf915de80caedf', '0xa350bbbfc57f83a1', '0x5348d2d9a6d4c15e']
        ['0xa200a1db015dda03', '0x9dfcac66829a52be', '0x5bae51decd2e0505', '0x3d7514b30bad989c', '0x52344cb5a2b2ceb2']
        ['0x541c5d9691df0b9', '0x725309a84bde7cf6', '0xad7c6fb4751afaaa', '0x2190f610e05b97f3', '0xa5136e234e9c607e']
Current value of state: Satus end of round #21/24
        ['0xde6f7a6fbf119cfc', '0xb876ded20214815d', '0x103155b3fa398a27', '0x799f3560bae1b100', '0xfc6dcf45776c2ada']
        ['0xe07cfaab5d654e34', '0x86575a2803fe29dd', '0xfd4979f71c4bf3b4', '0x95b77d3078ca5843', '0xc22d871b124cba40']
        ['0x16cc5754cfd4a65a', '0xceba73fc7920b7b4', '0xa147e2a5d0201b2b', '0x7c54a4c638f0e89d', '0xcd2c30580c56799a']
        ['0x5fd03342a8c174ae', '0xc8e9ecd5b78987fa', '0x1736c6f9c9a2b506', '0x531fad62901ce97b', '0x38b1095c7817565f']
        ['0x30dc9d6317333ad', '0x1bec5c2adb9e127a', '0x8a9f614eb924a3e4', '0x7a5d0ed8cffc11f0', '0x7c99b85823e52585']
Current value of state: Satus end of round #22/24
        ['0xbe071e1f85aebf9e', '0xcb29cd27885d83ae', '0x7a50a40f85b82714', '0xc2167c34129f900c', '0xaa77fabeb4ac8bc8']
        ['0x3d93c70a586842e5', '0x69f6b7ea035f81f9', '0x25c4b923bbc9057e', '0x6b0b8bfac267b546', '0x7903872ddfe0ea67']
        ['0xdea608f632d8a0e6', '0xa9e03575b02ac2ab', '0x1cb6db5015b15329', '0x493c3b710fc81849', '0x1cd0bc32785d87df']
        ['0x17c2dca704dabe91', '0x682092e5064766bc', '0x42705173e1d24076', '0xfbe5684038e3de9', '0x7fe942b58aed6074']
        ['0x30964188e336c8ee', '0x8f115d5261c4ca8b', '0xa6fb70ce8302bef8', '0xfd82585b31cfbde3', '0xf50b9a48989a267b']
Current value of state: Satus end of round #23/24
        ['0x237b857db12a7270', '0xfed80d96724a4af8', '0x4a6b97a5bed57019', '0x7cb90c2257d61170', '0x786c1983f16d8d7e']
        ['0xc73cad57abb53ac6', '0x4d421552aa98cead', '0x3a69c9a457cecc76', '0x5a5c8ad15c675902', '0x259bdc8000a1902d']
        ['0xfcb89c72b1957dab', '0x547e3f1f684661fa', '0x53a80ba670d835f8', '0xa409ddb6598ff113', '0x636e0f17845a3765']
        ['0x60198729c9373f7b', '0xad85a39e0489618e', '0x6d8e8abe7f35823', '0x88dffbcd2352e02a', '0xd552975f26f2d2f6']
        ['0x288de06040cf2c31', '0xab2b652f72ccd704', '0x4c27811fcca7d5c0', '0xd186f315332bcf48', '0xfab16f7ced5f2ac6']
Current value of state: Satus end of round #24/24
        ['0x40c2a59b42ba3735', '0xa280ab833f60094', '0xb2d6989b766d31b4', '0x6639b34888f969dd', '0xe8b1f2df055ea8b4']
        ['0x81986f9093118564', '0x12b4714c2910efd8', '0x38bbbc8560aa7a25', '0x17526f88335886b', '0x5120e8cdd9db5fce']
        ['0x7d3f4fe2f8ffc88e', '0x3223dd04642cdfbf', '0xd727d3faf72cf50b', '0x8850e0215b045ba8', '0x40497d5c65f3f899']
        ['0x9ba676b0b8107363', '0x83e9baf1dfb5737d', '0xded2819701405459', '0x905982c203809c7c', '0x30daafaa2cd84377']
        ['0x87e4f4797f16d7cf', '0xbd08f78abe4bc048', '0x5fdff40c167d3449', '0x1c86a97ec7cf96f7', '0x9fa332e4d48ae6dc']
Value after absorption : 3537BA429BA5C2409400F633B80A280AB4316D769B98D6B2DD69F98848B33966B4A85E05DFF2B1E864851193906F9881D8EF10294C71B412257AAA6085BCBB386B883583F8267501CE5FDBD9CDE8205
18EC8FFF8E24F3F7DBFDF2C6404DD23320BF52CF7FAD327D7A85B045B21E0508899F8F3655C7D4940637310B8B076A69B7D73B5DFF1BAE983595440019781D2DE7C9C8003C28259907743D82CAAAFDA30CFD7167F79F4E48748C04BBE8AF708BD49347D160CF4DF5FF796CFC77EA9861CDCE68AD4E432A39F
```
