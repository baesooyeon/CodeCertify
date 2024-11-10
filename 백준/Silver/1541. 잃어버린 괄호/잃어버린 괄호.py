expression = input()
exp_list = expression.split("-")

min_result = sum(map(int, exp_list[0].split("+")))

for idx in range(1, len(exp_list)):
    min_result -=sum(map(int, exp_list[idx].split("+")))
print(min_result)