package main

import (
	"fmt"
	gg "sploit/bad_graph"
	badio "sploit/servertcpio"

	"gonum.org/v1/gonum/graph/path"
	"gonum.org/v1/gonum/graph/simple"
)

const server_addr = "localhost:4444"

func BetterGraph(g gg.Graph) *simple.DirectedGraph {
	arr := g.Matrix.Arr
	ret := simple.NewDirectedGraph()
	for i := 0; i < len(arr); i++ {
		for k := range arr[i] {
			if arr[i][k] == 1 {
				ret.SetEdge(simple.Edge{F: simple.Node(i), T: simple.Node(k)})
			}
		}
	}
	return ret
}

func main() {
	var con badio.Con
	err := con.Init(server_addr)
	if err != nil {
		panic(err)
	}
	con.Register()
	con.JoinRoom()
	for !con.ReciveStart() {
	}
	seed := con.GetSeed()
	var game_graph gg.Graph
	game_graph.Init(15000, seed, 10)
	bettergraph := BetterGraph(game_graph)
	pth := path.DijkstraFrom(simple.Node(0), bettergraph)
	end, _ := pth.To(14999)
	ans := make([]int, 0)
	for _, i := range end {
		ans = append(ans, int(i.ID()))
	}
	if len(ans) == 0 {
	}
	con.SendAns(ans)
	for !con.IsEnded() {
	}
	cur := con.GetANS()
	fmt.Println(cur)
}
