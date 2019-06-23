try:
    for i in range(1, 7):
        result = 7 // i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다.")
