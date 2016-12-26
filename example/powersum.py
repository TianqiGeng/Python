def powersum(power,*args):
    '''return sum:'''
    total=0
    for i in args:
        total +=pow(i,power)
    return total
