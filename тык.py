import sys
import time

def animateMessage(message, typingDelay=0.1, eraseDelay=0.05, pause=1.3):
    for ch in message:
        print(ch, end='', flush=True)
        time.sleep(typingDelay)
    time.sleep(pause)
    for _ in message:
        print('\b \b', end='', flush=True)
        time.sleep(eraseDelay)
    print()

def singSong():
    lines = [
        "Now, it's three in the mornin'",
        "And I'm tryna' change your mind",
        "Left you multiple missed calls",
        "And to my message, you reply",
        "Why'd you only call me when you're high?",
        "Hi, why'd you only call me when you're high?",
    ]

    delays = [0.2, 0.2, 0.3, 1.2, 1.3, 1]

    for line, delay in zip(lines, delays):
        for ch in line:
            print(ch, end='', flush=True)
            time.sleep(0.07)
        print()
        time.sleep(delay)


if __name__ == "__main__":
    title = "<3"
    animateMessage(title)
    singSong()
    print("\n❤️ КІНЕЦЬ ❤️")
    input("\nНатисни Enter, щоб закрити...")
