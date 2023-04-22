#I want to keep things safe and secure. One way to do that is by creating a special code called a "hash" that takes information and turns it into a secret code. It's like a secret decoder ring that only I know how to use. The SHA256 Python program I'm creating helps me make these secret codes. These codes are special because they are unique to each piece of information, like a fingerprint. If someone tries to change or take the information, the secret code will be different and I'll know something is wrong. It's like a secret guard that watches over our important things to make sure they stay safe!


import hashlib
#This line imports the hashlib library which provides hash functions, one of them being SHA-256 which is what we're using here.

message = input("Enter a message to hash: ")
#This line commands the user to enter a message to be hashed, and gathers that input into the message variable.

hash_object = hashlib.sha256(message.encode())
#This line creates the hash using the SHA-256 algorithm provided by the hashlib library imported above. The message variable is encoded using the 'encode()' method, which is necessary for the SHA256 encryption standard.

hex_dig = hash_object.hexdigest()
#This line gets the hexadecimal of the hash value created by the SHA256 standard and stores it in the 'hex_dig' variable.

print("Hash value:", hex_dig)
#This line prints the hash value of the message that was given by the user. The 'hex_dig' variable is concatenated with the "Hash value" string using a comma in the print function, which then shows the hash value and the message.