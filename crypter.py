def pwd(string, key):
    key = list(key) 
    for i in range(len(key)):
        x = (ord(key[i]) + 200)
        key[i] = chr(x)
        
    if len(string) == len(key):
        return(key) 
    elif len(string) > len(key):
        for i in range(len(string) -len(key)):
            key.append(key[i % len(key)])
        return("" . join(key)) 
    elif len(string) < len(key):
        key = key[:len(string)]
        return("" . join(key))
    
def encrypt(string,password):
    string = string + " "
    key = pwd(string, password)
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +ord(key[i]) + 1000)
        encrypt_text.append(chr(x))
    encrypt_text = ("" . join(encrypt_text))
    key = ("".join(key))
    return encrypt_text + key

def decrypt(encrypt_text):
    orig_text = []
    b = int(len(encrypt_text)/2)
    key = encrypt_text[b:]
    encrypt_text = encrypt_text[:b-1]
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) -ord(key[i]) - 1000)
        orig_text.append(chr(x))
    orig_text = ("" . join(orig_text))
    return orig_text
