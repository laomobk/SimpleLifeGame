// +build linux
package main

import (
	"fmt"
)

const pcstr = "\033[%d;%dH%s"

var CellShapes = []string{" ", "■"}

func puts(x, y int, s string) {
	fmt.Printf(pcstr, y, x, s)
}

func putCell(x, y int, cellState uint8) {
	puts(x, y, CellShapes[cellState])
}

func clear() {
	fmt.Printf("\033[2J")
}

func clearFromCursor() {
	fmt.Printf("\033[K")
}
