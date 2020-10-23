# CTF: All-Army Cyberstakes 2020

- Challenge: Headpiece Silver 
- Category: crypto	
- Points: 200
- Difficulty: Introductory/Intermediate

## Instructions:

Can you break our unbreakable crypto? [challenge.acictf.com:51303](challenge.acictf.com:51303)

## Hints:

How large is the N that you receieved?

The password is alphanumerictelnet is known to interact poorly with the challenge instance. 

We recommend using 'netcat' to connect to the challenge.

## Solution:

In this challenge we are given a url and a port number and we are adviced to connect using 'netcat'.

When we are connected to the challenge we get the following menu options

1. Print public key
2. Get password ciphertext
3. Enter password
4. Test ciphertext
5. Exit

If we ask to Print Public key (option 1) we get the following output:

```
Here is our public key information
N: 122298190177919866881639090045815514691491489519639425496178483984084352945237
e: 65537
```

Next I asked for the password ciphertext (option 2)

```
If you can decrypt the password you will get a reward.
1a7627ccc36d251fb9276fb3d312807409e6a486ba2cbbd94d4e35d74dc29dda
```

Test ciphertext option (option 4) decrypts the given ciphertext.
I tested out what our ciphertext would decrypt to and got the following decrypted hex number:

```
Please send in a ciphertext as a hex string:
1a7627ccc36d251fb9276fb3d312807409e6a486ba2cbbd94d4e35d74dc29dda
Your ciphertext decrypted to:
3464536d394c57685951784962466a58
```

Lets See what ASCII characters this hex string corresponds to:

```
>>> hexStr="3464536d394c57685951784962466a58"
>>> bytes_object = bytes.fromhex(hexStr)
>>> ascii_String = bytes_object.decode("ASCII")
>>> ascii_String
'4dSm9LWhYQxIbFjX'
```

Maybe this is the password???
We can test it out using the option 3 (Enter Password)

```
Please enter password:
4dSm9LWhYQxIbFjX
You beat our crypto, here is your reward!
ACI{2297322356781f628e90b7336d6}
```

And here is our flag!


## Flag

`ACI{2297322356781f628e90b7336d6}`



