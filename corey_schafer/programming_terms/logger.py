def logger(msg):

    def log_message():
        print('Log:', msg)

    return log_message


log_hi = logger('HI!')
log_hi()
