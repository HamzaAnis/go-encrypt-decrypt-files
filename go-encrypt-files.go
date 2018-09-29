package main

import (
	"bufio"
	"flag"
	"os"
	"strings"

	"github.com/fatih/color"
)

func main() {
	c := color.New(color.FgRed, color.Bold)
	reader := bufio.NewReader(os.Stdin)

	printHeader()
	key := flag.String("key", "encrypt_files", "key to encrypt and decrypt")
	flag.Parse()
	for {
		if *key == "encrypt_files" {
			c.Print("please enter the key to encrypt and decrypt files ")
			key_, err := reader.ReadString('\n')
			if err != nil {
				color.Red("error while reading key")
			}
			*key = strings.TrimSpace(string(key_))
		}
		reader.ReadString('\n')
	}
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
