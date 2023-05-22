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
    
    num1 = int(input("������ ����� �����: "))
    num2 = int(input("������ ����� �����: "))

    gcd = find_gcd(num1, num2)
    print("��������� ������� ������:", gcd)
 
    lcm = find_lcm(num1, num2)
    print("�������� ������ ������:", lcm)

    return f"��������� ������� ������: {gcd}, �������� ������ ������: {lcm}"


def point2d():
    x1 = float(input("������ x1: "))
    y1 = float(input("������ y1: "))
    x2 = float(input("������ x2: "))
    y2 = float(input("������ y2: "))
    return f"��������� d = {math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}"


def square():
    def fibonacci(n):
        if n <= 0:
            raise ValueError("N ������� ���� ������� ������.")
        if n == 1:
            return 0
        elif n == 2:
            return 1
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        return fib_seq[-1]

    n = int(input("������ �������� N: "))

    fib_num = fibonacci(n)
    return f"N-�� ����� Գ�������: {fib_num}"


def sincos():
    x = float(input("������ �������� x: "))
    sin_x = math.sin(x)
    cos_x = math.cos(x)

    print("sin(x) =", sin_x)
    print("cos(x) =", cos_x)

    return f"{sin_x} - {cos_x}"


def point():
    x1 = float(input("������ ���������� ������� x1: "))
    y1 = float(input("������ ���������� ������� y1: "))
    x2 = float(input("������ ���������� ������� x2: "))
    y2 = float(input("������ ���������� ������� y2: "))
    t = ((x1 - x2) * (y2 - y1)) / ((y2 - y1) ** 2 + (x2 - x1) ** 2)
    x = x1 + t * (x2 - x1)
    y = y1 + t * (y2 - y1)

    return ('���������� ����� ��������: (' + str(x) + ',' + str(y) + ')')


def boil():
    v1 = float(input("������ q1: "))
    v2 = float(input("������ q2: "))
    p2 = float(input("������ r: "))

    return f"��������� P1 = {p2 * v2 / v1}"

def stala():
    
    planck_constant_joules = 6.62607015e-34
    planck_constant_eV = 4.135667696e-15

    print("�������� ����� ������ � ������� �� �������:", planck_constant_joules)
    print("�������� ����� ������ � ��������-������� �� �������:", planck_constant_eV)


def mountains():
    return ("5 �������� �� ���� �� - 1)�������(8848) "
            "2)���������(6962) "
            "3)�����(6168) "
            "4)ʳ���������(5892) "
            "5)�������(5642)")


