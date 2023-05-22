# -*- coding: cp1251 -*-
import datetime
import math
import random

from colorama import init, Fore

init(autoreset=True)


def printBot(text):
    if text is not None:
        print(Fore.BLUE + text)


def writetofile(text, filename):
    with open(filename, 'a') as file:
        file.write(text + "\n")


def arc():
    def find_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def find_lcm(a, b):
        gcd = find_gcd(a, b)
        lcm = (a * b) // gcd
        return lcm
    
    num1 = int(input("Введіть перше число: "))
    num2 = int(input("Введіть друге число: "))

    gcd = find_gcd(num1, num2)
    print("Найбільший спільний дільник:", gcd)
 
    lcm = find_lcm(num1, num2)
    print("Найменше спільне кратне:", lcm)

    return f"Найбільший спільний дільник: {gcd}, Найменше спільне кратне: {lcm}"


def point2d():
    x1 = float(input("Введіть x1: "))
    y1 = float(input("Введіть y1: "))
    x2 = float(input("Введіть x2: "))
    y2 = float(input("Введіть y2: "))
    return f"Результат d = {math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}"


def square():
    def fibonacci(n):
        if n <= 0:
            raise ValueError("N повинно бути додатнім числом.")
        if n == 1:
            return 0
        elif n == 2:
            return 1
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        return fib_seq[-1]

    n = int(input("Введіть значення N: "))

    fib_num = fibonacci(n)
    return f"N-те число Фібоначчі: {fib_num}"


def sincos():
    x = float(input("Введіть значення x: "))
    sin_x = math.sin(x)
    cos_x = math.cos(x)

    print("sin(x) =", sin_x)
    print("cos(x) =", cos_x)

    return f"{sin_x} - {cos_x}"


def point():
    x1 = float(input("Введіть координату вектора x1: "))
    y1 = float(input("Введіть координату вектора y1: "))
    x2 = float(input("Введіть координату вектора x2: "))
    y2 = float(input("Введіть координату вектора y2: "))
    t = ((x1 - x2) * (y2 - y1)) / ((y2 - y1) ** 2 + (x2 - x1) ** 2)
    x = x1 + t * (x2 - x1)
    y = y1 + t * (y2 - y1)

    return ('Координати точки перетину: (' + str(x) + ',' + str(y) + ')')


def boil():
    v1 = float(input("Введіть q1: "))
    v2 = float(input("Введіть q2: "))
    p2 = float(input("Введіть r: "))

    return f"Результат P1 = {p2 * v2 / v1}"

def stala():
    
    planck_constant_joules = 6.62607015e-34
    planck_constant_eV = 4.135667696e-15

    print("Значення Сталої Планка в джоулях на секунду:", planck_constant_joules)
    print("Значення Сталої Планка в електрон-вольтах на секунду:", planck_constant_eV)


def mountains():
    return ("5 найвищих гір світу це - 1)Еверест(8848) "
            "2)Аконкагуа(6962) "
            "3)Деналі(6168) "
            "4)Кіліманджаро(5892) "
            "5)Ельбрус(5642)")


