from chuck_a_luck import ChuckALuckGame


def play_terminal():
    """Запуск игры в терминале"""
    game = ChuckALuckGame()

    # Заголовок как в BASIC
    print(" " * 22 + "CHUCK-A-LUCK")
    print(" " * 19 + "CREATIVE COMPUTING")
    print(" " * 17 + "MORRISTOWN, NEW JERSEY")
    print()
    print()
    print()
    print("CHOOSE A NUMBER FROM 1 TO 6. I WILL ROLL 3 DICE.")
    print("IF YOUR NUMBER MATCHES 1 DIE, I PAY OFF EVEN MONEY.")
    print("TWO DICE, 2:1    3 DICE, 3:1")
    print()
    print()

    while not game.is_game_over():
        print(f"YOU HAVE ${game.get_money()}. MAKE A BET.")

        # Ввод ставки
        while True:
            bet_input = input().strip()
            success, message = game.make_bet(bet_input)
            if success:
                break
            print(message)

        print("CHOOSE A NUMBER", end="")

        # Ввод числа
        while True:
            num_input = input().strip()
            success, message = game.choose_number(num_input)
            if success:
                break
            print(message)
            print("CHOOSE A NUMBER", end="")

        # Бросок и вывод результатов
        result = game.roll_dice()
        print(game.get_dice_output())
        print(f"YOU'VE MATCHED {game.matches} TIMES.")
        print(result)

        if not game.is_game_over():
            print()


if __name__ == "__main__":
    play_terminal()