def azimyt():
    def calculate_azimuth(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1

        azimuth_rad = math.atan2(dy, dx)
        azimuth_deg = math.degrees(azimuth_rad)

        if azimuth_deg < 0:
            azimuth_deg += 360

        return azimuth_deg

    x1 = float(input("������ ���������� x1 ��� ����� �: "))
    y1 = float(input("������ ���������� y1 ��� ����� �: "))
    x2 = float(input("������ ���������� x2 ��� ����� �: "))
    y2 = float(input("������ ���������� y2 ��� ����� �: "))

    azimuth = calculate_azimuth(x1, y1, x2, y2)

    print("������ �� ����� � �� ����� �:", azimuth)


def space():
    input_filename = input("������ ��'� �������� �����: ")
    output_filename = input("������ ��'� ��������� �����: ")

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        processed_content = ' '.join(content.split())

        with open(output_filename, 'w') as output_file:
            output_file.write(processed_content)

        return f"��������� ��� ��������� � ���� {output_filename}"
    except FileNotFoundError:
        return "�������: ���� �� ��������."
    except:
        return "�������: ������� ������� ��� ������� �����."


def words():
    def count_words(text):
        words = text.split()
        return len(words)

    file_path = "����_��_�����.txt"

    try:

        with open(file_path, 'r') as file:

            file_content = file.read()
            word_count = count_words(file_content)


        return f"ʳ������ ������ � �����: {word_count}"
    except FileNotFoundError:
        return "�������: ���� �� ��������."
    except:
        return "�������: ������� ������� ��� ������� �����."


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
            season = "����"
        elif (month == 3 and day >= 20) or (month >= 4 and month <= 5) or (month == 6 and day < 21):
            season = "�����"
        elif (month == 6 and day >= 21) or (month >= 7 and month <= 8) or (month == 9 and day < 23):
            season = "˳��"
        else:
            season = "����"

        return season


    current_season = get_current_season()
    print("������� ���� ����:", current_season)


def yeardays():
    year = int(input("������ ��: "))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days = 366
    else:
        days = 365

    return ("ʳ������ ��� � ����" + str(year) + "���������" + str(days) + "���.")


def name():
    return ("�������.")

def game():
    import random

    def determine_winner(player_choice, computer_choice):
        if player_choice == computer_choice:
            return "ͳ���"
        elif (player_choice == "�����" and computer_choice == "������") or \
                (player_choice == "������" and computer_choice == "����") or \
                (player_choice == "����" and computer_choice == "�����"):
            return "�� �������!"
        else:
            return "����'���� ������!"

    def play_game():
        choices = ["�����", "������", "����"]
        computer_choice = random.choice(choices)

        print("��� '�����-������-����' ����� ����'�����")
        print("��� ����:")
        print("1. �����")
        print("2. ������")
        print("3. ����")

        while True:
            player_choice = input("������ ����� ������ ������ (1-3): ")

            if player_choice in ["1", "2", "3"]:
                player_choice = choices[int(player_choice) - 1]
                break
            else:
                print("����������� ����. ��������� �� ���.")

        print("��� ����:", player_choice)
        print("���� ����'�����:", computer_choice)

        winner = determine_winner(player_choice, computer_choice)
        print(winner)


    play_game()


def books():
    import random

    def recommend_book():
        books = [
            "ҳ� ������� ������",
            "�����",
            "�������� ��'�",
            "̳���",
            "������",
            "T���� �����",
        ]

        recommended_book = random.choice(books)
        return recommended_book


    book = recommend_book()
    print("������������� �����:", book)


def bay():
    return ("�������� ������ ���� - ����������� ������.")


def library():
    return (" ���������� �������� - �������� �������� ���� .")


class Bot:
    def __init__(self, mountain=None):
        self.f = ''
        self.branch = ''
        self.branches = {
            '����������': { '������ ��������� ������� ������ ��� �������� ������ ������ ���� �����': arc,
                           '���������� ������� ������ �� ����� ������� �� ������': point2d,
                           '�-�� ����� Գ�������': square,
                           'sin(x) �� cos(x)': sincos,
                           '���������� ����� �������� ���� ������': point},
            '������': {'����� �����-�������': boil,
                       '����� ������': stala},
            '���������': {'5 �������� �� � ��� �� ��� ������.': mountains,
                          '������ �� ����� � (x1, y1) �� ����� � (x2, y2), ���� ���� �� ����������.': azimyt,
                          },
            '������ � �������': {'������� ����� ��� ������ ������': space,
                                 'ϳ��������� ������� ��� � �����': words,
                                 '������ �� �����, �� ����������� � ����.': digit ,
                                 },
            '��������': {'��� ����� ���� ����?': season,
                         '���������� ��� � ����': yeardays,
                         '�� ���� �����?': name,
                         '�����-������-����': game,
                         '��� ������� ���� � ���?': mountain,
                         '��� ����� �� ��� �������������?': books,
                         '��� �������� ������ ����?': bay,
                         '��� ������� �������� � ���?': library}
        }

    def start(self):
        while True:
            printBot(
                "�� ������ ������ ��� ������� � ��������� �������: ����������, ������, ���������, ������ � �������, ��������.")
            writetofile(
                "�� ������ ������ ��� ������� � ��������� �������: ����������, ������, ���������, ������ � �������, ��������.",
                self.f)
            theme = input().lower()
            writetofile(theme, self.f)
            if theme.lower() == '�����':
                printBot("�� ���������")
                writetofile("�� ���������", self.f)
                exit()
            elif theme.lower() == '��������':
                printBot(
                    "�� ��������� ���� �����. ��� ������� ������ �� �� �������� ��������� �����������. ���������!\n")
                writetofile(
                    "�� ��������� ���� �����. ��� ������� ������ �� �� �������� ��������� �����������. ���������!\n",
                    self.f)
            elif theme.lower() == '�����':
                printBot("ͳ���� �����������. �� �������� ����. ��� ������ �������� �����\n")
                writetofile("ͳ���� �����������. �� �������� ����. ��� ������ �������� �����\n", self.f)
            else:
                if theme in self.branches.keys():
                    self.branch = theme
                    break
                else:
                    printBot("�������, � �� ���� ���� �����! ��������� �� ��� �� ������.")
                    writetofile("�������, � �� ���� ���� �����! ��������� �� ��� �� ������.", self.f)
        self.themes()

    def hi(self):
        printBot("�����, ���� ����� �������.")
        writetofile("�����, ���� ����� �������.", self.f)
        self.start()

    def themes(self):
        while True:
            printBot("\n�� ������ ������ <" + self.branch + ">. �� ������ ������ ��� ������� � ��������� ���:")
            writetofile("\n�� ������ ������ <" + self.branch + ">. �� ������ ������ ��� ������� � ��������� ���:",
                        self.f)
            for text in self.branches[self.branch].keys():
                printBot("\t" + text)
                writetofile("\t" + text, self.f)
            theme = input()
            writetofile(theme, self.f)
            if theme.lower() == "�����":
                printBot("�� ���������\n")
                writetofile("�� ���������\n", self.f)
                exit()
            elif theme.lower() == "��������":
                printBot(
                    "�� ������ ������ <" + self.branch + ">. ��� ������� ������ ���� �� �������� ��������� �����������. ������� ���� �����!\n")
                writetofile(
                    "�� ������ ������ <" + self.branch + ">. ��� ������� ������ ���� �� �������� ��������� �����������. ������� ���� �����!\n",
                    self.f)
            elif theme.lower() == "�����":
                self.start()
            else:
                if theme in self.branches[self.branch].keys():
                    temp = self.branches[self.branch][theme]()
                    printBot(temp)
                    writetofile(temp, self.f)
                else:
                    printBot("�������, � �� ���� ���� ����! ��������� �� ��� �� ������.")
                    writetofile("�������, � �� ���� ���� ����! ��������� �� ��� �� ������.", self.f)


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

