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




#!usr/bin/python

def main() :
        num1 = 10;
        num2 = 14;
        num3 = 12;

        if(num1>num2) and (num1>num3) :
                largest = num1;
        elif (num2>num1) and (num2>num3):
                largest = num2;
        else:
                largest = num3;
        print 'The largest number between',num1,num2,num3,'is',largest

if __name__ == '__main__' :
        main();



#!usr/bin/python

def factorial(n):
        if n == 1:
                return n;
        else:
                return n*factorial(n-1);

def main() :
        num = int(input("Enter a number: "));
        if num < 0:
                print"Sorry, factorial does not exist for negative numbers";
        elif num == 0:
                print"The factorial of 0 is 1";
        else:
                print'The factorial of',num,'is',factorial(num);

if __name__ == '__main__' :
        main();





#!usr/bin/python

def main() :
        prima = 1;
        num = int(input("Enter a number: "));
        if num > 2:
                for i in range(2,num):
                        if (num % i) == 0:
                                i = num+4;
                                prima = 0;
                if prima == 1:
                        print num,"is a prime number";
                else:
                        print num,"is not a prime number";
        elif num == 2:
                print num,"is a prime number";
        else:
                print num,"is not a prime number";

if __name__ == '__main__' :
        main();
