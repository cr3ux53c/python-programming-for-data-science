import random
answer = random.randint(1,10)
def guess_number(answer):
    try:
        guess = int(input("숫자를 넣어 주세요: "))
        if answer == guess:
            print("정답!")
        else:
            print("틀렸습니다.")
    except ValueError:
        print("숫자가 아닙니다.")

guess_number(answer)
