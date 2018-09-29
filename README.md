# go-encrypt-files
A tool that use Advance Encryption Algorithm to encrypt and decrypt files.

```
           _________________________________________                                                 
          | _______________________________________ |    
          ||                                       ||    
          || # cat banner_start.txt                ||    
          ||                                       ||
          ||                                       ||    
          ||  MIRROR - ENCRYPTION/DECRYPTION TOOL  ||    
   @      ||         Created by Hamza Anis         ||   @          
  / \     ||                                       ||  / \         
-/---\---/||                                       ||-/---\---/    
/     \ / ||        ___________                    ||/     \ /     
       @  ||       |           |                   ||       @      
          ||       | S T A R T |    (*)   ( )      ||    
          ||       |___________|                   ||    
          ||                                       ||    
          ||                                       ||    
          ||_______________________________________||    
          |____________________________________[_]__|

```

## Repo Overview

```
│   .gitignore              This file includes the gitignore for the golang program
│   ecrypt-decrypt-file.go  This is the source code for the program
│   LICENSE                 License of the program
│   README.md               Project readme
└───
```

### Usage
```
$ encrypt_decrypt_file --help

  -df string
        folder path to store decrypted files (default "decrypt")
  -ef string
        folder path to store encrypted files (default "encrypt")
  -key string
        key to encrypt and decrypt (default "default key 1234")

$ encrypt_decrypt_file --key=[keytouse] --ef=[encrypt folder path] --df=[decrypt path]
```

### Sample run
```
$ encrypt_decrypt_file --key my16bitaeskey123
```
The key which is used to encrypt should be same as the key that will be used for decrypt

