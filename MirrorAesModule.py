#!/usr/bin/env python
# coding=utf-8

import base64
import os.path
from Crypto import Random
from Crypto.Cipher import AES



def file_modes(opt_file, opt_folder, opt_text):
    file_mode = None
    string = None
    if opt_file:
        file_mode = "File"
        string = opt_file
    elif opt_folder:
        file_mode = "Folder"
        string = opt_folder
    elif opt_text:
        file_mode = "Text"
        string = opt_text
    return file_mode, string



def key_string():
    key = raw_input("\n=> ")
    while len(key) != 16 and len(key) != 24 and len(key) != 32:
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



def choose_path(file_mode, path):
    output_path = None
    while output_path != '1' and output_path != '2':
        output_path = raw_input("\n=> ")
    if output_path == '1':
        output_path = path
    elif output_path == '2':
        output_path = raw_input("\nEnter output " + file_mode.lower() + " path: ")
    return output_path



def search_file(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths



def encrypt_func(plaintext, key):  ## , key_size=256):
    try:
        text = plaintext + b"\0" * (AES.block_size - len(plaintext) % AES.block_size)
        IV = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, IV)
        return IV + cipher.encrypt(text)
    except Exception as e:
        raise e



def decrypt_func(ciphertext, key):
    try:
        IV = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, IV)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")
    except Exception as e:
        raise e



def encrypter_files(file_path, key, new_path):
    try:
        with open(file_path, 'rb') as fopen:
            plaintext = fopen.read()
        encr = encrypt_func(plaintext, key)
        with open(new_path, 'wb') as fopen:
            fopen.write(encr)
    except Exception as e:
        raise e



def decrypter_files(file_path, key, new_path):
    try:
        with open(file_path, 'rb') as fopen:
            ciphertext = fopen.read()
        decr = decrypt_func(ciphertext, key)
        with open(new_path, 'wb') as fopen:
            fopen.write(decr)
    except Exception as e:
        raise e



def encrypter_texts(text, key):
    try:
        enc_text = encrypt_func(text, key)
        b64_output = base64.b64encode(enc_text)
        return b64_output
    except Exception as e:
        raise e



def decrypter_texts(text, key):
    try:
        b64_output = base64.b64decode(text)
        dec_text = decrypt_func(b64_output, key)
        return dec_text
    except Exception as e:
        raise e



def info(file_mode, end_alg, key):
    if file_mode == "Text":
        b64 = " + Base64"
    else:
        b64 = ""
    print('\n' +
          "        .-\"\"-.                                          \n" +
          "       / .--. \                                           \n" +
          "      / /    \ \       " + file_mode + " " + end_alg +
          "\n      | |    | |                                        \n" +
          "      | |.-\"\"-.|       Algorithm: AES-" + str(len(key) * 8) + b64 +
          "\n     ///`.::::.`\                                       \n" +
          "    ||| ::/  \:: ;     Key: " + key +
          "\n    ||; ::\__/:: ;                                      \n" +
          "     \\\\\ '::::' /                                       \n" +
          "      `=':-..-'`                                            ")



def end(file_mode, output_path, output_text):
    if file_mode == "Text":
        print("\nOutput " + file_mode + ": \n" + output_text + '\n')
    else:
        print("\nOutput " + file_mode + " Path: \n" + output_path + '\n')



def main(opt_file_path, opt_folder_path, opt_text):
    print("\nInsert key (16, 24 or 32 bytes)")
    key = key_string()
    file_mode, path = file_modes(opt_file_path, opt_folder_path, opt_text)
    if file_mode == "File":
        print("\nWhat do you want to do?")
        print("[1] Encrypt    [2] Decrypt      (select 1 or 2)")
        alg_mode = choose_alg()
        if alg_mode == "Encrypt":
            print("\nDo you want to REPLACE the original file?")
            print("[1] Yes        [2] No           (select 1 or 2)")
            output_path = choose_path(file_mode, path)
            print("\nEncrypting... ")
            try:
                encrypter_files(path, key, output_path)
                info(file_mode, alg_mode + "ed", key)
                end(file_mode, output_path, None)
            except:
                print("\nFile " + path + " not valid for encryption")
                exit(1)
        if alg_mode == "Decrypt":
            print("\nDo you want to REPLACE the original file?")
            print("[1] Yes        [2] No           (select 1 or 2)")
            output_path = choose_path(file_mode, path)
            print("\nDecrypting... ")
            try:
                decrypter_files(path, key, output_path)
                info(file_mode, alg_mode + "ed", key)
                end(file_mode, output_path, None)
            except:
                print("\nFile " + path + " not valid for decryption")
                exit(1)
    elif file_mode == "Folder":
        print("\nWhat do you want to do?")
        print("[1] Encrypt    [2] Decrypt      (select 1 or 2)")
        alg_mode = choose_alg()
        if alg_mode == "Encrypt":
            print("\nDo you want to REPLACE the original folder?")
            print("[1] Yes        [2] No           (select 1 or 2)")
            output_path = choose_path(file_mode, path)
            print("\nEncrypting... ")
            errors = 0
            for files in search_file(path):
                file_name = files.split('/')[-1]
                new_path_files = output_path + '/' + file_name
                try:
                    encrypter_files(files, key, new_path_files)
                except:
                    print("File " + files + " not valid for encryption")
                    errors += 1
            if errors < len(search_file(path)):
                in_folder = len(search_file(path)) - errors
                info(file_mode, alg_mode + "ed [" + str(in_folder) + " file(s)]" , key)
                end(file_mode, output_path, None)
            elif errors == len(search_file(path)):
                exit(1)
        elif alg_mode == "Decrypt":
            print("\nDo you want to REPLACE the original folder?")
            print("[1] Yes        [2] No           (select 1 or 2)")
            output_path = choose_path(file_mode, path)
            print("\nDecrypting... ")
            errors = 0
            for files in search_file(path):
                file_name = files.split('/')[-1]
                new_path_files = output_path + '/' + file_name
                try:
                    decrypter_files(files, key, new_path_files)
                except:
                    print("File " + files + " not valid for decryption")
                    errors += 1
            if errors < len(search_file(path)):
                in_folder = len(search_file(path)) - errors
                info(file_mode, alg_mode + "ed [" + str(in_folder) + " file(s)]" , key)
                end(file_mode, output_path, None)
            elif errors == len(search_file(path)):
                exit(1)
    elif file_mode == "Text":
        text = opt_text
        print("\nWhat do you want to do?")
        print("[1] Encrypt    [2] Decrypt      (select 1 or 2)")
        alg_mode = choose_alg()
        if alg_mode == "Encrypt":
            print("\nEncrypted string will be encoded with Base64 algorithm")
            try:
                output_text = encrypter_texts(text, key)
                info(file_mode, alg_mode + "ed", key)
                end(file_mode, None, output_text)
            except:
                print("This text is not valid for encryption")
        if alg_mode == "Decrypt":
            try:
                output_text = decrypter_texts(text, key)
                info(file_mode, alg_mode + "ed", key)
                end(file_mode, None, output_text)
            except:
                print("This text is not valid for decryption")
