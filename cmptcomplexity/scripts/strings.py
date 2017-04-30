class Strings():
    import datetime
    now =datetime.datetime.now()
    s = now.strftime('%Y-%m-%d')
    LOGS = './cmptcomplexity/logs/'+s+'.log'
    INIT_CODE = './temporary_files/init.py'
    EXAMINED_CODE = './temporary_files/examined_code.py'
    CLEAN_UP_CODE = './temporary_files/clean_up_code.py'