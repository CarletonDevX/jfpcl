import re
import requests
from subprocess import Popen, PIPE

def get_printers():
    resp = requests.get('https://print.ads.carleton.edu/printers/')
    row_expr = (
        '<td[^>]*><font[^>]*><a[^>]*>([^>]*)</a></font></td>'
        '<td[^>]*><font[^>]*><font[^>]*>([^>]*)</font></font></td>'
        '<td[^>]*><font[^>]*>([^>]*)</font></td>'
        '<td[^>]*><font[^>]*>([^>]*)</font></td>'
        '<td[^>]*><font[^>]*>([^>]*)</font></td>'
        '<td[^>]*><font[^>]*>([^>]*)</font></td>'
        )
    row = re.compile(row_expr, re.MULTILINE | re.DOTALL)
    for match in row.finditer(resp.text):
        name, status, location, jobs, model, notes = match.groups()
        yield {
            'name': name,
            'status': status,
            'location': location,
            'jobs': jobs,
            'model': model,
            'notes': notes,
            }

def fzf_printer():
    fzf = Popen(['fzf'], stdin=PIPE, stdout=PIPE)
    for printer in get_printers():
        row = '\t'.join([printer['name'], printer['status'], printer['location']]) + '\n'
        fzf.stdin.write(row.encode('utf-8'))
    choice, _ = fzf.communicate()
    return choice.split('\t'.encode('utf-8'))[0]
