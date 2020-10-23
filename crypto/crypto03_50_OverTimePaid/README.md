# CTF: All-Army Cyberstakes 2020

- Challenge: Over Time Paid 
- Category: crypto	
- Points: 50
- Difficulty: Introductory

## Instructions:

After many months of hard work by our agents, we've gained access to a sensitive payroll document from a competitor. Unfortunately, it looks heavily encrypted. [document.encrypted](https://gitlab.usna.edu/cyberopsmidncourses/sy485k/shamugia/-/blob/master/ACIctf/crypto03_50_OverTimePaid/document.encrypted) [source.py](https://gitlab.usna.edu/cyberopsmidncourses/sy485k/shamugia/-/blob/master/ACIctf/crypto03_50_OverTimePaid/source.py)

## Hints:

Isn't it strange how each line of text in their document is of an identical length?

Key Management is a difficult problem on the battlefield; maybe they reused key material in this document?

Previous documents we've recovered had lines of encrypted whitespace as a result of text-formatting in the plaintext... Maybe that applies to this document too?

## Solution:

We are given the [encrypted document](https://gitlab.usna.edu/cyberopsmidncourses/sy485k/shamugia/-/blob/master/ACIctf/crypto03_50_OverTimePaid/document.encrypted) which has been encrypted using a OTP. Since we know that OTP is irreversible without knowing any additional information we have to look for the possible mistake in implemenation. In source.py we can see that the Intro to the document says `"The following encoded individuals are to be given a $27.3k bonus"`. 

To our convenience the length of this string happens to be 64 bytes. We can use this string to find out the randomly generated string in the generate_line function.

By the mathematical properties of OTP we can xor the ciphertext with the message in order to get the random bytes used to encrypt the message.

After getting the 'random bytes' we can use the bytes to decrypt the entire message.

Here is the [solution script](https://gitlab.usna.edu/cyberopsmidncourses/sy485k/shamugia/-/blob/master/ACIctf/crypto03_50_OverTimePaid/sol.py) in python. 

## Flag
`ACI{82bd244412c4e1cf2e58a75041e}`

## Mitigation:

We have to be careful in order to correctly implement the OTP. We can not give away the information about the actual plaintext because it can lead to the loss of integrity of the entire ciphertext.
