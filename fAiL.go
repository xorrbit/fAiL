package main

import (
    "fmt"
    "math/rand"
    "time"
    "strings"
)

var alnum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


func main() {
	rand.Seed(time.Now().UnixNano())

	for i := 0; i < 5000000; i++ {
		buf := make([]byte, 6)
		for j := 0; j < 6; j++ {
			buf[j] = alnum[rand.Intn(62)]
		}
		file_name := string(buf)

		if strings.Contains(strings.ToLower(file_name), "fail") {
			fmt.Printf("hit: %s pos: %d\n", file_name, i)
		}
	}
}

