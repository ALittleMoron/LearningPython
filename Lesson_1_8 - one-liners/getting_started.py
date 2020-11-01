"""
По заветам Питоновского Дзена "Простое лучше, чем сложное".
А что может быть проще фунции, написанной в 1 строчку с одним return'ом?
Конечно, далеко не всегда можно писать в таком стиле, но тех возможносте,
которые дает Python, на 99% хватает для повседневного программирования.
"""

# Блок работы с числами:
def list_of_numbers(range_num: int) -> list:
    # самый просто способ создать список от 0 до range_num
    return [x for x in range(range_num+1)]


def list_of_odd_numbers(range_num):
    # та же функция, что выше, но с условным оператором
    return [x for x in range(range_num+1) if x % 2]


if __name__ == "__main__":
    print(list_of_numbers(5), list_of_odd_numbers(5))