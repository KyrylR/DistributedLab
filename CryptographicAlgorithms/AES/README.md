# AES encryption 

The AES encryption algorithm defines multiple transformations that are performed on data stored in an array. 
AES involves operating on an array of 4×4 bytes, which is called a state (in the simplest case).

![image](https://user-images.githubusercontent.com/89979281/174750846-0f2ae5ef-296d-4c39-a3af-1d9d328a173e.png)
Figure 1.1 - Schematic diagram of AES workflow

### Pseudo-code for Encrypt

```
function Encrypt(plaintext, key) {      
    blocks := DivideIntoBlocks(plaintext);   
    roundKeys = GetRoundKeys(key)   

    for (block in blocks) {            
        //first round
        AddRoundKey(roundKeys[0], block);            
        //intermediate rounds     
        for (8, 10 or 12 rounds) {          
            SubBytes(block);       
            ShiftRows(block);           
            MixColumns(block);       
            AddRoundKey(roundKeys[..], block);     
        }            
        //last round     
        SubBytes(block);     
        ShiftRows(block);     
        AddRoundKey(roundKeys[numRounds - 1], block);   
    }   
    ciphertext := Reassemble(blocks);   
    return ciphertext; 
}
```

1. The DivideIntoBlocks function must divide the input text into blocks of 128 bits (16 bytes). 
   Each block is represented as a 4x4 matrix (example in the following figure).

   ![image](https://user-images.githubusercontent.com/89979281/174750983-511b393a-c27f-46f0-b137-3154fd3ed623.png)
   Figure 1.2 - Example of a block of initial message to be encrypted

2. The GetRoundKeys function performs key expansion. Since AES assumes a key length of 128 bits (in the simplest case), 
   this means that a key sequence equal to the length of the message to be encrypted must be generated for longer data. 
   This is what the deployment function is used for (a separate 128-bit encryption key is generated 
   for each block to be encrypted).


### Pseudo-code for GetRoundKeys

```
function GetRoundKeys(byte key[4*Nk], word w[Nb*(Nr+1)], Nk) { 
   begin 
      word temp 
      i = 0 
      
      while (i < Nk) 
         w[i] = word(key[4*i], key[4*i+1], key[4*i+2], key[4*i+3]) 
         i = i+1 
      end while 
      
      i = Nk 
      
      while (i < Nb * (Nr+1)] 
         temp = w[i-1] 
         if (imod Nk = 0) 
            temp = SubWord(RotWord(temp)) xor Rcon[i/Nk] 
         else if (Nk > 6 and i mod Nk = 4) 
            temp = SubWord(temp) 
         end if
      w[i] = w[i-Nk] xor temp 
      i = i + 1 
      end while 
   end 
} 
```

3. The AddRoundKey function performs addition of a block with a RoundKey key (XOR (⊕) operation). 
4. The SubBytes function is required to perform substitution: each byte in the block is replaced by 
the corresponding element in the fixed table (S-box).

![image](https://user-images.githubusercontent.com/89979281/174751134-2a263588-bccf-47e5-910d-6605a095acba.png)
Figure 1.3 - Substitution table

5. The ShiftRows function cyclically shifts the bytes in each row of the block by r bytes to the left, 
depending on the row number.

![image](https://user-images.githubusercontent.com/89979281/174751166-a04e8916-ddb8-4c15-82b2-47acd20b058f.png)
Figure 1.4 - Block line shift diagram

6. The MixColumns function consists of multiplying each column of a block with a constant matrix as follows:

![image](https://user-images.githubusercontent.com/89979281/174751203-8c4f2e15-7f39-4bd6-9678-219d9dd17d49.png)
Figure 1.5 - MixColumns operation

## Decryption takes place according to the following algorithm

### Pseudo-code for InvCipher  

```
function InvCipher(byte in[4*Nb], byte out[4*Nb], word w[Nb*(Nr+1)]) 
   begin 
      byte state[4,Nb] 
      state = in

      AddRoundKey(state, w[Nr*Nb, (Nr+1)*Nb-1])  
      
      for round = Nr-1 step -1 downto 1 
         InvShiftRows(state)  
         InvSubBytes(state)
         AddRoundKey(state, w[round*Nb, (round+1)*Nb-1]) 
         InvMixColumns(state) // See Sec. 5.3.3 
      end for 
      
      InvShiftRows(state)
      InvSubBytes(state) 
      AddRoundKey(state, w[0, Nb-1])  
      out = state 
   end
```
 
The functions InvShiftRows, InvSubBytes and InvMixColumns are inverse - i.e. 
they perform inverse operations (4-6).

[The standard itself and test vectors](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)

