#!/usr/bin/env python

import string
import random
from Crypto.PublicKey import RSA
from Crypto import Random

def detect_alg(rsa_bits, aes_bits):
    alg = None
    if rsa_bits:
        alg = "Rsa"
    elif aes_bits:
        alg = "Aes"
    return alg



def rand_aes(bits):
    chars = string.letters + string.digits + string.punctuation
    return "".join([random.choice(chars) for c in xrange(bits)])



def rand_rsa(bits):
    random_generator = Random.new().read
    key = RSA.generate(int(bits), random_generator)
    return key



def end(alg, bits):
    if alg == "Aes":
        alg = alg.upper() + "-" + bits + " "
    elif alg == "Rsa":
        if bits == "512":
            alg = alg.upper() + "-" + bits + " "
        elif bits == "1024":
            alg = alg.upper() + "-" + bits
    print('\n' + "\n I am generating your key for " + alg.lower() + "\n\n" +
          " _______________________________________________\n" +
          "/                                               \\\n" +
          "|  ___________________________________________  |\n" +
          "| |                                           | |\n" +
          "| |                                           | |\n" +
          "| | C:\ > Generating Key...                   | |\n" +
          "| |                                           | |\n" +
          "| |                                           | |\n" +
          "| |                                           | |\n" +
          "| | Algorithm: " + alg + "                       | |\n" +
          "| |                                           | |\n" +
          "| |                                           | |\n" +
          "| |                                           | |\n" +
          "| | Stay encrypted LOL                        | |\n" +
          "| |                                           | |\n" +
          "| |                                           | |\n" +
          "| |                                           | |\n" +
          "| |___________________________________________| |\n" +
          "\_______________________________________________/\n" +
          "   \________________________________________/")



def info(alg, key):
    if alg == "Aes":
        print("\n\nAES Key: " + key)
        print('')
    elif alg == "Rsa":
        print('\n')
        print(key.publickey().exportKey('PEM'))
        print('')
        print(key.exportKey('PEM'))
        print('')



def main(rsa_bits, aes_bits):
    alg = detect_alg(rsa_bits, aes_bits)
    if alg == "Aes":
        aes_key = rand_aes(int(aes_bits)/8)
        end(alg, aes_bits)
        info(alg, aes_key)
    elif alg == "Rsa":
        rsa_key = rand_rsa(rsa_bits)
        end(alg, rsa_bits)
        info(alg, rsa_key)
