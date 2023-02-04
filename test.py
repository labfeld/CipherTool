#!/bin/python3

import unittest
import main
import string

# TODO: Add test cases with characters (!@#$%&*(){}, etc) and numbers (0-9).

class TestCiphers(unittest.TestCase):
    def test_rot(self):
        self.assertEqual(main.rot(string.ascii_lowercase, n=13), 'nopqrstuvwxyzabcdefghijklm', 'Rot13 failed')

    
    def test_to_ascii(self):
        self.assertEqual(main.to_ascii(string.ascii_lowercase), '97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122', 'to_ascii failed.')


    def test_to_morse(self):
        self.assertEqual(main.to_morse(string.ascii_lowercase), '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..', 'to_morse failed')

    def test_to_bin(self):
        self.assertEqual(main.to_bin(string.ascii_lowercase), '01100001 01100010 01100011 01100100 01100101 01100110 01100111 01101000 01101001 01101010 01101011 01101100 01101101 01101110 01101111 01110000 01110001 01110010 01110011 01110100 01110101 01110110 01110111 01111000 01111001 01111010', 'to_bin failed')


    def test_to_hex(self):
        self.assertEqual(main.to_hex(string.ascii_lowercase), '61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a', 'to_hex failed')

    def test_reverse(self):
        self.assertEqual(main.reverse(string.ascii_lowercase), 'zyxwvutsrqponmlkjihgfedcba', 'reverse failed')


    def test_to_b64(self):
        self.assertEqual(main.to_b64(string.ascii_lowercase), 'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo=', 'to_b64 failed')
    
    
    def test_atbash(self):
        self.assertEqual(main.atbash(string.ascii_lowercase), 'zyxwvutsrqponmlkjihgfedcba', 'atbash failed')


if __name__ == '__main__':
    unittest.main()
