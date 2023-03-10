# CipherTool 

This is a tool to practice using [CyberChef](https://gchq.github.io/CyberChef).

Currently it suppports a few ciphers:
- Rot13
- Ascii encoding
- Morse code
- Binary encoding
- Hexadecimal encoding
- Reversing the text
- Base64 encoding
- Atbash

- - -
## Usage

The simpliest way is to run `./main.py` in your terminal.

By default, it uses 1-3 ciphers. To change the numbers, use `--min <X>`, `--max <Y>` to set the minimum number of ciphers to `<X>`, and the maximum to `<Y>.

By default, it will generate a flag in the form `flag{xxxxxxxxxxxxxxxx}`, use `--flag <text>` to specify a custom flag.

By default this will output to the terminal. To output to a file, use `--outfile <file_name>`.

It outputs both the ciphertext, and the recipe used to generate it. It encodes the recipe in Base64, so you do not have to worry about accidentally seeing it.

Currently there are a few unittests to verify the ciphers are working as intended. However, they are not very extensive.

- - -

## TODO:
- Add more ciphers.
- Make it smarter about what ciphers can be used after other ciphers; it shouldn't do back-to-back reverses.

- - -

If you encounter any bugs or issues, please let me know or submit a pull request to fix it.

Feel free to create pull requests to improve this tool/add more ciphers.

