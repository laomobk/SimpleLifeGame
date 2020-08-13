package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Cell struct {
	state uint8 // dead -> 0 | alive -> 1
}

func (self *Cell) Update(alive int) *Cell {
	if self.state == 1 {
		self.caseAlive(alive)
	} else if self.state == 0 {
		self.caseDead(alive)
	}

	return self
}

func (self *Cell) caseAlive(alive int) {
	if alive < 2 || alive > 3 {
		self.state = 0
	}
}

func (self *Cell) caseDead(alive int) {
	if alive == 3 {
		self.state = 1
	}
}

func (self *Cell) State() uint8 {
	return self.state
}

type CellMap struct {
	Height int
	Width  int

	matrix [][]*Cell
}

func (self *CellMap) get(x, y int) *Cell {
	if y >= 0 && y < self.Height && x >= 0 && x < self.Width {
		return self.matrix[y][x]
	}
	return nil
}

func (self *CellMap) initMatrix() {
	var matrix [][]*Cell

	for y := 0; y < self.Height; y++ {
		matrix = append(matrix, []*Cell{})
		for x := 0; x < self.Width; x++ {
			matrix[y] = append(matrix[y], nil)
		}
	}

	self.matrix = matrix
}

func (self *CellMap) InitBySeed(seed int64) *CellMap {
	self.initMatrix()

	matrix := self.matrix
	rand.Seed(seed)

	for _, line := range matrix {
		for i := range line {
			c := new(Cell)
			c.state = uint8(rand.Intn(2))

			line[i] = c
		}
	}

	return self
}

type Simulator struct {
	cmap *CellMap
}

func (self *Simulator) getSurroundAliveCount(x, y int, target *CellMap) int {
	mget := target.get

	sur := []*Cell{
		mget(x-1, y-1), mget(x, y-1), mget(x+1, y-1),
		mget(x-1, y), mget(x+1, y),
		mget(x-1, y+1), mget(x, y+1), mget(x+1, y+1),
	}

	alivec := 0

	for _, c := range sur {
		if c != nil {
			if c.state == 1 {
				alivec++
			}
		}
	}

	return alivec
}

func (self *Simulator) Update() (alivec int) {
	matrix := self.cmap.matrix
	buf_cmap := *self.cmap

	for y, line := range matrix {
		for x, cell := range line {
			alivec := self.getSurroundAliveCount(x, y, &buf_cmap /* copy */)

			if cell.Update(alivec).state == 1 {
				alivec++
			}
		}
	}

	return
}

func (self *Simulator) DrawMap() {
	matrix := self.cmap.matrix

	var buf string

	puts(0, 0, "")

	for _, line := range matrix {
		for _, cell := range line {
			buf += CellShapes[cell.state]
		}
		buf += "\n"
	}

	fmt.Printf(buf)
}

func (self *Simulator) RunNoInterval() {
	clear()

	for {
		self.DrawMap()
		self.Update()

		printFps()
	}
}

func (self *Simulator) RunWithInterval(intervalMilSec int64) {
	clear()

	for {
		self.DrawMap()
		self.Update()

		time.Sleep(time.Duration(intervalMilSec) * time.Millisecond)

		printFps()
	}
}

func newSimulator(cmap *CellMap) *Simulator {
	return &Simulator{
		cmap: cmap,
	}
}
