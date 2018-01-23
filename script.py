# Crypto Encoder and Decoder
# This script will take various keys/ciphers and either decode them or encode them
# User can input crypto ciphers or password or files can be read but not written to.

# Start of code
# Global Variables
from Crypto.Hash import *
from Crypto.PublicKey import *
from Crypto.Cipher import *
from twofish import TwoFish

import youngCaesar

def encode():
    print "\nWould you like to read from a file or input the text? Enter 'file' or 'text'\n"
    textR = raw_input("")
    if textR == "file":
        print "null"
    elif textR == "text":
        print "\nPlease enter the text you'd like to encode?\n"
        textR = raw_input("")
    else:
        print "You do not follow instructions. Try again.\n"
        encode()

    print "Listed below are the type of encryptions that you can obtain:"
    print "\t1. SHA256\n\t2. RSA\n\t3. AES\n\t4. Blowfish\n\t5. Twofish\n "
    print "Enter the number to define which encryption you'd like."

    numberCrypto = raw_input("")
    # Will add switch or if/else statements later
    # Encoding of SHA256
    if numberCrypto == '1':
        # Encoding of SHA256
        sha256 = SHA256.new(textR)
        print sha256.hexdigest()

    elif numberCrypto == '2':
        # Encoding of RSA
        rsaKey = RSA.generate(4096)
        pubrsaKey = RSA.importKey(rsaKey.publickey().exportKey('DER'))
        prirsaKey = RSA.importKey(rsaKey.exportKey('DER'))
        cipher = PKCS1_OAEP.new(pubrsaKey)
        ctext = cipher.encrypt(textR)

    # Encoding of AES
    elif numberCrypto == '3':
        aesKey = AES.new('This is the encrypted text.', AES.MODE_CBC)
        aesKey.encrypt(textR)

    # Encoding of Blowfish
    elif numberCrypto == '4':
        blowCip = Blowfish.new("This is the encrypted text for blowfish.",Blowfish.MODE_CTR)
        blowCip.encrypt(textR)

    # Encoding of Twofish
    elif numberCrypto == '5':
        print "A work in progress."

    # Encoding of Caesar Cipher
    elif numberCrypto == '6':
        youngCaesar.inputandEncode()

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

