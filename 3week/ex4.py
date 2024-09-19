i = 0
a = int(input("수를 입력하세요"))

if 0 < a < 10:
    for i in range(1, 10):
        print(f"{a} X {i} = {a*i}")
else:
    print("1~9 사이의 수를 입력해주세요")