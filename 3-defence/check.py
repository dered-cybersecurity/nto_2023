import subprocess
import json
import time

CHECKS = 10

ip = 'xss'

for i in range(CHECKS):
    print(f'Check {i+1}/{CHECKS}')
    st = time.time()
    cmd = ['docker', 'run', '--network', 'service_xss', 'checker', ip]
    r = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data = json.loads(r.stdout)
    try:
        assert data['check']['status'] == 'UP'
        for vuln in data['exploit']:
            assert data['exploit'][vuln]['status'] == 'NOT FIXED'
    except AssertionError:
        print(f'Failed on run {i}')
        print(f'stdout: {r.stdout}\nstderr: {r.stderr}')
        exit(1)

    t = time.time() - st
    print(f'Check {i+1}/{CHECKS} success in {t} s')
