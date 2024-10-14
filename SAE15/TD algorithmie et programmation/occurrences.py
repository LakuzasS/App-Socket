"""def occurrences(tab, x):
    return tab.count(x)

tab = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} apparaît {} fois dans la liste'.format(x, occurrences(tab, x)))"""


import numpy
numpy.random.seed(6)
values = values.arange(1,46)
for i in range(6):
    x = numpy.random.choice(values, size = 5, replace = False)
    print(x) 

