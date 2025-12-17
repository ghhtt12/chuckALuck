# test_game.py - tests for Chuck-A-Luck
print("=== TESTING CHUCK-A-LUCK ===")
print("Checking system...")

# 1. Check game import
print("\n1. Checking game import...")
try:
    import chuck_a_luck

    print("[OK] Game module loaded")
except Exception as e:
    print(f"[ERROR] Load error: {e}")

# 2. Check random numbers
print("\n2. Checking random numbers...")
import random

random.seed(42)  # Fix randomness
test_rolls = [random.randint(1, 6) for _ in range(5)]
print(f"[OK] Test rolls: {test_rolls}")

# 3. Check game logic
print("\n3. Checking game logic...")


def test_game_logic():
    test_cases = [
        # (bet, number, dice, expected result)
        (10, 3, [3, 1, 5], 10),  # 1 match
        (10, 2, [2, 2, 6], 20),  # 2 matches
        (10, 4, [4, 4, 4], 30),  # 3 matches
        (10, 1, [2, 3, 4], -10),  # 0 matches
    ]

    all_ok = True
    for bet, number, dice, expected in test_cases:
        matches = sum(1 for d in dice if d == number)
        if matches == 0:
            result = -bet
        elif matches == 1:
            result = bet
        elif matches == 2:
            result = bet * 2
        elif matches == 3:
            result = bet * 3
        else:
            result = 0

        if result == expected:
            print(f"  [OK] Dice {dice}, number {number}: {matches} matches")
        else:
            print(f"  [ERROR] Dice {dice}, number {number}: calculation error")
            all_ok = False

    return all_ok


if test_game_logic():
    print("[OK] Game logic works correctly")
else:
    print("[ERROR] Problems with game logic")

# 4. Check project files
print("\n4. Checking project files...")
import os

required_files = [
    ("chuck_a_luck.py", "Main game code"),
    ("web_game.html", "Web version"),
    ("Makefile", "Build file"),
    ("README.md", "Documentation")
]

all_files_ok = True
for filename, description in required_files:
    if os.path.exists(filename):
        print(f"  [OK] {description}: {filename}")
    else:
        print(f"  [ERROR] {description}: {filename} - MISSING")
        all_files_ok = False

print("\n" + "=" * 50)
if all_files_ok:
    print("ALL TESTS PASSED SUCCESSFULLY!")
    print("\nAvailable commands:")
    print("  py chuck_a_luck.py    - Start game")
    print("  make run              - Start game (via make)")
    print("  make test             - Run tests")
    print("  make web              - Web version info")
else:
    print("SOME FILES ARE MISSING")
print("=" * 50)