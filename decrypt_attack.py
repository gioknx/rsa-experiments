#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Para executar, faça:
    python decrypt_attack.py

Digite a chave privada e a cifra no mesmo formato que são dadas pelo programa
encrypt.py.

Esse programa implementa um ataque do tipo chosen-ciphertext (CCA1):
    https://en.wikipedia.org/wiki/Chosen-ciphertext_attack

Note que em hora alguma a chave privada é usada para descriptografar a entrada
original.
"""

pubkey = eval("dict" + raw_input("chave pública: "))
n = pubkey["n"]
e = pubkey["e"]
privkey = eval("dict" + raw_input("chave privada: "))
d = privkey["d"]

ciphertext = eval(raw_input("cifra: "))

# C = cifra
# P = texto

# C' = C * 2^e
ciphertextPrime = [(byte * pow(2, e, n)) % n for byte in ciphertext]
print("cifra * 2^e (mod n): {}".format(repr(ciphertextPrime)))

# P' = C'^d = (P^e*2^e)^d = P*2
plaintextPrime = [pow(byte, d, n) for byte in ciphertextPrime]
print(u"mensagem: {}".format(repr(plaintextPrime)))

# P = P'/2
plaintext = bytearray(x//2 for x in plaintextPrime)
print(u"mensagem / 2: {}".format(plaintext.decode("utf-8")))
