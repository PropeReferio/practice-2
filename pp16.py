# Write a password generator in Python. Be creative with how you generate passwords
#  - strong passwords have a mix of lowercase letters, uppercase letters, numbers, 
# and symbols. The passwords should be random, generating a new password every time 
# the user asks for a new password. Include your run-time code in a main method.
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-.,;?'
ranpass = ''.join([chars[random.randint(0, len(chars) - 1)] for _ in range(0, random.randint(11,17))])
                       #selects a char at random                           #Repeats random selection at least 10 times, up to 16 times
                       
# ranpass = ''
# for _ in range(random.randint(10,17)):
#     ranpass += chars[random.randint(0, end - 1)]

print(ranpass)