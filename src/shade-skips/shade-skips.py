SQL_commands = ['SELECT',';--','&','-','|','TRUNCATE','%', 'UNION','DROP','CREATE','INTO','COPY','*',"'"]
XSS_commands = ['<','>','script','javascript',':','document','location','html','"','/','+']

def validate(input):
    sql_report , sql_injection= validateSQLInjection(input)
    xss_report , xss= validateXSS(input)
    return f'{sql_report} {xss_report}', (xss and sql_injection)

def validateXSS(data):
    for i in XSS_commands:
        if i.lower() in data.lower():
            return 'Cross-site Scripting: Vulnerable', True
    return 'Cross-site Scripting: NOT Vulnerable', False

def validateSQLInjection(data):
    for i in SQL_commands:
        if i.lower() in data.lower():
            return 'SQL Injection: Vulnerable', True
    return 'SQL Injection: NOT Vulnerable', False
