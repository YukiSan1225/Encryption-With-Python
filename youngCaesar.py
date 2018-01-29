## This is the implementation of Caesar Cipher

def inputandEncode():
    print "You need a key to base your encryption off of. Enter a key below: "
    key = raw_input('')
    print "Enter the number of rotations:"
    rot = raw_input('')
    alphaNumerals = 'abcdefghijklmnopqrstuvwxyz'
    cipher = ''

    # Encryption
    for n in key:
        if n in alphaNumerals:
            cipher += alphaNumerals[(alphaNumerals.index(n)+int(rot)) % (len(alphaNumerals))]

    print "You're encrypted message is: " + cipher

if __name__ == '__main__':
    inputandEncode()
