a = float(input("Enter first number: "))

b = float(input("Enter second number: "))

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

op = input("Which operation you want to perform: ")

if op == '+' or op == '1':
	res = a+b
	print("Result =",res)
	
elif op == '-' or op == '2':
	res = a-b
	print("Result =",res)
	
elif op == '*' or op == '3':
	res = a*b
	print("Result =",res)
	
elif op == '/' or op == '4':
	res = a/b
	print("Result =",res)
	
else:
	print("Invalid choice")