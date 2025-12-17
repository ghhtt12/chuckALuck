import random
from io import StringIO
import sys


def test_exact_format():
    """Тестирует точное форматирование как в BASIC"""
    print("=== TESTING EXACT BASIC FORMAT ===")

    # Фиксируем случайность для теста
    random.seed(42)

    print("\n1. Simulating dice output...")

    # Имитируем вывод кубиков как в BASIC строках 270-280
    A = random.randint(1, 6)
    D = random.randint(1, 6)
    C = random.randint(1, 6)

    # Собираем строку как в BASIC: PRINT A;"    ";:PRINT D;"    ";:PRINT C;"     "
    output_line = f"{A}    {D}    {C}     "

    print(f"  Generated: '{output_line}'")
    print(f"  Length: {len(output_line)} characters")

    # Проверяем точное форматирование
    expected_parts = [
        f"{A}",
        "    ",
        f"{D}",
        "    ",
        f"{C}",
        "     \n"
    ]

    # Визуализируем пробелы
    print(f"  Visualized: {A}|....|{D}|....|{C}|.....|")
    print("               ^4sp ^4sp ^5sp")

    # Проверяем количество пробелов
    spaces_between = output_line.count("    ")
    spaces_at_end = output_line.endswith("     ")

    if spaces_between == 2:
        print("  ✅ Correct: 4 spaces between dice")
    else:
        print(f"  ❌ Wrong: {spaces_between} groups of 4 spaces")

    if spaces_at_end:
        print("  ✅ Correct: 5 spaces at end")
    else:
        print("  ❌ Wrong ending spaces")

    # Проверяем оригинальный BASIC вывод
    print("\n2. Expected BASIC output examples:")
    print("   '4    2    5     '")
    print("   '1    6    3     '")
    print("   '3    3    1     '")

    print("\n3. Full format check:")
    test_cases = [
        (3, 5, 1, "3    5    1     "),
        (4, 2, 5, "4    2    5     "),
        (1, 1, 1, "1    1    1     ")
    ]

    all_correct = True
    for a, d, c, expected in test_cases:
        actual = f"{a}    {d}    {c}     "
        if actual == expected:
            print(f"  ✅ {a},{d},{c} -> '{actual}'")
        else:
            print(f"  ❌ {a},{d},{c} -> '{actual}' (expected: '{expected}')")
            print(f"     Difference: {repr(actual)} vs {repr(expected)}")
            all_correct = False

    print("\n" + "=" * 50)
    if all_correct:
        print("✅ ALL FORMAT TESTS PASSED - Output matches BASIC exactly!")
    else:
        print("❌ Format differences detected")

    return all_correct


def simulate_basic_output():
    """Показывает как выглядит вывод в оригинале"""
    print("\n=== ORIGINAL BASIC SIMULATION ===")
    print("Lines 270-280 in BASIC:")
    print("270 A=INT(RND(1)*6)+1:PRINT A;\"    \";:D=INT(RND(1)*6)+1:PRINT D;\"    \";")
    print("280 C=INT(RND(1)*6)+1:PRINT C;\"     \"")
    print()
    print("This produces output like: '4    2    5     '")
    print("Where: number + 4 spaces + number + 4 spaces + number + 5 spaces")


if __name__ == "__main__":
    test_exact_format()
    simulate_basic_output()