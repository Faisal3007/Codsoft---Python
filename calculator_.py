def add(a,b):
	res = a+b
	return res


def sub(a,b):
	res = a-b
	return res
	

def mul(a,b):
	res = a*b
	return res
	

def div(a,b):
	res = a/b
	return res

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
op = input("Which operation you want to perform: ")
if op == '+' or op == '1':
	print("Result =",add(a,b))
elif op == '-' or op == '2':
	print("Result =",sub(a,b))
elif op == '*' or op == '3':
	print("Result =",mul(a,b))
elif op == '/' or op == '4':
	print("Result =",div(a,b))
else:
	print("Invalid choice")	