# CTF: All-Army Cyberstakes 2020
- Challenge: Speak Plainly 
- Category: crypto	
- Points: 150
- Difficulty: Intermediate


## Instructions:

There's something suspicious about how account logins happen on this server... ? http://challenge.acictf.com:2338

## Hints:

Your username and the secret strongtoken are the only components of the encrypted cookieHow does the length of your username effect the length of the cookie?It is possible to guess strongtoken one byte-at-a-time because of how AES-ECB worksThe strongtoken itself does not contain any ';' characters

## Solution:

After lookig at the website cookies at some time I noticed that there were several factors that affected the auth_token. 

One of them was the length of the username

AAA -->     
bbed2c2bc459d5cda5690e770a719a2d2d3a066274a44b7b72fc8367c6da458f

AAAAAAAAAAAAAAA -->     
281beef26003b790747867396687dae569b71623a660162cb077263050e87cb8

AAAAAAAAAAAAAAAA -->     
6196e0d7ab95361845891cf1c4c1f91b6b2063ba256e2245f3552fb5d3464c06e4d96dded33a761e1e05720c2fd78f98

32 As -->       
6196e0d7ab95361845891cf1c4c1f91b6196e0d7ab95361845891cf1c4c1f91b6b2063ba256e2245f3552fb5d3464c06e4d96dded33a761e1e05720c2fd78f98

We can see that after entering a username longer than 15 characters the lenght of the token increases. 

The hints also tell us that this might have to do something with AES-ECB encrytption, which is known to be not very strong.

In the hints section we are also told that the username and the secret token are the only components of the encrypted cookie.

I used the following method for guessing the secret token https://zachgrace.com/posts/attacking-ecb/  

This is [my solution attempt](sol.py). 

I recieved a token of 16 characters, however it was not correct and did not recieve the flag. 


## Flag:

Not Completed

## Mitigation:

AES ECB is not a safe from of encryption. In AES ECB each block of plaintext is encrypted independently with the key therefore identical blocks of plaintext will result in identical ciphertext blocks 
