import time
from datetime import datetime

COEF = 1


def dish(num, prepare, wait):
    print(f"Начинаем готовить блюдо №{num} в {datetime.now().strftime('%H:%M:%S')} - "
          f"будем выполнять {prepare} минут(ы).")
    time.sleep(COEF * prepare)
    print(f"Начинаем в {datetime.now().strftime('%H:%M:%S')} ждать пока блюдо №{num} приготовится - "
          f"будем ждать {wait} минут(ы).")
    time.sleep(COEF * wait)
    print(f"Закончили в {datetime.now().strftime('%H:%M:%S')} готовить блюдо №{num}.\n")


def main():
    dish(1, 2, 3)
    dish(2, 5, 10)
    dish(3, 3, 5)


if __name__ == "__main__":
    t0 = time.time()
    main()
    delta = int((time.time() - t0) / COEF)
    print(f"Всё готово в {datetime.now().strftime('%H:%M:%S')}. Всего потрачено {delta}.")

