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

    # Об'єднання кабелів, поки не залишиться один кабель
    while len(cables) > 1:
        # Вилучення двох кабелів з найменшою довжиною
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        # Додавання об'єднаного кабелю до купи
        heapq.heappush(cables, cable1 + cable2)
    
        # Виведення інформації про об'єднання
        print(f"Об'єднання кабелів: {cable1} + {cable2} = {cable1 + cable2}")

    return cables


def main():
    # Введення даних
    cables = [int(x) for x in input("Введіть Integer довжини кабелів через пробіл: ").split()]

    # Об'єднання кабелів
    merged_cables = merge_cables(cables)

    # Виведення результату
    print(f"Список довжин об'єднаних кабелів: {merged_cables}")

    # Розрахунок загальних витрат
    #total_cost = sum(cables)
    total_cost = sum(merged_cables)
    
    print(f"Загальні витрати: {total_cost}")


if (__name__ == "__main__") or (__name__ == "__hw_08__"):
    main()
    