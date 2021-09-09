# 사용자로부터 숫자를 입력받아 그 숫자의 크기 만큼 "*"출력하기

number_input = input("숫자를 입력해주세요 : ")

user_input_number = int(number_input)

for i in range(1,user_input_number+1):
    print(i*"*")
    print("와우 정말 대단한걸~! 따봉!")
    print("복습 재밌다..정말...")