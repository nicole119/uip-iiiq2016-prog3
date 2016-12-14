while true:
    preg = imput("preguntale a juan:")

    if preg.endswith('?'):
        print ("Ofi")

    elif preg >= 'A'and preg <='Z':
        print ("chilea")

    elif (len(preg)==0):
        print ("Mmm")

    else:
        print ("me da igual")