# get two integer parameters
# retrun sum
def plus(x, y):
	return x+y
def minus(x, y):
	retrun x-y
def mul(x, y):
	return x*y
def div(x, y)
	return x/y

# main function
def main():
	check = 1
	print("Welcome to calcuator")
	while check >= 1:
	print("0" exit, 1: plus, 2:minus, 3:multiply, 4:divide")
	try:
		check = int(input())
	except ValueError:
		print("숫자를 입력하세요.")
	if (check > 4):
		print("Unsupported")
	elif (check == 1 or 2 or 3 or 4):
		print("First Number")
		x = float(input())
		print("Second Number")
		y = float(input())
		if check == 1:
			print("answer : ", plus(x, y))
		elif check == 2:
			print("answer : ". minus(x, y))
		elif check == 3:
			print("answer : ", mul(x,y))
		elif check == 4:
			if y == 0:
				print("0으로 나눌 수 없습니다.")
			else:
				print("answer : ", div(x, y))

if __name__ == "__main__":
	main()
