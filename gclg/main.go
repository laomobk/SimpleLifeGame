package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	args := os.Args
	h, w := 20, 10

	if len(args) == 3 {
		h64, _ := strconv.ParseInt(args[1], 10, 32)
		w64, _ := strconv.ParseInt(args[2], 10, 32)

		h = int(h64)
		w = int(w64)
	} else {
		fmt.Println("gclg [height] [width]")
		return
	}

	cmap := (&CellMap{
		Height: h,
		Width:  w,
	}).InitBySeed(TimeSeed())

	newSimulator(cmap).RunNoInterval()
}
