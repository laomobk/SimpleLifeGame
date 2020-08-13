package main

import (
	"fmt"
	"time"
)

var _lastTime int64 = 0

func printFps() {
	nowTime := time.Now().UnixNano()

	interval := nowTime - _lastTime

	_lastTime = nowTime

	if interval == 0 {
		interval = 1
	}

	fps := int64(time.Second) / interval

	fmt.Printf("\nfps: %08d", fps)
	clearFromCursor()
}