def azimyt():
    def calculate_azimuth(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1

        azimuth_rad = math.atan2(dy, dx)
        azimuth_deg = math.degrees(azimuth_rad)

        if azimuth_deg < 0:
            azimuth_deg += 360

        return azimuth_deg

    x1 = float(input("Введіть координату x1 для точки А: "))
    y1 = float(input("Введіть координату y1 для точки А: "))
    x2 = float(input("Введіть координату x2 для точки В: "))
    y2 = float(input("Введіть координату y2 для точки В: "))

    azimuth = calculate_azimuth(x1, y1, x2, y2)

    print("Азимут від точки А до точки В:", azimuth)


def space():
    input_filename = input("Введіть ім'я вхідного файлу: ")
    output_filename = input("Введіть ім'я вихідного файлу: ")

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        processed_content = ' '.join(content.split())

        with open(output_filename, 'w') as output_file:
            output_file.write(processed_content)

        return f"Результат був записаний у файл {output_filename}"
    except FileNotFoundError:
        return "Помилка: Файл не знайдено."
    except:
        return "Помилка: Виникла помилка при обробці файлу."


def words():
    def count_words(text):
        words = text.split()
        return len(words)

    file_path = "шлях_до_файлу.txt"

    try:

        with open(file_path, 'r') as file:

            file_content = file.read()
            word_count = count_words(file_content)


        return f"Кількість речень у тексті: {word_count}"
    except FileNotFoundError:
        return "Помилка: Файл не знайдено."
    except:
        return "Помилка: Виникла помилка при обробці файлу."


def digit():
    import re

    def find_digit_words(file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            digit_words = re.findall(r'\b\d+\b', text)
            return digit_words

    file_path = 'text.txt'
    result = find_digit_words(file_path)
    print(result)


def season():
    import datetime

    def get_current_season():
        now = datetime.datetime.now()
        month = now.month
        day = now.day

        if (month == 12 and day >= 21) or (month <= 2) or (month == 3 and day < 20):
            season = "Зима"
        elif (month == 3 and day >= 20) or (month >= 4 and month <= 5) or (month == 6 and day < 21):
            season = "Весна"
        elif (month == 6 and day >= 21) or (month >= 7 and month <= 8) or (month == 9 and day < 23):
            season = "Літо"
        else:
            season = "Осінь"

        return season


    current_season = get_current_season()
    print("Поточна пора року:", current_season)


def yeardays():
    year = int(input("Введіть рік: "))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days = 366
    else:
        days = 365

    return ("Кількість днів у році" + str(year) + "становить" + str(days) + "днів.")


def name():
    return ("Світлана.")

def game():
    import random

    def determine_winner(player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Нічия"
        elif (player_choice == "камінь" and computer_choice == "ножиці") or \
                (player_choice == "ножиці" and computer_choice == "папір") or \
                (player_choice == "папір" and computer_choice == "камінь"):
            return "Ви виграли!"
        else:
            return "Комп'ютер виграв!"

    def play_game():
        choices = ["камінь", "ножиці", "папір"]
        computer_choice = random.choice(choices)

        print("Гра 'камінь-ножиці-папір' проти комп'ютера")
        print("Ваш вибір:")
        print("1. Камінь")
        print("2. Ножиці")
        print("3. Папір")

        while True:
            player_choice = input("Введіть номер вашого вибору (1-3): ")

            if player_choice in ["1", "2", "3"]:
                player_choice = choices[int(player_choice) - 1]
                break
            else:
                print("Некоректний вибір. Спробуйте ще раз.")

        print("Ваш вибір:", player_choice)
        print("Вибір комп'ютера:", computer_choice)

        winner = determine_winner(player_choice, computer_choice)
        print(winner)


    play_game()


def books():
    import random

    def recommend_book():
        books = [
            "Тіні забутих предків",
            "Енеїда",
            "Кайдашеа сім'я",
            "Місто",
            "Кобзар",
            "Tанго смерті",
        ]

        recommended_book = random.choice(books)
        return recommended_book


    book = recommend_book()
    print("Рекомендована книга:", book)


def bay():
    return ("Найбільша затока світу - Бенгальська затока.")


def library():
    return (" Британська бібліотека - найбільша бібліотека світу .")


class Bot:
    def __init__(self, mountain=None):
        self.f = ''
        self.branch = ''
        self.branches = {
            'математика': { 'Знайти найбільший спільний дільник або найменше спільне кратне двох чисел': arc,
                           'Обчислення довжини відрізка між двома точками на площині': point2d,
                           'Н-те число Фібоначчі': square,
                           'sin(x) та cos(x)': sincos,
                           'Обчислення точки перетину двох прямих': point},
            'фізика': {'Закон Бойля-Маріотта': boil,
                       'Стала Планка': stala},
            'географія': {'5 найвищих гір в світі та їхні висоти.': mountains,
                          'Азимут від точки А (x1, y1) до точки В (x2, y2), якщо відомі їх координати.': azimyt,
                          },
            'робота з текстом': {'Вивести текст без зайвих пробілів': space,
                                 'Підрахувати кількість слів у тексті': words,
                                 'Знайти всі слова, які складаються з цифр.': digit ,
                                 },
            'загальна': {'Яка зараз пора року?': season,
                         'Обчислення днів у році': yeardays,
                         'Як тебе звати?': name,
                         'камінь-ножиці-папір': game,
                         'Яка найвища гора у світі?': mountain,
                         'Яку книгу ви мені порекомендуєте?': books,
                         'Яка найбільше затока світу?': bay,
                         'Яка найбільш бібліотека у світі?': library}
        }

    def start(self):
        while True:
            printBot(
                "Ви можете задати мені питання з наступних галузей: математика, фізика, географія, робота з текстом, загальна.")
            writetofile(
                "Ви можете задати мені питання з наступних галузей: математика, фізика, географія, робота з текстом, загальна.",
                self.f)
            theme = input().lower()
            writetofile(theme, self.f)
            if theme.lower() == 'вихід':
                printBot("До побачення")
                writetofile("До побачення", self.f)
                exit()
            elif theme.lower() == 'допомога':
                printBot(
                    "Ви розпочали вибір галузі. Вам потрібно обрати її та слідувати наступним інструкціям. Спробуйте!\n")
                writetofile(
                    "Ви розпочали вибір галузі. Вам потрібно обрати її та слідувати наступним інструкціям. Спробуйте!\n",
                    self.f)
            elif theme.lower() == 'назад':
                printBot("Нікуди повертатись. Це стартове меню. Для виходу напишіть вихід\n")
                writetofile("Нікуди повертатись. Це стартове меню. Для виходу напишіть вихід\n", self.f)
            else:
                if theme in self.branches.keys():
                    self.branch = theme
                    break
                else:
                    printBot("Помилка, я не знаю цієї галузі! Спробуйте ще раз її ввести.")
                    writetofile("Помилка, я не знаю цієї галузі! Спробуйте ще раз її ввести.", self.f)
        self.themes()

    def hi(self):
        printBot("Привіт, мене звати Світлана.")
        writetofile("Привіт, мене звати Світлана.", self.f)
        self.start()

    def themes(self):
        while True:
            printBot("\nВи обрали галузь <" + self.branch + ">. Ви можете задати мені питання з наступних тем:")
            writetofile("\nВи обрали галузь <" + self.branch + ">. Ви можете задати мені питання з наступних тем:",
                        self.f)
            for text in self.branches[self.branch].keys():
                printBot("\t" + text)
                writetofile("\t" + text, self.f)
            theme = input()
            writetofile(theme, self.f)
            if theme.lower() == "вихід":
                printBot("До побачення\n")
                writetofile("До побачення\n", self.f)
                exit()
            elif theme.lower() == "допомога":
                printBot(
                    "Ви обрали галузь <" + self.branch + ">. Вам потрібно обрати тему та слідувати наступним інструкціям. Вводьте тему чітко!\n")
                writetofile(
                    "Ви обрали галузь <" + self.branch + ">. Вам потрібно обрати тему та слідувати наступним інструкціям. Вводьте тему чітко!\n",
                    self.f)
            elif theme.lower() == "назад":
                self.start()
            else:
                if theme in self.branches[self.branch].keys():
                    temp = self.branches[self.branch][theme]()
                    printBot(temp)
                    writetofile(temp, self.f)
                else:
                    printBot("Помилка, я не знаю цієї теми! Спробуйте ще раз її ввести.")
                    writetofile("Помилка, я не знаю цієї теми! Спробуйте ще раз її ввести.", self.f)


def main():
    """

    :rtype: object
    """
    b = datetime.datetime.now()
    date = b.strftime("%d-%m-%Y %H-%M-%S")

    bot = Bot()
    bot.f = 'dialog-' + date + '.txt'
    bot.hi()

if __name__ == '__main__':
    main()

