#!/usr/bin/env python3

cipher = "IKQ{KzGxBw_NcV_nWz_ItT_bMEDLBvk}"
decipher = ""
s=0

while (s<27):
    for i in cipher:
        if (i.isalpha()):
            if (i.isupper()):
                decipher+= chr((ord(i)+s-65)%26+65)
            elif (i.islower()):
                decipher+= chr((ord(i)+s-97)%26+97)
        elif (i=='{'):
            decipher+='{'
        elif (i=='_'):
            decipher+='_'
        elif (i=='}'):
            decipher+='}'
        
    print(decipher+'\n')
    decipher=''
    s+=1


