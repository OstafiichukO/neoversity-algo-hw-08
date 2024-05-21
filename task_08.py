# my cable mess in heap

import heapq

def merge_cables(cables):
    """
    Функція для об'єднання кабелів в оптимальному порядку.

    Args:
        cables: Список довжин кабелів.

    Returns:
        Список довжин об'єднаних кабелів.
    """

    # Створення купи з довжин кабелів
    heapq.heapify(cables)

    total = 0

    # Об'єднання кабелів, поки не залишиться один кабель
    while len(cables) > 1:
        # Вилучення двох кабелів з найменшою довжиною
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        # Додавання об'єднаного кабелю до купи
        merged_cable = cable1 + cable2
        heapq.heappush(cables, merged_cable)

        # Додавання вартості цього об'єднання до загальних витрат
        total += merged_cable

        # Виведення інформації про об'єднання
        print(f"Об'єднання кабелів: {cable1} + {cable2} = {merged_cable}")

    return total


def main():
    # Введення даних
    cables = [int(x) for x in input("Введіть Integer довжини кабелів через пробіл: ").split()]

    # Об'єднання кабелів
    total = merge_cables(cables)

    # Виведення результату
    print(f"Загальні витрати: {total}")


if __name__ == "__main__":
    main()
