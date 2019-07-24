# your code goes here
n=int(input())
rev=0
temp=n
while temp>0:
	rem=temp%10
	rev=(rev*10)+rem
	temp=temp//10
if n==rev:
	print("yes")
else:
	print("no")
