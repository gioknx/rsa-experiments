#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Para executar, faça:
    python decrypt.py

Digite a chave privada e a cifra no mesmo formato que são dadas pelo programa
encrypt.py.
"""

privkey = eval("dict" + raw_input("chave privada: "))
n = privkey["n"]
d = privkey["d"]
ciphertext = eval(raw_input("cifra: "))

# texto = cifra^d mod n
plaintext = bytearray(pow(byte, d, n) for byte in ciphertext)
print(u"mensagem: {}".format(plaintext.decode("utf-8")))
