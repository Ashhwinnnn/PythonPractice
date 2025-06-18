amount=int(input('Enter the total bill amount:'))
if amount<1000:
    total=amount-amount*0.10
    print(total)
elif amount>=1000 and amount<5000:
    total=amount-amount*0.15
    print(total)
elif amount>=500 and amount<10000:
    total=amount-amount*0.20
    print(amount)
else:
    total=amount-amount*0.25
    print(total)
