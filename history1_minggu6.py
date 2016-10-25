#!/usr/bin/python

def main() :
	friends = ['Satria','Stephanie','Elbert']
	for i, name in enumerate(friends):
   	 print "iteration {iteration} is {name}".format(iteration=i, name=name)

if __name__ == '__main__' :
	main();




#!/usr/bin/python

def main() :
        x = 5;
        y = 10;
        print('The value of x before swapping : {}'.format(x));
        print('The value of y before swapping : {}'.format(y));

        temp =  x;
        x = y;
        y = temp;

        print('The value of x after swapping : {}'.format(x));
        print('The value of y after swapping: {}'.format(y));

if __name__ == '__main__':
        main()
