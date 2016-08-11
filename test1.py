#!/usr/bin/python
# _*_ coding: UTF-8 _*_

print '======================================'

for letter in 'Python':
    if letter == 'h':
        #break
        continue
    print 'Current Letter:',letter

var = 10
while var > 0:
    print 'Current variable value:',var
    var = var - 1
    if var == 4:
        break

print "Good bye"

print '======================================'

i = 2
while (i<10):
    j = 2
    while(j <= (i/j)):
        if not (i%j):break
        j = j + 1
    if (j > i/j):print i,' is primer number'
    i = i +1

print "Good bye"

print '======================================'

for num in range(10,20):
	for i in range(2,num):
		if num % i == 0:
			j = num / i
			print '%d = %d * %d'%(num,i,j)
			break
	else:
		print num,'is primer number'
