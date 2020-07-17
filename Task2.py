#a
suitcase = []
suitcase.append('Hat')
suitcase.append('Dress')
suitcase.append('Sun block')
suitcase.append('Swimming suit')
suitcase.append('Book')
print(suitcase)
#b
del suitcase [-1]
print(suitcase)
#C
suitcase2 = list(suitcase)
suitcase2[0] = 'Sunglasses'
suitcase = tuple(suitcase2)
print(suitcase)

