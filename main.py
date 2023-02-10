#!/bin/python3

# TODO: Make more cipher methods
# TODO: Make it so there are different "difficulties" of ciphers? 
# TODO: Make it so that there aren't so many "confusing" symbols generated in the flags?

import random
import base64
import string
import argparse
import time


def rot(s, n=13):
    lookup = dict(zip(string.ascii_lowercase+string.ascii_uppercase,''.join([string.ascii_lowercase[n:], string.ascii_lowercase[:n], string.ascii_uppercase[n:], string.ascii_uppercase[:n]])))
    return ''.join([lookup[c] if c in lookup.keys() else c for c in s]) 

def to_ascii(s):
    return ' '.join([str(ord(c)) for c in s])

def to_morse(s):
    lookup = {'a':'.-',
              'b':'-...',
              'c':'-.-.',
              'd':'-..',
              'e':'.',
              'f':'..-.',
              'g':'--.',
              'h':'....',
              'i':'..',
              'j':'.---',
              'k':'-.-',
              'l':'.-..',
              'm':'--',
              'n':'-.',
              'o':'---',
              'p':'.--.',
              'q':'--.-',
              'r':'.-.',
              's':'...',
              't':'-',
              'u':'..-',
              'v':'...-',
              'w':'.--',
              'x':'-..-',
              'y':'-.--',
              'z':'--..',
              '1':'.----',
              '2':'..---',
              '3':'...--',
              '4':'....-',
              '5':'.....',
              '6':'-....',
              '7':'--...',
              '8':'---..',
              '9':'----.',
              '0':'-----',
              '.':'.-.-.-',
              ',':'--..--',
              '?':'..--..',
              '\'':'----.',
              '!':'-.-.--',
              '/':'-..-.',
              '(':'-.--.',
              ')':'-.--.-',
              '&':'.-...',
              ':':'---...',
              ';':'-.-.-.',
              '=':'-...-',
              '+':'.-.-.',
              '-':'-....-',
              '"':'.-..-.',
              '$':'...-..-',
              '@':'.--.-.',
              ' ':';'}
    return ' '.join([lookup[c] if c in lookup.keys() else c for c in s.lower()])

def to_bin(s):
    # Note, the `rjust()` is to pad out bits, because cyberchef struggles to decode variable length ie numbers ar e 6 bit, and letters 7.
    return ' '.join([bin(ord(c)).replace('0b','').rjust(8,'0') for c in s])

def to_hex(s):
    return ' '.join([hex(ord(c)).replace('0x','') for c in s])

def reverse(s):
    return s[::-1]

def to_b64(s):
    # Note, the `.decode()` at the end is needed to convert the bytes object back to a str. The `.encode()` on the string is used to make it a bytes object for b64.
    return base64.b64encode(s.encode()).decode()

def atbash(s):
    lookup = dict(zip(string.ascii_lowercase+string.ascii_uppercase,string.ascii_lowercase[::-1]+string.ascii_uppercase[::-1]))
    return ''.join([lookup[c] if c in lookup.keys() else c for c in s])


METHODS_REQUIRE_CASE = [to_b64]
METHODS_CASE_SAFE = [rot, to_ascii, to_bin, to_hex, reverse, atbash]
METHODS_CASE_UNSAFE = [to_morse]


def main():
    # Debug
    DEBUG_LOG_CIPHER_HISTORY = False
    
    # Parse any command line arguments
    parser = argparse.ArgumentParser(description='Generate random ciphers')
    parser.add_argument('-o', '--outfile', nargs='?', type=argparse.FileType('w'), help='output file. Will output to console if omitted.')
    parser.add_argument('-m','--min', type=int, default=1, help='minimum number of ciphers to apply.')
    parser.add_argument('-M','--max', type=int, default=3, help='maximum number of ciphers to apply.')
    parser.add_argument('-f','--flag', type=str, default=None, help='the flag to be ciphered. Will generate one in the format "flag{xxxxxxxxxxxxxxxx}" if omitted')
    parser.add_argument('-i','--input', action='store_true', help='make the script wait with an input box for you to verify the flag.')
    args = parser.parse_args()
    
    MIN_STEPS = args.min
    MAX_STEPS = args.max 

    methods_to_use = METHODS_CASE_SAFE
    methods_to_use.extend(METHODS_CASE_UNSAFE)
    methods_to_use.extend(METHODS_REQUIRE_CASE)

    
    if args.flag == None:
        raw_text = 'flag{' + ''.join([random.choice(string.ascii_letters + string.digits + '!@#$%^&*-_=+') for _ in range(16)]) + '}'
    else:
        raw_text = args.flag
    cipher_text = raw_text

    cipher_history = []
    for i in range(random.randint(MIN_STEPS,MAX_STEPS)):
        methods = methods_to_use 
        m = random.choice(methods)
        if m in METHODS_REQUIRE_CASE:
            # If there has been a cipher that requires case to be preserved, it will remove ciphers that do not preserve case, otherwise the message can become unrecoverable.
            # Note: This is slow; it only needs to remove case unsafe methods once, and not check again.
            for unsafe_method in METHODS_CASE_UNSAFE:
                if unsafe_method in methods_to_use:
                    methods_to_use.remove(unsafe_method)
        if DEBUG_LOG_CIPHER_HISTORY:
            print(f'Step:{can_do_case_unsafe_cipher} {i} - "{s}"')
            print(f'Applying {m}')
            print(f'methods = {methods}')
        cipher_text = m(cipher_text)
        cipher_history.append(m.__name__)

    # The output is both the recipe used to create the cipher (encoded in base64), and the cipher_text.
    output = f'Recipe (base64):\n{base64.b64encode(" ".join(cipher_history).encode()).decode()}\nCipher:\n{cipher_text}\n'
    if args.outfile == None:
        print(output)
    else:
        with args.outfile as f:
            f.write(output)
            f.close()
    if args.input:
        start_time = time.time()
        while input('Enter the flag: ') != raw_text:
            print('Incorrect flag.')
        print(f'Correct flag. It took you {round(time.time()-start_time, 3)} seconds to solve it.')

if __name__ == '__main__':
    main()
