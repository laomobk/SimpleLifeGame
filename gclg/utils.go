package main

import (
	"time"
)

func TimeSeed() int64 {
	return time.Now().UnixNano()
}
