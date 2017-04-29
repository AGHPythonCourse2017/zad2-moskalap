class Strings():
    import datetime
    now =datetime.datetime.now()
    s = now.strftime('%Y-%m-%d')
    LOGS = './countit/logs/'+s+'.log'
    INIT_CODE = './countit/temporary_files/init.py'
    EXAMINED_CODE = './countit/temporary_files/examined_code.py'
    CLEAN_UP_CODE = './countit/temporary_files/clean_up_code.py'