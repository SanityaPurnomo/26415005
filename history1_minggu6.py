#!/usr/bin/python

def main() :
	friends = ['Satria','Stephanie','Elbert']
	for i, name in enumerate(friends):
   	 print "iteration {iteration} is {name}".format(iteration=i, name=name)

if __name__ == '__main__' :
	main();
