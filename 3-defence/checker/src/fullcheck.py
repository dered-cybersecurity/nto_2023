import check
import exploit
import sys
import json

ip = sys.argv[1]

vulns = [
    'register_rewrite',
    'login_without_password',
    'set_permissions_idor',
    'change_password_idor',
    'write_on_read',
    'nosql_injection',
    'ssrf_reset_state',
    'xss'
]

result = {'ip': ip}

result['check'] = check.run(ip)

if result['check']['status'] == 'DOWN' and result['check']['trace'] in ['Connection failed', 'Connection timed out']:
    result['exploit'] = { v:result['check'] for v in vulns}
else:
    result['exploit'] = exploit.run(ip, vulns)

print(json.dumps(result))
