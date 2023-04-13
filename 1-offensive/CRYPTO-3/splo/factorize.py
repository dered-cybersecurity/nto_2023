from __future__ import print_function, unicode_literals

import requests 
import time
ENDPOINT = "http://factordb.com/api"
class Singleton(type):
    _instances = {}
    numbers = dict()
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class FactorDB(metaclass=Singleton):
    def __init__(self):
        self.session = requests.Session()
    def factor(self, n):
        facs = self.session.get(f"{ENDPOINT}/api/?query={n}").json()['factors']
        factors = []
        for fac in facs:
            factors.append(int(fac[0]))
        return factors
def factorize(n):
    f = FactorDB()
    return f.factor(n)
