# unittest 모듈을 사용한 테스트 코드
# chat gpt
import unittest
import decimal_to_hex as dh

class TestDecimalToHex(unittest.TestCase):
    def test_decimal_to_hex(self):
        test_cases = [
            # 양수 테스트 케이스
            (0, "0"),
            (10, "A"),
            (255, "FF"),
            (4096, "1000"),
            (16777215, "FFFFFF"),

            # 음수 테스트 케이스
            (-1, "FFFFFFFF"),
            (-10, "FFFFFFF6"),
            (-255, "FFFFFE01"),
            (-4096, "FFFFF000"),
            (-16777215, "FF000001"),
        ]

        for num, hex_num in test_cases:
            self.assertEqual(decimal_to_hex(num), hex_num)

if __name__ == '__main__':
    unittest.main()
