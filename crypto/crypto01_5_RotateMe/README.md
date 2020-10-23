# CTF: All-Army Cyberstakes 2020

- Challenge: Rotate Me    
- Category: crypto    	
- Points: 5   
- Difficulty: Introductory    

## Instructions:

Our security manager, Julius, is confident nobody can break his encryption and so left the flag for everyone to see. ciphered_flag.txt

## Hints:

Does knowing the flag format give you any information about how the flag was encrypted? 
When in Rome?   
Julius is notorious for playing games with the problem names...

## Solution

In this introductory challenge we are given a ciphertext which is said to be made by Julius the security manager. This gives us a hint that this might be a caesar cipher.

I wrote a [python script](https://gitlab.usna.edu/cyberopsmidncourses/sy485k/shamugia/-/blob/master/ACIctf/crypto01_5_RotateMe/sol.py) to decipher the caesar.

## Flag

`ACI{CrYpTo_FuN_fOr_AlL_tEWVDTnc}`

## Mitigation:

It is important to use ciphers that are strong and can not be easily broken. The legacy ciphers such as caesar should not be used in the modern times. 
