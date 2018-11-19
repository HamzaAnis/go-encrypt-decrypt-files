#!/usr/bin/env python

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

def key_string():
    key = raw_input("\n=> ")
    while len(key) != 512 and len(key) != 1024:
        key = raw_input("=> ")
    return key



def choose_alg():
    alg_mode = None
    while alg_mode != '1' and alg_mode != '2':
        alg_mode = raw_input("\n=> ")
    if alg_mode == '1':
        alg_mode = "Encrypt"
    elif alg_mode == '2':
        alg_mode = "Decrypt"
    return alg_mode



def rsa_encrypt(public_key,message):
    encrypted = public_key.encrypt(message, 32)
    return encrypted

def rsa_decrypt(key,encrypted):
    decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
    return decrypted



def info(file_mode, end_alg, key):
    print('\n' +
          "        .-\"\"-.                                          \n" +
          "       / .--. \                                           \n" +
          "      / /    \ \       " + file_mode + " " + end_alg +
          "\n      | |    | |                                        \n" +
          "      | |.-\"\"-.|       Algorithm: RSA-" + str(len(key) * 8) +
          "\n     ///`.::::.`\                                       \n" +
          "    ||| ::/  \:: ;     Key: " + key +
          "\n    ||; ::\__/:: ;                                      \n" +
          "     \\\\\ '::::' /                                       \n" +
          "      `=':-..-'`                                            ")



def end(file_mode, output_text):
    if file_mode == "Text":
        print("\nOutput " + file_mode + ": \n" + output_text + '\n')




def main(opt_text):
    print("\nInsert key (512 or 1024 bits)")
    key = key_string()
    text = opt_text
    print("\nWhat do you want to do?")
    print("[1] Encrypt    [2] Decrypt      (select 1 or 2)")
    alg_mode = choose_alg()
    if alg_mode == "Encrypt":
        try:
            output_text = rsa_encrypt(key, text)
            info("Text", alg_mode + "ed", key)
            end("Text", None, output_text)
        except:
            print("This text is not valid for encryption")
    if alg_mode == "Decrypt":
        try:
            output_text = rsa_decrypt(key, text)
            info("Text", alg_mode + "ed", key)
            end("Text", None, output_text)
        except:
            print("This text is not valid for decryption")
