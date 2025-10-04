
d1={'tsla':300,'amzn':500,'goog':900}
print(d1)

#accessing elem
#old
print(d1['nifty'])
#new
print(d1.get('nifty'))

#adding new elem
#old
d1['nvda']=689
#new
d1.update({'ongc':567})

print(d1)

#updating elem
d1['nvda']=700
d1.update({'ongc':600})
print(d1)

#del elem
del d1['goog']
d1.pop('tsla')

print(d1)


#set
