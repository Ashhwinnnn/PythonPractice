url=input('Enter the url of the website:')
protocol=url[ : url.find(':')]
dot1=url.find('.')
dot2=url.find('.',dot1+1)
domain=url[dot1+1:dot2]
page=url[url.find('/', dot2): ]

print('Protocol:', protocol)
print('Domain:', domain)
print('Page:', page)