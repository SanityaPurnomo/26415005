#!/usr/bin/python

import csv

jumlah =[]
file = open('hasil.txt', 'rb')
data = csv.reader(file, delimiter=',')
table = [row for row in data]

z = 1
jumlah = 0

for a in range(5,269) :
	for b in a.len :
		print table[a][b]
