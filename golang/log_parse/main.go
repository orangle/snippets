package main

import (
	"fmt"
	"log"
	"os"
	"compress/gzip"
	"bufio"
	"strings"
	"strconv"
)

func main() {
	//OneLine()
	//ReadLogFile()
	//SplitOne()
	SplitFile()
}

//SplitOne #
func SplitOne() {
	logs := `27.154.70.117 - - [20/Nov/2018:20:23:56 +0800] 2 "GET http://7img1.tianlaikge.com/tv/homeimage/201709/shengridangao.zip HTTP/1.1" 200 842186 841382 "-" "-" "Dalvik/2.1.0 (Linux; U; Android 7.1.2; vivo Y79A Build/N2G47H)" "-" 219082621 "HIT" 27.159.73.35`
	bS := strings.Split(logs, " ") 
	qS := strings.Split(logs, `"`)
	fmt.Println(bS[10])
	// fmt.Println(qS[1])
	fmt.Println(strings.Join(qS, ", "))
}


//SplitFile #
func SplitFile() {
	filename := "/Users/liuzhizhi/udn/testdatas/7img1.tianlaikge.com.gz"
	file, err := os.Open(filename)

	if err != nil {
		log.Fatal(err)
	}

	gz, err := gzip.NewReader(file)
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	defer gz.Close()

	scanner := bufio.NewScanner(gz)
	var total int64
	total = 0

	for scanner.Scan() {
		line := string(scanner.Bytes())
		bS := strings.Split(line, " ") 
		qS := strings.Split(line, `"`)
		if len(qS) != 13 {
			fmt.Println(line)
			continue
		}	
		
		i, err := strconv.Atoi(bS[10])
		if err != nil {
			fmt.Println(line)
			continue
		}
		total = total + int64(i)
	}
	fmt.Println("total: ", total)
}


//OneLine #
func OneLine() {
	var logs = []byte(`27.154.70.117 - - [20/Nov/2018:20:23:56 +0800] 2 "GET http://7img1.tianlaikge.com/tv/homeimage/201709/shengridangao.zip HTTP/1.1" 200 842186 841382 "-" "-" "Dalvik/2.1.0 (Linux; U; Android 7.1.2; vivo Y79A Build/N2G47H)" "-" 219082621 "HIT" 27.159.73.35`)

	g := &Nginx{}
	ok, err := g.Extract(logs)
	if !ok {
		if err != nil {
			fmt.Println(err)
		}
	}
	fmt.Println(g.ByteSend)
}

//ReadLogFile #
func ReadLogFile() {
	g := &Nginx{}
	filename := "/Users/liuzhizhi/udn/testdatas/7img1.tianlaikge.com.gz"
	file, err := os.Open(filename)

	if err != nil {
		log.Fatal(err)
	}

	gz, err := gzip.NewReader(file)

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	defer gz.Close()

	scanner := bufio.NewScanner(gz)
	var total int64
	total = 0

	for scanner.Scan() {
		ok, err := g.Extract(scanner.Bytes())
		if !ok {
			if err != nil {
				fmt.Println(err)
			}
			continue
		}
		total = total + g.ByteSend
	}
	fmt.Println("total: ", total)
}