import requests
from forms import *


ENDPOINT = 'https://print.ads.carleton.edu:9192'
APP      = ENDPOINT + '/app'
UPLOAD   = ENDPOINT + '/upload'


class Session(object):

    def __init__(self):
        self.session = requests.session()


    def connect(self):
        self.session.get(APP)


    def login(self, username, password):
        self.sesion.post(APP, data=mk_login(username, password))


    def navigate(self):
        self.session.get(APP + '?service=page/UserWebPrint', params=mk_web_print())
        self.session.get(APP + '?service=action/1/UserWebPrint/0/$ActionLink')


    def find_printer(self, printer):
        query_base = '?service=direct/1/UserWebPrintSelectPrinter/table.tablePages.linkPage&sp=AUserWebPrintSelectPrinter%2Ftable.tableView&sp='
        for page in range(1, 4):
            resp0 = self.session.get(APP + query_base + page)
            r = re.compile('value=\"([0-9]+)\" .*\n' + printer, re.MULTILINE | re.DOTALL)
            match = r.search(resp0.text)
            if match is not None:
                return match.group(1)
        raise Exception('Printer does not exist: ' + printer)


    def select_printer(self, printer_id):
        self.session.post(APP, data=mk_select_printer(printer_id))


    def submit_options(self, copies):
        resp = self.session.post(APP, data=mk_print_options(copies))
        r = re.compile('uploadUID = \'([0-9]+)\'')
        return r.search(resp.text).groups(1) # uid


    def upload(self, uid, files):
        self.session.post(UPLOAD + '/' + uid, data=files)
