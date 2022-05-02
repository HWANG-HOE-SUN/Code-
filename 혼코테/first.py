# 문제 1
# 문제 풀이: Lv1.숫자
# 문자열과 영단어
# 1478 → “one4seveneight”
# 234567 → “23
# four5six7”
# 10203 → “1
# zerotwozero3”
#
# 네오와 프로도가
# 위와 같이 숫자를 문자열로
# 바꾸는 게임을 하고있습니다.이때 일부 자릿수가 영단어로 바뀌었거나
# 바뀌지 않고 그대로인 문자열 s가
# 매개변수로 주어질 때, s가 의미하는 원래 숫자를 return 하는 함수를 완성해주세요.
#
# 제한사항 1 ≤ s의 길이 ≤ 50 s가 “zero” 또는 “0”으로
# 시작하는 경우는 주어지지 않습니다.
# return 값이 1이상 2, 000, 000, 000
# 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

# 입출력 예 s
# result
# "one4seveneight"
# 1478
# "23four5six7"
# 234567
# "2three45sixseven"
# 234567
# "123"
# 123

def solve_one(s):
    alpha_dict = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }
    result = []
    for i in s:
        temp = []
        if type(i)!=int:
            temp.append(i)
        if ''.join(temp) in alpha_dict:
            result.append(alpha_dict[''.join(temp)])
        elif type(i)==int:
            result.append(i)
    print(f"{result}")

    # Use a breakpoint in the code line below to debug your script.
if __name__ == '__main__':
    solve_one('one2three4')
