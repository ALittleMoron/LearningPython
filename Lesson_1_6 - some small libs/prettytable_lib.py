from prettytable import PrettyTable


if __name__ == "__main__":
    table = PrettyTable()
    table.add_column('food name', ['cake','meat', 'spagetti'])
    table.add_column('calories', [2700, 1200, 900])
    table.add_column('price', [2000.25, 570.0, 55.50])
    print(table)
