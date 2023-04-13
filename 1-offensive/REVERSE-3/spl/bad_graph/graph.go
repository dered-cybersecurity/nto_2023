package game

import (
	"math/rand"
)

type Graph struct {
	Matrix SpecMatrix
}

func have_out(m map[int]int) bool {
	for k := range m {
		if m[k] == -1 {
			return true
		}
	}
	return false
}

func (g *Graph) Optimize() {
	var status map[int]bool
	status = make(map[int]bool)
	for a := 0; a < g.Matrix.sizey; a++ {
		if !have_out(g.Matrix.Arr[a]) {
			status[a] = true
		}
	}
	var new_status map[int]bool
	for len(status) != 0 {
		for k := range status {
			var n int
			for n = range g.Matrix.Arr[k] {
				break
			}
			g.Matrix.Arr[k][n] = -1
			g.Matrix.Arr[n][k] = 1
			new_status = make(map[int]bool, 0)
			if !have_out(g.Matrix.Arr[n]) {
				new_status[n] = true
			}
		}
		status = new_status
	}

}

func (g *Graph) Init(size, seed, number int) {
	g.Matrix.Init(size, size)
	rand.Seed(int64(seed))
	for i := 0; i < size; i++ {
		for j := len(g.Matrix.Arr[i]); j < number; j++ {
			point, val := rand.Int()%size, 1
			for _, found := g.Matrix.Arr[i][point]; found || point == i; _, found = g.Matrix.Arr[i][point] {
				point = rand.Int() % size
			}
			g.Matrix.Arr[i][point] = val
			g.Matrix.Arr[point][i] = -val
		}
	}
	g.Optimize()
}
