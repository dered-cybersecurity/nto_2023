from sage.all import *
from factorize import factorize as ife
import math
from info import info as infos
from libnum import solve_crt
from Crypto.Util.number import *
import requests
import time
#main idea to find small factors of an order of element
#than take subgroup of order with small factor and compute discrete log
#than take crt and win 

url = 'http://127.0.0.1:5000'
def get_info(num):
    anses = []
    for _ in range(num):
        anses.append(requests.get(f"{url}/shared_flag").json())
    return anses

def find_convinient_factor(number, min=2**10, max=2**40):
    factors = ife(number)
    maxi = None
    for i in range(len(factors)):
        if min < factors[i] < max: 
            maxi = factors[i]
    return maxi

def get_small_discrete_log(info):
    p = info['p']
    g = info['g']
    order = p - 1
    _factor = find_convinient_factor(order)
    if _factor is None:
        return None, None
    G = GF(p)
    new_g = G(pow(g, order//_factor, p))
    new_secret = G(pow(info['shared_flag'], order//_factor, p))
    flag_part = discrete_log(new_secret, new_g, _factor)
    assert pow(new_g, flag_part, p) == new_secret
    return flag_part, _factor

def handle_info(infos):
    orders = []
    remainders = []
    for info in infos:
        parted = get_small_discrete_log(info)
        if parted[1] is not None:
            if parted[1] not in orders:
                orders.append(parted[1])
                remainders.append(parted[0])
        print(f"{prod(orders).bit_length()}/180 of progress", end = '\r')
        if prod(orders) > 2**180:
            return orders, remainders
    return orders, remainders
def solve():
    ords, rems = handle_info(infos)
    print(long_to_bytes(solve_crt(rems,ords )).decode())
if __name__ == "__main__":
    solve()
