import subprocess
import json

def generate(seed):
    out = b"NO\n"
    seed -= 1
    while out == b"NO\n":
        seed += 1
        out = subprocess.check_output(["./check", str(seed)])
    subprocess.run(["chmod", "777", "data.txt"])
    a = open("data.txt", "r")
    s = a.read().split('\n')
    a.close()
    bn = int(s[0], 10)
    g = json.loads(s[1])
    return g,bn,seed

def check_moves(sanity,moves):
    if 0 not in moves or 14999 not in moves or len(moves) < 2 or len(moves) > 30:
        return False
    print("MOVES",moves)
    npos = 0
    for i in range(len(moves) - 1):
        if str(moves[i]) not in sanity.keys():
            print(moves[i], "NOT IN GRAPH")
            return False
        pos = sanity[str(moves[i])]
        npos = moves[i + 1]
        if str(npos) not in pos.keys():
            print(npos, "NOT IN TIE")
            return False
    if moves[len(moves) - 1] != 14999:
        print("NO END")
        return False
    return True
        
        


