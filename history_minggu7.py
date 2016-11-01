#!/usr/bin/python

def main() :

	from time import localtime

	activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }

	time_now = localtime()
	hour = time_now.tm_hour

	for activity_time in sorted(activities.keys()):
    		if hour < activity_time:
        		print activities[activity_time]
        		break
		else:
    			print 'Unknown, AFK or sleeping!'

if __name__ == '__main__' :
	main();



#!/usr/bin/python

def main() :

	import unittest
	def median(pool):
    		copy = sorted(pool)
    		size = len(copy)
    		if size % 2 == 1:
        		return copy[(size - 1) / 2]
   		else:
        		return (copy[size/2 - 1] + copy[size/2]) / 2
	class TestMedian(unittest.TestCase):
    		def testMedian(self):
        		self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)

if __name__ == '__main__':
    unittest.main()



#!/usr/bin/python

def main() :

	import sys
	try:
    		total = sum(int(arg) for arg in sys.argv[1:])
    		print 'sum =', total
	except ValueError:
    		print 'Please supply integer arguments'

if __name__ == '__main__' :
	main();



#!/usr/bin/python

def main() :

	prices = {'apple': 0.40, 'banana': 0.50}
	my_purchase = {
    		'apple': 1,
    		'banana': 6}
	grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print 'I owe the grocer $%.2f' % grocery_bill

if __name__ == '__main__' :
	main();



#!/usr/bin/python

def main() :
	import re
	for test_string in ['555-1212', 'ILL-EGAL']:
    		if re.match(r'^\d{3}-\d{4}$', test_string):
        		print test_string, 'is a valid US local phone number'
    		else:
        		print test_string, 'rejected'

if __name__ == '__main__' :
	main();
