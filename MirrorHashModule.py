#!/usr/bin/env python

import os
import hashlib

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



def search_file(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths



def choose_hash():
    hash_mode = None
    while hash_mode != '1' and hash_mode != '2' and hash_mode != '3':
        hash_mode = raw_input("\n=> ")
    if hash_mode == '1':
        hash_mode = "Sha1"
    elif hash_mode == '2':
        hash_mode = "Sha-256"
    elif hash_mode == '3':
        hash_mode = "Md5"
    return hash_mode



def hashing_string(string, hash_mode):
    try:
        if hash_mode == "Sha-1":
            return hashlib.sha1(string).hexdigest()
        elif hash_mode == "Sha-256":
            return hashlib.sha256(string).hexdigest()
        elif hash_mode == "Md5":
            return hashlib.md5(string).hexdigest()
    except Exception as e:
        raise e



def hashing_files(path, hash_mode):
    try:
        with open(path, 'rb') as fopen:
            file = fopen.read()
        hash = hashing_string(file, hash_mode)
        return hash
    except Exception as e:
        raise e



def info(hash_mode):
    if hash_mode == "Sha-1":
        hash_name = hash_mode.upper() + "  "
    elif hash_mode == "Sha-256":
        hash_name = hash_mode.upper()
    elif hash_mode == "Md5":
        hash_name = hash_mode.upper() + "    "
    print('\n' +
          "        .-.                                     .-.\n" +
          "        | |                                     | |\n" +
          "        | |                                     | |\n" +
          "        | |-._                                  | |-._\n" +
          "        | | | |-.     Fingerprint!              |_| | |-.\n" +
          "       /|     ` |                              / )|_|_|_|\n" +
          "      | |       |                             | | `-^-^-'\n" +
          "      |         |     Algorithm: " + hash_name + "      |         |\n" +
          "      \         /                             \         /\n" +
          "       |       |                               |       |\n" +
          "       |       |                               |       |\n" )



def end(file_mode, path, text, hash_mode, hash):
    if file_mode == "File":
        print("\nFile: " + path)
        print('\n' + hash_mode.upper() + ": " + hash)
    elif file_mode == "Folder":
        i = 0
        while i < len(hash):
            print("\nFile: " + path[i])
            print(hash_mode.upper() + ": " + hash[i])
            i = i+1
    elif file_mode == "Text":
        print("\nText: " + text)
        print('\n' + hash_mode.upper() + ": " + hash)



def main(opt_file_path, opt_folder_path, opt_text):
    file_mode, path = file_modes(opt_file_path, opt_folder_path, opt_text)
    print("\nWhat type of fingerprint do you want to use?")
    print("[1] SHA-1    [2] SHA-256    [3] MD5")
    hash_mode = choose_hash()
    if file_mode == "File":
        try:
            hash = hashing_files(path, hash_mode)
            info(hash_mode)
            end(file_mode, path, None, hash_mode, hash)
        except:
            print("File " + path + " not valid for generate hash")
    elif file_mode == "Folder":
        paths = []
        hashes = []
        for files in search_file(path):
            try:
                hash = hashing_files(files, hash_mode)
                hashes.append(hash)
                paths.append(files)
            except:
                hashes.append("Not generated")
                paths.append(files)
        info(hash_mode)
        end(file_mode, paths, None, hash_mode, hashes)
    elif file_mode == "Text":
        try:
            hash = hashing_string(opt_text, hash_mode)
            info(hash_mode)
            end(file_mode, None, opt_text, hash_mode, hash)
        except:
            print("This text is not valid for generate hash")












