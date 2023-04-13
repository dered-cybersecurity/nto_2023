package tcpio

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"net"
	"strconv"
	"time"
)

type Con struct {
	_addrudp string
	_addr    string
	_ind     string
	_rid     string
	con      net.Conn
	LastQ    time.Time
}

func (c *Con) Init(addr string) error {
	var err error
	c.con, err = net.Dial("tcp", addr)
	c._addr = addr
	if c.con != nil {
		c.con.Close()
	}
	return err
}
func (c *Con) Register() {
	query := map[string]string{
		"action":  "register",
		"payload": "1235"}
	queryA, _ := json.Marshal(query)
	resp, _ := c.Send(queryA)
	var respun map[string]string
	json.Unmarshal([]byte(resp), &respun)
	c._ind = respun["message"]

}
func (c *Con) JoinRoom() {
	query := map[string]string{
		"action":     "debuggame",
		"identifier": c._ind}
	queryA, _ := json.Marshal(query)
	resp, _ := c.Send(queryA)
	var respun map[string]string
	json.Unmarshal([]byte(resp), &respun)
	c._rid = respun["message"]

}

func (c *Con) ReciveStart() bool {
	query := map[string]string{
		"action":     "isready",
		"identifier": c._ind,
		"room_id":    c._rid,
	}

	if time.Now().Sub(c.LastQ).Seconds() < 5.0 {
		return false
	}
	c.LastQ = time.Now()
	queryA, _ := json.Marshal(query)
	resp, _ := c.Send(queryA)
	var respun map[string]string
	json.Unmarshal([]byte(resp), &respun)
	return respun["message"] == "True"
}
func (c *Con) IsEnded() bool {
	query := map[string]string{
		"action":     "isended",
		"identifier": c._ind,
		"room_id":    c._rid,
	}
	if time.Now().Sub(c.LastQ).Seconds() < 5.0 {
		return false
	}
	c.LastQ = time.Now()
	queryA, _ := json.Marshal(query)
	resp, _ := c.Send(queryA)
	var respun map[string]string
	json.Unmarshal([]byte(resp), &respun)
	return respun["message"] == "True"
}
func (c *Con) GetANS() string {
	query := map[string]string{
		"action":     "getflag",
		"identifier": c._ind,
		"room_id":    c._rid,
	}
	queryA, _ := json.Marshal(query)
	resp, _ := c.Send(queryA)
	var respun map[string]string
	json.Unmarshal([]byte(resp), &respun)
	return respun["message"]
}
func (c *Con) GetSeed() int {
	query := map[string]string{
		"action":     "getseed",
		"identifier": c._ind,
		"room_id":    c._rid,
	}
	queryA, _ := json.Marshal(query)
	resp, _ := c.Send(queryA)
	var respun map[string]string
	json.Unmarshal([]byte(resp), &respun)
	ret, _ := strconv.Atoi(respun["message"])
	return ret
}
func (c *Con) SendAns(arr []int) bool {
	payload := "[0"
	for i := 1; i < len(arr); i++ {
		payload += fmt.Sprintf(",%d", arr[i])
	}
	payload += "]"
	query := map[string]string{
		"action":     "sendans",
		"identifier": c._ind,
		"room_id":    c._rid,
		"payload":    payload,
	}
	queryA, _ := json.Marshal(query)
	resp, _ := c.Send(queryA)
	var respun map[string]string
	json.Unmarshal([]byte(resp), &respun)
	ret := respun["success"] == "True"
	return ret
}
func (c *Con) Send(packet []byte) (string, error) {
	var err error
	c.con, err = net.Dial("tcp", c._addr)
	if err != nil {
		log.Printf("E: %v\n", err)
		return "", err
	}
	send, err := c.con.Write(packet)
	if err != nil {
		log.Printf("E: %v\n", err)
		return "", err
	}
	if send == 0 {
	}
	recv, err := bufio.NewReader(c.con).ReadBytes('\n')
	if err != nil {
		log.Printf("E: %v\n", err)
		return "", err
	}
	c.con.Close()
	return string(recv), nil
}
