number=23
guess=int(raw_input('Enter an integer:'))

if guess==number: 
    print 'hahahaha,you guess it.' 
    print "(but you do not win any prizes!)" 
elif guess<number:   
    print 'too small'
else:
    print 'too big'
    print 'Done'
