# 10진수가 주어졌을 때 그 수를 16진수로 변환하는 함수
# chat gpt가 작성하고, 최적화해줌

def decimal_to_hex(decimal_num):
    # 16진수에서 사용되는 문자
    hex_digits = ("0", "1", "2", "3", "4", "5", "6", "7",
                  "8", "9", "A", "B", "C", "D", "E", "F")

    # 10진수가 0인 경우
    if decimal_num == 0:
        return "0"

    hex_num = ""
    # 10진수가 양수인 경우
    if decimal_num > 0:
        for i in range(8):
            decimal_num, remainder = divmod(decimal_num, 16)
            hex_num = hex_digits[remainder] + hex_num
            if decimal_num == 0:
                break
        return hex_num

    # 10진수가 음수인 경우
    decimal_num = 4294967296 + decimal_num
    for i in range(8):
        decimal_num, remainder = divmod(decimal_num, 16)
        hex_num = hex_digits[remainder] + hex_num
        if decimal_num == 0:
            break
    return "-" + hex_num
