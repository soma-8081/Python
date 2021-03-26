import operator
soma={2:4,5:6,7:8,9:3}
print('Original dictionary:',soma)
sorted_soma=sorted(soma.items(),key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_soma)
sorted_soma = sorted(soma.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_soma)
