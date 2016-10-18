#!/usr/bin/python

def rek(lo,up,n,num):
	mid = ((up - lo) / 2) + lo;
	if lo >= up or up <= lo :
		return -1;
	elif n == num[mid] :
		return mid;
	elif n > num[mid] :
		lo = mid + 1;
		hasil = rek(lo,up,n,num);
	else :
		up = mid - 1;
		hasil = rek(lo,up,n,num);
	return hasil;

def main():
	arr = [1,2,3,4,5];
	panjang = len(arr);
	n = input("Masukkan input : ");
	hasil = rek(0,panjang,n,arr);
	if hasil == -1 :
		print "Angka yang dicari tidak ada";
	else :
		print "Angka", n, "ada di index", hasil;

if __name__ == '__main__' :
	main();
