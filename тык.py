from time import sleep
import sys


def printSong():
    """
    Виводить текст пісні з ефектом "друкарської машинки" та паузами.
    """

    # Повідомлення, яке ви просили додати
    dedication_message = "присвячується любімій Машці<3"
    print(dedication_message)
    # Додамо невелику паузу перед початком пісні для кращого сприйняття
    sleep(1.5)

    # Структура: (рядок, затримка між символами)
    lines_data = [
        ("Now, it's three in the mornin'", 0.04),
        ("And I'm tryna' change your mind", 0.045),
        ("Left you multiple missed calls", 0.045),
        ("And to my message, you reply", 0.045),
        ("Why'd you only call me when you're high?", 0.045),
        ("Hi, why'd you only call me when you're high?", 0.045),
    ]

    # Паузи після кожного рядка
    line_delays = [0.2, 0.2, 0.3, 1.2, 1.3, 1]

    for i, (line, char_delay) in enumerate(lines_data):
        # Виведення кожного символу з невеликою затримкою (ефект друкарської машинки)
        for char in line:
            # Використовуємо sys.stdout.write та sys.stdout.flush
            # для виведення символів без автоматичного переведення рядка
            # та для негайного відображення
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(char_delay)

        # Перехід на новий рядок після повного виведення фрази
        print()

        # Пауза після рядка
        if i < len(line_delays):
            sleep(line_delays[i])


if __name__ == "__main__":
    printSong()