import os
import hashlib
print("\u001b[32m#################################################################################################################")
print("#                                                                                                    \u001b[31m    v 1.3  #") 
print("# \u001b[32m██╗  ██╗ █████╗ ██████╗ ██╗  ██╗   ██████╗ ███████╗███╗  ██╗███████╗██████╗ █████╗  ████████╗ █████╗ ██████╗  #")
print("# \u001b[32m██║  ██║██╔══██╗██╔════╝██║  ██║  ██╔════╝ ██╔════╝████╗ ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗ #")
print("# \u001b[32m███████║███████║╚█████╗ ███████║  ██║  ██╗ █████╗  ██╔██╗██║█████╗  ██████╔╝███████║   ██║   ██║  ██║██████╔╝ #")
print("# \u001b[32m██╔══██║██╔══██║ ╚═══██╗██╔══██║  ██║  ╚██╗██╔══╝  ██║╚████║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║  ██║██╔══██╗ #")
print("# \u001b[32m██║  ██║██║  ██║██████╔╝██║  ██║  ╚██████╔╝███████╗██║ ╚███║███████╗██║  ██║██║  ██║   ██║   ╚█████╔╝██║  ██║ #")
print("# \u001b[32m╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚════╝ ╚═╝  ╚═╝ #")
print("#                                                                                \u001b[31mHash Generator By @AvShivaNoro #")
print("# \u001b[32m                                                                                                              #")                                                                                                                                                                                                                  
print("\u001b[32m#################################################################################################################")
print("")
print("\u001b[37mif you want to know what all hash's are there just type help or ? ")
print("")
while True:
    wright = input("What hash Type do you want to Generate: ")
    if wright =="sha512":
        mystring = input('Enter string to hash: ')
        hash_obj = hashlib.sha512(mystring.encode())
        print(hash_obj.hexdigest())
    elif wright =="md5":
        mystring = input('Enter string to hash: ')
        hash_obj = hashlib.md5(mystring.encode())
        print(hash_obj.hexdigest())
    elif wright =="md4":
        mystring = input('Enter string to hash: ')
        hash_obj = hashlib.sha512(mystring.encode())
        print(hash_obj.hexdigest())
    elif wright =="bcrypt":
        import bcrypt
        mystring = input("Enter string to hash: ")
        password = mystring.encode("utf-8")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        print(hashed)
    elif wright =="sha256":
        mystring = input('Enter string to hash: ')
        hash_obj = hashlib.sha256(mystring.encode())
        print(hash_obj.hexdigest())
    elif wright =="sha384":
        mystring = input('Enter string to hash: ')
        hash_obj = hashlib.sha384(mystring.encode())
        print(hash_obj.hexdigest())
    elif wright =="sha224":
        mystring = input('Enter string to hash: ')
        hash_obj = hashlib.sha224(mystring.encode())
        print(hash_obj.hexdigest())
    elif wright =="sha1":
        mystring = input('Enter string to hash: ')
        hash_obj = hashlib.sha1(mystring.encode())
        print(hash_obj.hexdigest()) 
    elif wright =="base64":
        import base64
        mystring = input("Enter string to base64: ")
        message = mystring
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        print(base64_message)
    elif wright =="help":
        print("We Have All The Hash's Given Down Below ↓↓")
        print("##############################")
        print("##########")
        print("# base64 #")
        print("##########")
        print("#  sha1  #")
        print("##########")
        print("# sha224 #")
        print("##########")
        print("# sha384 #")
        print("##########")
        print("# sha256 #")
        print("##########")
        print("# bcrypt #")
        print("##########")
        print("#  md4   #")
        print("##########")
        print("#  md5   #")
        print("##########")
        print("# sha512 #")
        print("##########")
        print("##############################")
        print("type exit to close the Script")
    elif wright =="?":
        print("We Have All The Hash's Given Down Below ↓↓")
        print("##############################")
        print("##########")
        print("# base64 #")
        print("##########")
        print("#  sha1  #")
        print("##########")
        print("# sha224 #")
        print("##########")
        print("# sha384 #")
        print("##########")
        print("# sha256 #")
        print("##########")
        print("# bcrypt #")
        print("##########")
        print("#  md4   #")
        print("##########")
        print("#  md5   #")
        print("##########")
        print("# sha512 #")
        print("##########")
        print("type exit to close the Script")
        print("##############################")
    elif wright =="youtube":
        print("Ok Fine Subscribe To My Channel AVSHIVA NORO")
    elif wright =="exit":
        print("Ok Bye | Thanks For Using The Script")
        exit()
           
    else:
        print("Sorry we do not support the hash algorithm "  + wright + "")
else:
    print(" ok cool ")
            







