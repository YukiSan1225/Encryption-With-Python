# Crypto Encoder and Decoder
# This script will take various keys/ciphers and either decode them or encode them
# User can input crypto ciphers or password or files can be read but not written to.

from base64 import b64encode
# Start of code
# Global Variables
from hashlib import md5

from Crypto.Cipher import *
from Crypto.Hash import *

# from twofish import TwoFish
import CaesarCipher, fileReader, AffineCipher
from fileReader import main

def encode():
    print "\nWould you like to read from a file or input the text? Enter 'file' or 'text'\n"
    textR = raw_input("")
    # Reading the file
    if textR == "file":
        fileReader.main()
        textR = fileReader.info
    # Inputting text into program
    elif textR == "text":
        print "\nPlease enter the text you'd like to encode?\n"
        textR = raw_input("")

    # Error control
    else:
        print "You do not follow instructions. Try again.\n"
        encode()

    print "Listed below are the type of encryptions that you can obtain:"
    print "\t1. SHA256\n\t2. Affine\n\t3. AES\n\t4. Caesar Cipher"
    print "Enter the number to define which encryption you'd like."

    numberCrypto = raw_input("")

    # Encoding of SHA256
    if numberCrypto == '1':
        # Encoding of SHA256
        sha256 = SHA256.new(textR)
        print sha256.hexdigest()
        exit()

    elif numberCrypto == '2':
        # Encoding of Affine Cipher
        exit()
    # Encoding of AES; Will redo the coding base
    elif numberCrypto == '3':
        #Lambda Function
        BLOCK_SIZE = 32
        pad = lambda p: p + (BLOCK_SIZE - len(p) % BLOCK_SIZE) * \
            chr(BLOCK_SIZE - len(p) % BLOCK_SIZE)

        #MD5 Encryption for AES Key
        textR = md5(textR.encode('utf8')).hexdigest()

        enc = pad(textR)
        cipher = AES.new(textR, AES.MODE_ECB)
        print b64encode(cipher.encrypt(enc))
        exit()

    # Encoding of Caesar Cipher
    elif numberCrypto == '4':
        CaesarCipher.inputandEncode()
        exit()

def decode():
    print "Work in progress"

def main():
    print "\nCrypto Decoder and Encoder. (C) Damien Burks 2018"
    print "Before we get started, would you like to encode or decode?"
    choice = raw_input("")

    if choice == "encode":
        encode()
    elif choice == "decode":
        decode()
    else:
        print "I'm sorry, I didn't get that. Please try again."
        main()

if __name__ == '__main__':
    main()

