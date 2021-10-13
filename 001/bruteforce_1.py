import itertools

문자열 = '0123456789'  # 특수 문자는 없다고 가정한다

# https://docs.python.org/ko/3/library/itertools.html
# 2자리 비밀번호
# for i in 문자열:
#     for j in 문자열:
#         print(i, j)

# 3자리 비밀번호
# for i in 문자열:
#     for j in 문자열:
#         for k in 문자열:
#             print(i, j, k)

for 패스워드길이 in range(1, 5):  # 1 - 1~3에서 1~5까지 해볼 것
    for password in itertools.product(문자열, repeat=패스워드길이):
        print(password)  # 1
        print(''.join(password))
