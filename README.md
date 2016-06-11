Implementação simples de RSA em Python e um ataque CCA1.

##### Exemplo de execução:

![Gravação de um terminal executando o programa. O texto está transcrito abaixo.](https://i.imgur.com/rtFHqXR.gif)

    $ python encrypt.py
    chave pública = (n = 899, e = 137)
    chave privada = (n = 899, d = 233)
    mensagem: Álgebra A!
    cifra: [670, 149, 612, 286, 746, 831, 830, 636, 652, 487, 469]
    $ python decrypt.py
    chave privada: (n = 899, d = 233)
    cifra: [670, 149, 612, 286, 746, 831, 830, 636, 652, 487, 469]
    mensagem: Álgebra A!
    $ python decrypt_attack.py
    chave pública: (n = 899, e = 137)
    chave privada: (n = 899, d = 233)
    cifra: [670, 149, 612, 286, 746, 831, 830, 636, 652, 487, 469]
    cifra * 2^e (mod n): [758, 131, 526, 710, 318, 441, 778, 529, 531, 398, 171]
    mensagem: [390, 258, 216, 206, 202, 196, 228, 194, 64, 130, 66]
    mensagem / 2: Álgebra A!
