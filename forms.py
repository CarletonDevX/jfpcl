def mk_web_print():
    return {
        'service': 'page/UserWebPrint',
    }

def mk_select_printer(radio_group):
    return {
        'service': 'direct/1/UserWebPrintSelectPrinter/$Form',
        'sp': 'S0',
        'Form0': '$Hidden,$Hidden$0,$TextField,$Submit,$RadioGroup,$Submit$0,$Submit$1',
        '$Hidden': '',
        '$Hidden$0': '',
        '$TextField': '',
        '$RadioGroup': radio_group,
        '$Submit$1': '2. Print Options and Account Selection \xc2',
    }

def mk_print_options(copies):
    return {
        'service': 'direct/1/UserWebPrintOptionsAndAccountSelection/$Form',
        'sp': 'S0',
        'Form0': 'copies,$RadioGroup,$TextField$0,$Submit,$Submit$0',
        'copies': copies,
        '$RadioGroup': '0',
        '$Submit': '3. Upload Documents \xc2'
    }

def mk_upload_file():
    return {
        'service': 'direct/1/UserWebPrintUpload/$Form$0',
        'sp': 'S1',
        'Form1': '',
    }

def mk_login(username, password):
    return {
        'service': 'direct/1/Home/$Form$0',
        'sp': 'S0',
        'Form0': '$Hidden$0,$Hidden$1,inputUsername,inputPassword,$PropertySelection$0,$Submit$0',
        '$Hidden$0': 'true',
        '$Hidden$1': 'X',
        '$PropertySelection$0': 'en',
        '$Submit$0': 'Log in',
        'inputUsername': username,
        'inputPassword': password,
    }
