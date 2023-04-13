package game

type SpecMatrix struct {
	sizex int
	sizey int
	Arr   map[int](map[int]int)
}

func (sm *SpecMatrix) Init(sizex, sizey int) {
	sm.Arr = make(map[int]map[int]int)
	for i := 0; i < sizey; i++ {
		sm.Arr[i] = make(map[int]int)
	}
}
