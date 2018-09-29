package main

import (
	"bufio"
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"flag"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"

	"github.com/fatih/color"
)

func main() {

	printHeader()
	key := flag.String("key", "encrypt_files", "key to encrypt and decrypt")
	encryptFolder := flag.String("ef", "encrypt", "folder in which encrypted files will be stored")
	decryptFolder := flag.String("df", "decrypt", "folder in which decrypted files will be stored ")

	flag.Parse()

	for {
		// Check if the key is valid
		if _, err := aes.NewCipher([]byte(*key)); err != nil {
			fmt.Println(err)
			inputKey(key)
			continue
		}
		printMenu()
		choice := readInput()
		if choice == "encrypt" {
			fmt.Print("enter file name to encrypt: ")
			fileName := readInput()
			encrypt(fileName, encryptFolder, key)
		} else if choice == "decrypt" {

		} else if choice == "exit" {
			os.Exit(0)
		} else {
			c := color.New(color.FgRed, color.Bold)
			c.Println("you entered wrong choice")
		}

	}
	fmt.Println(*key)
	fmt.Println(*encryptFolder)
	fmt.Println(*decryptFolder)

}

func encrypt(fileName string, encryptFolder, keyString *string) {
	plaintext, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Println(err)
		return
	}
	key := []byte(*keyString)

	block, err := aes.NewCipher(key)
	if err != nil {
		fmt.Println(err)
		return
	}

	ciphertext := make([]byte, aes.BlockSize+len(plaintext))
	iv := ciphertext[:aes.BlockSize]
	if _, err := io.ReadFull(rand.Reader, iv); err != nil {
		fmt.Println(err)
		return
	}

	stream := cipher.NewCFBEncrypter(block, iv)
	stream.XORKeyStream(ciphertext[aes.BlockSize:], plaintext)

	//creating folder if not exist
	folderPath := filepath.Join(".", *encryptFolder)
	os.MkdirAll(folderPath, os.ModePerm)

	// create a new file for saving the encrypted data.
	p := filepath.FromSlash(*encryptFolder + "/" + fileName)

	// f, err := os.Create(p)
	// if err != nil {
	// 	fmt.Println(err)
	// 	return
	// }
	// _, err = io.Copy(f, bytes.NewReader(ciphertext))
	// if err != nil {
	// 	fmt.Println(err)
	// 	return
	// }
	// fmt.Println("written to path", p)
	ioutil.WriteFile(p, ciphertext, 777)
}
func printMenu() {
	c := color.New(color.FgCyan, color.Bold)
	s := "what would you like to do?\n" +
		"\tencrypt: to encrypt file\n" +
		"\tdecrypt: to decrypt file\n" +
		"\texit: to exit program\n" +
		"choice: "
	c.Print(s)
}
func readInput() string {
	reader := bufio.NewReader(os.Stdin)
	line, _, err := reader.ReadLine()
	if err != nil {
		fmt.Println(err)
	}
	return string(line)
}

func inputKey(key *string) {
	c := color.New(color.FgRed, color.Bold)
	reader := bufio.NewReader(os.Stdin)
	c.Print("please enter the key to encrypt and decrypt files ")
	input, err := reader.ReadString('\n')
	if err != nil {
		color.Red("error while reading key")
	}
	*key = strings.TrimSpace(string(input))
}
func printHeader() {
	banner := "           _________________________________________ \n" +
		"          | _______________________________________ |\n" +
		"          ||                                       ||\n" +
		"          || # cat banner_start.txt                ||\n" +
		"          ||                                       ||\n" +
		"          ||                                       ||\n" +
		"          ||  MIRROR - ENCRYPTION/DECRYPTION TOOL  ||\n" +
		"   @      ||         Created by Mario Saso         ||   @\n" +
		"  / \\     ||                                       ||  / \\\n" +
		"-/---\\---/||                                       ||-/---\\---/\n" +
		"/     \\ / ||        ___________                    ||/     \\ /\n" +
		"       @  ||       |           |                   ||       @\n" +
		"          ||       | S T A R T |    (*)   ( )      ||\n" +
		"          ||       |___________|                   ||\n" +
		"          ||                                       ||\n" +
		"          ||                                       ||\n" +
		"          ||_______________________________________||\n" +
		"          |____________________________________[_]__|\n"
	// banner, _ := ioutil.ReadFile("banner.txt")

	c := color.New(color.FgGreen, color.Bold)
	c.Println(banner)
}
