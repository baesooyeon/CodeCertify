expression = input()
# 빼기 기호로 식을 분할
terms = expression.split('-')
# 첫 번째 항목은 덧셈으로 합치고 나머지는 빼기
result = sum(map(int, terms[0].split('+')))
for term in terms[1:]:
    result -= sum(map(int, term.split('+')))
print(result)
