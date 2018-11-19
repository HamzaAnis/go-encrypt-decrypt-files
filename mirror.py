#!/usr/bin/env python
# coding=utf-8

import os
import optparse
import MirrorGenModule
import MirrorAesModule
import MirrorHashModule
import MirrorRsaModule


def get_opts():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="file_path", help="File path to encrypt\n")
    parser.add_option("-F", "--folder", dest="folder_path", help="Folder path to encrypt\n")
    parser.add_option("-t", "--text", dest="text", help="Text to encrypt")
    parser.add_option("-r", "--rsagen", dest="rsa_bits", help="Generate a keypair for RSA (512 or 1024 bits)\n")
    parser.add_option("-a", "--aesgen", dest="aes_bits", help="Generate a random key for AES (128, 192 or 256 bits)\n")
    (opts, args) = parser.parse_args()
    return opts



def banner():
    print('\n\n' +
          "  ___________ @ @                                                     \n" +
          " /   v1.0   @\   @                       _                            \n" +
          " \___________/  _@              ___ __ _(_)__ _ __ _  ___ __ _        \n" +
          "           @  _/@ \_____       / _ ' _` | |__` |__` |/ _ \__` |       \n" +
          "            @/ \__/-=-=^`     | | | | | | |  | |  | | (_) | | |       \n" +
          "             \_ /             |_| |_| |_|_|  |_|  |_|\___/  |_|       \n" +
          "              <|                                                      \n" +
          "              <|                     github.com/M4R1OS4S0             \n" +
          "              <|                                                      \n")



def choose_module():
    module = None
    while module != '1' and module != '2' and module != '3':
        module = raw_input("\n=> ")
    if module == '1':
        module = "AES"
    elif module == '2':
        module = "RSA"
    elif module == '3':
        module = "HASH"
    return module



def main():
    banner()
    opts = get_opts()
    if opts.aes_bits or opts.rsa_bits:
        MirrorGenModule.main(opts.rsa_bits, opts.aes_bits)
        exit()
    print("\nWhat algorithm do you want to use?\n")
    print("[1] AES Encryption  (128, 192 or 256 bits)")
    print("[2] RSA Encryption  (512 or 1024 bits)")
    print("[3] Fingerprint     (SHA-1, SHA-265 and MD5)")
    module = choose_module()
    if module == "AES":
        MirrorAesModule.main(opts.file_path, opts.folder_path, opts.text)
    elif module == "RSA":
        MirrorRsaModule.main(opts.text)
    elif module == "HASH":
        MirrorHashModule.main(opts.file_path, opts.folder_path, opts.text)



if __name__ == '__main__':
    main()



