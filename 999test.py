




#EX

meter1= '123200456123'
meter2= 'EX-123456'
meter3= 'EX-2453145'
meter4= '121200456123'

def is_numeric(input_str):
    return input_str.isdigit()




def is_askue(meter):
    if len(meter) == 9 and meter.startswith('EX-1'):
        if is_numeric(meter[-6:]):
            return 1
    elif len(meter) == 10 and meter.startswith('EX-2'):
        if is_numeric(meter[-7:]):
            return 1
    elif len(meter) == 12 and is_numeric(meter[-12:]):
        if meter[:2] == '20' and meter[2:4] in ('15', '16', '17', '18', '19', '20', '21', '22'):
            return 1
        elif meter[:2] == '11' and meter[2:3] in ('1', '3', '4', '5'):
            return 1
        elif meter[:2] == '02' and meter[2:3] in ('1', '3', '4'):
            return 1
        elif meter[:2] == '12' and meter[2:3] in ('1', '3', '4'):
            return 1
        else:
            return 0
    else:
        return 0
    
    
a = is_askue(meter2)
print (a)


    
