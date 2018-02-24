# coding: utf-8

# Fibonacci number finder
# 

f=[1, 1]

# print 'what order of Fibonacci Number?'
# lastStep = int(raw_input())
lastStep = 101

for n in range( len(f) - 1 , lastStep-1):
	f.append( f[ n ]+ f[ n - 1]  )

print ( '  f = ', f )
print ()
print (len(f))
