package main 

import "testing"

func BenchmarkSplit(b *testing.B) {
	SplitFile()
}


func BenchmarkLdetool(b *testing.B) {
	ReadLogFile()
}