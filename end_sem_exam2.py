import operator as op 
list1 = [2, 7, 98, 44]
list2 = [99, 2, 24]
flag = 0
for elem in list2:
	if op.countOf(list1, elem) > 0:
		flag = 1
if flag ==1:
	print("True")
else:
	print("False")