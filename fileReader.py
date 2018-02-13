## Reading a file in Python for Crypto_Decoder&Encoder
## This will end up taking a minute first.
# Import Statements
import os
import future_builtins
# start of the program

# Global Variable
info = ''

def main():
    print "What is the file path with the encrypted code in your .txt file?\nYou must enter your path" \
          "with a forwardlash (/) in order for this to be read."
    i = raw_input("")

    # Error checking for dumbasses
    for symbol in i:
        if symbol == '\'':
            print "Try again."
            exit()
    # Reading the file contents
    file = open(i)
    contents = file.read()

if __name__ == '__main__':
    main()