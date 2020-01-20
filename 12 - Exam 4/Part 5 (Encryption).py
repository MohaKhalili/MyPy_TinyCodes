# Encryption problem: You and your friend want to encrypt your messages and you have
# shared a secret key that is known to just the two of you. Every character in the 
# character_set is mapped to some other character in the secret key. For example 'a'
# is mapped to 'D', 'b' is mapped to 'd', 'c' is mapped to '1' and so forth as shown below:

# character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
# secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"

# Write a function named my_encryption that accepts a string (a message which will only
# consist of the characters from the character set) as function parameter and encrypts 
# that message using the secret_key and returns it. 
# 
# For example if input to this function (the message that you want to send) is:
# "Lets meet at the usual place at 9 am"
# Then your function should should return the encrypted message:
# "oABjMWAABMDBMB2AMvjvDPMYPD1AMDBMGMDW" 

# Note that capitalization does matter here!

# Type your code here
def my_encryption(some_string):

    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"