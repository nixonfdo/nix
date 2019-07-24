# your code goes here
x=int(input())
if(x>0):
	for i in range(1,x):
		if x%2==0:
			print("no")
			break
	else:
		print("yes")
else:
	print("no")
