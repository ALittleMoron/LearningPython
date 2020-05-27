# Учу ООП, а конретно, dunder методы.
import classes as cl

def main():
    republic_list, monarchy_list, kingdom_list = [], [], []
    while True:
        first_menu_sel = int(input("\nЧто вы хотите, чтобы я сделал:\n1. Создал экземпляр класса.\n2. Удалил экземпляр класса.\n3. Вывел список экземпляров классов.\n4. Вышел из программы.\n"))
        print("\n")
        if first_menu_sel == 1:
            second_menu_sel = int(input("Экземпляр какого класса мне создать:\n1. Республику.\n2. Монархию.\n3. Королевство.\n"))
            if second_menu_sel == 1:
                republic_list.append(cl.Republic(str(input("Введите название: ")), int(input("Введите число жителей: ")), float(input("размер в млн. кв. км.: ")), float(input("трлн. $: ")), str(input("Имя президента: ")), str(input("Имя след. президента: ")), int(input("число членов парламента: ")) ))
                print("\n")
            elif second_menu_sel == 2:
                monarchy_list.append(cl.Monarchy(str(input("Введите название: ")), int(input("Введите число жителей: ")), float(input("размер в млн. кв. км.: ")), float(input("трлн. $: ")), str(input("Имя президента: ")), str(input("Имя след. президента: ")), int(input("число членов парламента: ")) ))
                print("\n")
            elif second_menu_sel == 3:
                kingdom_list.append(cl.Kingdom(str(input("Введите название: ")), int(input("Введите число жителей: ")), float(input("размер в млн. кв. км.: ")), float(input("трлн. $: ")), str(input("Имя президента: ")), str(input("Имя след. президента: ")), int(input("число членов парламента: ")) ))
                print("\n")
            else:
                print("вы что-то накосячили. Выключаю программу!")
                break
        
        elif first_menu_sel == 2:
            third_menu_sel = int(input("Какое государство вы хотите удалить:\n1. Республику.\n2. Монархию.\n3. Королевство.\n"))
            if third_menu_sel == 1:
                for i in range(len(republic_list)):
                    print(f"{i+1}: {cl.Republic.item[i]}")
                print("\n")
                pop_sel = int(input("Какое из этих государств вы хотите удалить? "))
                republic_list.pop(pop_sel-1)
                print(f"Республика {pop_sel} была удалена.\n")
            if third_menu_sel == 2:
                for j in range(len(monarchy_list)):
                    print(f"{j+1}: {cl.Monarchy.item[j]}")
                print("\n")
                pop_sel = int(input("Какое из этих государств вы хотите удалить? "))
                monarchy_list.pop(pop_sel-1)
                print(f"Монархия {pop_sel} была удалена.\n")
            if third_menu_sel == 3:
                for k in range(len(kingdom_list)):
                    print(f"{k+1}: {cl.Kingdom.item[k]}")
                print("\n")
                pop_sel = int(input("Какое из этих государств вы хотите удалить? "))
                republic_list.pop(pop_sel-1)
                print(f"Королевство {pop_sel} была удалена.\n")
        elif first_menu_sel == 3:
            print("Республики:")
            for i in range(len(republic_list)):
                print(f"{i+1}: {cl.Republic.item[i]}")
            print("\nМонархии:")
            for j in range(len(monarchy_list)):
                print(f"{j+1}: {cl.Monarchy.item[j]}")
            print("\nКоролевства:")
            for k in range(len(kingdom_list)):
                print(f"{k+1}: {cl.Kingdom.item[k]}")
        elif first_menu_sel == 4:
            break
        else:
            print("вы что-то накосячили. Выключаю программу!")
            break



if __name__ == "__main__":
    main()