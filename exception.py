# try:
#     number = int(input("정수입력"))
#     print('원의 반지름', number)
#     print('원의 둘레', 2 * 3.14 * number)
#     print('원의 넓이', 3.14 * number * number)
# except Exception as exception:
#     if type(exception) == ValueError:
#         print('값에 문제가있습니다.')
while True:
    try:
        a=[274,233,12,43,65,100]
        number = int(input('정수입력(0~4까지)'))
        print(a[number])
        break
    except Exception as exception:
        # print(type(exception))
        if type(exception) == ValueError:
            print('값에 문제가있습니다.')
        elif type(exception) == IndexError:
            print('0~4까지 입력해주세요')