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
