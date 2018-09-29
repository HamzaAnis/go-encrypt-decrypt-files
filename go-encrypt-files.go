package main

import "github.com/fatih/color"

func main() {
	printHeader()
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
