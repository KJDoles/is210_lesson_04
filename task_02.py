import data
ACCESS = False
ATTEMPT = 3

while not ACCESS:
    PASSW = (raw_input('What is your password ({} attempts left)? '
                       .format(ATTEMPT)))
    if PASSW == data.PASSWORD:
        ACCESS = True
        print ('Access granted.')
    elif ATTEMPT <= 1:
        print ('Access is denied, please check password and try again later.')
        break
    ATTEMPT -= 1
