# 자음 : c
# 모음 : v

alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_dict = {ch: "vowel" if ch in "aeiou" else "cons" for ch in alphabet}

while True:
    test = input().strip()
    if test == "end":
        break
    
    has_vowel = False  # 모음 포함 여부
    consecutive_count = 1  # 연속된 글자 수 체크
    is_acceptable = True  # 기본값을 true로 두고 조건에서 불만족 시 False로 전환

    for i in range(len(test)):
        # 1. 모음 포함 여부
        if test[i] in "aeiou":
            has_vowel = True

        # 2. 같은 글자 연속 (단, ee나 oo는 허용)
        if i > 0 and test[i] == test[i - 1] and test[i] not in "eo":
            is_acceptable = False
            break

        # 3. 모음/자음이 3개 연속
        if i > 0 and alpha_dict[test[i]] == alpha_dict[test[i - 1]]:
            consecutive_count += 1
            if consecutive_count == 3:
                is_acceptable = False
                break
        else:
            consecutive_count = 1

    # 모음이 하나도 없는 경우
    if not has_vowel:
        is_acceptable = False

    # 결과 출력
    if is_acceptable:
        print(f"<{test}> is acceptable.")
    else:
        print(f"<{test}> is not acceptable.")
