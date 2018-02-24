# coding: utf-8

# Prime number finder
#   Prompted for an expoent of ten as the max number to find up to, this probram finds primes,
#   one by one, and adds them to a list of found primes, and checks future candidates against
#   this list.
# 
p=[]

print ('max exp')
maxExp = int(input())
maxNum = pow(10,maxExp)

percent = int(maxNum/100.0)

for n in range(2, maxNum):
	# Print progress
	if n % percent == 0:
		if n % (10 * percent) == 0:
			print (". " + str(n/percent) + "%")
		elif n % (2 * percent) == 0:
			print (".")
	#print 'checking ', n
	for x in p:
		# Only need to check possible factors up to the square of the candidate
		if x <= pow(n,.5):
			if n % x == 0:
				break
	else:
		#print ('  ', n, ' is prime')
		p.append(n)
		
		
print ('  p = ', p)
print ()
print (len(p))
print ((float(len(p)) / maxNum) * 100.0, '%')

