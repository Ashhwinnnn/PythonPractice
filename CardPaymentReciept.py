cardno=input('Enter the card no.:')

lastdigits=cardno[12:]
four='X'*4+' '
Displno=four*3 + lastdigits
print('The amount has been deducted from your card:', Displno)
