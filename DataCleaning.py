scan=input('Enter the text to scan:')
clean=''
for x in scan:
    if x.isalpha() or x.isspace():
        clean=clean+x
    else:
        clean=clean+' ' 
print('The cleaned test is:', clean)