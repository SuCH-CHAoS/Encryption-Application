# Encryption Toolkit

A Python-based GUI application for encrypting and decrypting text using classical cryptographic algorithms. The project combines multiple cipher techniques in a simple, user-friendly interface, making it suitable for both educational purposes and basic encryption tasks.

---

## Features

* Multiple cipher algorithms:

  * Caesar Cipher (with brute-force support)
  * Vigenère Cipher
  * Rail Fence Cipher
* Encryption and decryption modes
* Brute-force analysis for Caesar cipher
* File input and output support
* Graphical user interface built with Tkinter
* Input validation and error handling

---

## Project Structure

```
Encryption App/
│
├── main.py                 # Application entry point
│
├── ciphers/                # Cipher implementations
│   ├── caesar.py
│   ├── vigenere.py
│   └── rail_fence.py
│
├── gui/
│   └── interface.py        # GUI layout and components
│
├── utils/
│   └── file_handler.py     # File read/write utilities
│
└── __pycache__/            # Compiled files (ignored)
```

## Supported Ciphers

### Caesar Cipher

A substitution cipher that shifts characters by a fixed number of positions. Includes a brute-force mode for testing all possible shifts.

### Vigenère Cipher

A polyalphabetic cipher that uses a keyword to encrypt text, offering more complexity than Caesar.

### Rail Fence Cipher

A transposition cipher that rearranges characters in a zigzag pattern based on the number of rails.

---

## Application Workflow

1. Select a cipher method
2. Choose the operation (Encrypt, Decrypt, or Brute Force)
3. Provide the required key (shift, keyword, or number of rails)
4. Enter text or upload a file
5. View the result in the interface
6. Optionally save the output to a file

---

## Error Handling

The application validates:

* Empty inputs
* Invalid key formats
* Unsupported operations for selected ciphers

---

## Use Cases

* Learning basic cryptography concepts
* Demonstrating classical encryption techniques
* Practicing Python GUI development
* Small-scale text encryption tasks

---

## Future Improvements

* Add modern encryption algorithms (e.g., AES)
* Enhance the user interface
* Add dark mode support
* Include analysis tools (e.g., frequency analysis)

---

## Contributing

Contributions are welcome. You can fork the repository, create a branch, and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by [SuCH CHAoS]
