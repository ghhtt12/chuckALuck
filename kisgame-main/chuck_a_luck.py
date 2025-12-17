import random


class ChuckALuckGame:
    """Основная логика игры, независимая от интерфейса"""

    def __init__(self, start_money=500):
        self.money = start_money
        self.bet = 0
        self.number = 0
        self.dice = []
        self.matches = 0
        self.game_over = False

    def make_bet(self, bet_amount):
        """Проверка и установка ставки"""
        try:
            bet = float(bet_amount)
        except ValueError:
            return False, "DON'T GET CUTE!!!"

        if bet > self.money:
            return False, "I DON'T TAKE I.O.U's !!!!"
        if bet <= 0 or bet * 100 != int(bet * 100):
            return False, "DON'T GET CUTE!!!"

        self.bet = bet
        return True, ""

    def choose_number(self, number):
        """Проверка и установка числа"""
        try:
            num = float(number)
        except ValueError:
            return False, "CHEATER'!!!!!"

        if int(num) != num or num < 1 or num > 6:
            return False, "CHEATER'!!!!!"

        self.number = int(num)
        return True, ""

    def roll_dice(self):
        """Бросок кубиков и подсчет результатов"""
        # Случайные кубики как в BASIC
        a = random.randint(1, 6)
        d = random.randint(1, 6)
        c = random.randint(1, 6)
        self.dice = [a, d, c]

        # Подсчет совпадений
        self.matches = 0
        if a == self.number:
            self.matches += 1
        if d == self.number:
            self.matches += 1
        if c == self.number:
            self.matches += 1

        # Вычисление выигрыша/проигрыша
        if self.matches == 0:
            self.money -= self.bet
            result = f"YOU LOOSE ${int(self.bet)}"
        elif self.matches == 1:
            self.money += self.bet
            result = f"YOU'VE WON ${int(self.bet)}"
        elif self.matches == 2:
            self.money += self.bet * 2
            result = f"YOU'VE WON ${int(self.bet * 2)}"
        elif self.matches == 3:
            self.money += self.bet * 3
            result = f"YOU'VE WON ${int(self.bet * 3)}"

        # Проверка конца игры
        if self.money <= 0:
            self.game_over = True
            result += "\n\nGAME OVER"

        return result

    def get_dice_output(self):
        """Форматирование вывода кубиков как в BASIC"""
        if self.dice:
            return f"{self.dice[0]}    {self.dice[1]}    {self.dice[2]}     "
        return ""

    def get_money(self):
        return self.money

    def is_game_over(self):
        return self.game_over

    def reset(self):
        """Сброс игры"""
        self.__init__()