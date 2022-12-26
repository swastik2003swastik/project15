a=int(input(">>>Enter the lower limit⏬: "))
b=int(input(">>>Enter the upper limit⏫: "))
d=0
e=0
#verifying given input are appropriate or not
if a>b:
	c=input("\nThe lower limit cannot be more than the upper limit😑 \nIf you wish to interchange the values type 'Yes'' else 'No': ").lower()
#doing corrections in input
	if c=="yes":
		temp=b
		b=a
		a=temp
#checking the conditions that given number is prime or not
for i in range(a,b+1):
	print()
	s=0
	if i==0:
		print("0 is neither prime nor composite")
		continue
	for j in range(1,i+1):
		if i%j==0:
			s+=1
	if s==2:
		print(i, "is a prime number")
		d=d+1
	else:
		print(i, "is a composite number")
		e=e+1
print(f"Count:{d} prime numbers and {e} composite numbers are there in the range")
