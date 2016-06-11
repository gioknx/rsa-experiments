#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Para executar, faça:
    python encrypt.py
"""

import random
import sys

def rand_prime(n):
    """
        Retorna um primo aleatório > n.

        Teste de primalidade tenta todos os números ímpares entre 3 e sqrt(p)
        onde p é o candidato a primo.
    """
    n = n+1 if n % 2 == 0 else n
    while True:
        p = random.randrange(n, 2*n, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p

def mdc(a, b):
    """
        Dado a e b, calcula x, y e mdc(a, b) tal que a*x + b*y = mdc(a, b).

        Quando mdc(a, b) = 1, x é o inverso de a mod b.
    """
    r, r_ = b, a
    x, x_ = 0, 1
    y, y_ = 1, 0
    while r != 0:
        q = r_ // r
        r_, r = r, r_ - q * r
        x_, x = x, x_ - q * x
        y_, y = y, y_ - q * y
    if a < 0:
        x_ = -x_
    if b < 0:
        y_ = -y_
    return r_, x_, y_

def generate_keypair():
    """
        Retorna n, e, d. Chave pública e privada para RSA.
    """
    p, q = rand_prime(16), rand_prime(16)
    phi_n = (p-1)*(q-1)

    while True:
        e = random.randint(3, phi_n-1)
        if mdc(e, phi_n)[0] == 1:
            break

    d = mdc(e, phi_n)[1]
    if d < 0:
        d += phi_n
    return p*q, e, d

def encrypt(plaintext, n, e):
    """
        Para cada byte do texto codificado em UTF-8, calcula byte^e mod n.
        Retorna o texto criptografado como uma lista de números.
    """
    return [pow(ord(byte), e, n) for byte in plaintext.encode('utf-8')]

if __name__ == "__main__":
    n, e, d = generate_keypair()
    print("chave pública = (n = {}, e = {})".format(n, e))
    print("chave privada = (n = {}, d = {})".format(n, d))

    encoding = "utf-8" if sys.stdin.encoding in (None, "ascii") else sys.stdin.encoding
    plaintext = raw_input("mensagem: ").decode(encoding)
    print("cifra: " + repr(encrypt(plaintext, n, e)))
