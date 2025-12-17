import random
import sys

def play_chuck_a_luck(start_money=500):
    money = start_money
    print(" " * 20 + "CHUCK-A-LUCK")
    print(" " * 18 + "CREATIVE COMPUTING")
    print(" " * 16 + "MORRISTOWN, NEW JERSEY\n")

    print("CHOOSE A NUMBER FROM 1 TO 6. I WILL ROLL 3 DICE.")
    print("IF YOUR NUMBER MATCHES 1 DIE, I PAY OFF EVEN MONEY.")
    print("TWO DICE, 2:1    3 DICE, 3:1\n")

    while money > 0:
        print(f"YOU HAVE ${money}. MAKE A BET.")
        try:
            bet = int(input())
        except ValueError:
            print("DON'T GET CUTE!!!")
            continue

        if bet > money:
            print("I DON'T TAKE I.O.U's !!!!")
            continue
        if bet <= 0 or bet * 100 != int(bet * 100):
            print("DON'T GET CUTE!!!")
            continue

        print("CHOOSE A NUMBER")
        try:
            number = int(input())
        except ValueError:
            print("CHEATER!!!!!")
            continue

        if not (1 <= number <= 6):
            print("CHEATER!!!!!")
            continue

        dice = [random.randint(1, 6) for _ in range(3)]
        print(f"{dice[0]}    {dice[1]}    {dice[2]}")

        matches = sum(1 for d in dice if d == number)
        print(f"YOU'VE MATCHED {matches} TIMES.")

        if matches == 0:
            print(f"YOU LOSE ${bet}")
            money -= bet
        elif matches == 1:
            print(f"YOU'VE WON ${bet}")
            money += bet
        elif matches == 2:
            print(f"YOU'VE WON ${bet * 2}")
            money += bet * 2
        elif matches == 3:
            print(f"YOU'VE WON ${bet * 3}")
            money += bet * 3

        if money <= 0:
            print("\nGAME OVER! YOU'RE BROKE!")
            break

if __name__ == "__main__":
    play_chuck_a_luck()