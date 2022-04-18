import os
import asyncio
import time
import threading
from datetime import datetime

COEF = 0.1


async def dish(num, prepare, wait):
    print(f"Начинаем готовить блюдо №{num} в {datetime.now().strftime('%H:%M:%S')} - "
          f"будем выполнять {prepare} минут(ы).")
    time.sleep(COEF * prepare)  # синхронно - повар занят
    print(f"Начинаем в {datetime.now().strftime('%H:%M:%S')} ждать пока блюдо №{num} приготовится - "
          f"будем ждать {wait} минут(ы).")
    await asyncio.sleep(COEF * wait)  # асинхронный вызов
    print(f"Закончили в {datetime.now().strftime('%H:%M:%S')} готовить блюдо №{num}.\n")


async def main():
    await asyncio.gather(asyncio.create_task(dish(1, 2, 3)),
                         asyncio.create_task(dish(2, 5, 10)),
                         asyncio.create_task(dish(3, 3, 5)))


if __name__ == "__main__":
    t0 = time.time()
    asyncio.run(main())
    delta = int((time.time() - t0) / COEF)
    print(f"Всё готово в {datetime.now().strftime('%H:%M:%S')}. Всего потрачено {delta}.")

