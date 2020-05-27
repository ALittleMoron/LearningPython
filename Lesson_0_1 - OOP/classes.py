# модуль с расписанными классами.
# Родительский класс "Государство". Желательно не создавать экземпляры этого класса и работать с дочерними.
class State():
    _count = 0 # число всех государств. ВНИМАНИЕ! НЕ ПЕРЕОПРЕДЕЛЯТЬ ПОЛЕ! ОНО УВЕЛИЧИВАЕТСЯ НА 1 С КАЖДЫМ НОВЫМ ЭКЗЕМПЛЯРОМ ДОЧЕРНЕГО КЛАССА
    item = []
    def __init__(self, name, population, size, gdp):
        State._count += 1
        self.name = name
        self.population = population
        self.size = size
        self.gdp = gdp
        State.item.append(self)

    def __str__(self):
        return f"""Государство {self.name} с численностью населения в {self.population} человек,
площадью {self.size} млн. кв. км. и объему Валового внутреннего продукта в {self.gdp} трл. $."""


# Дочерний класс "Республика" от класса "Государство".
class Republic(State):
    _count = 0
    item = []
    _FORM = 'Республика' # форма правления. ВНИМАНИЕ! НЕ ИЗМЕНЯТЬ! КОНСТАНТА!
    def __init__(self, name:str, population:int, size:float, gdp:float, president_name:str, next_president_name:str, parlament_members:int):
        Republic._count += 1
        super().__init__(name, population, size, gdp)
        self.president_name = president_name
        self.next_president_name = next_president_name
        self.parlament_members = parlament_members
        Republic.item.append(self)

    def __str__(self):
        return f"""Государство {self.name} с численностью населения в {self.population} человек,
площадью {self.size} млн. кв. км. и объему Валового внутреннего продукта в {self.gdp} трл. $,
Имя президента - {self.president_name}, имя след. президента - {self.next_president_name}, 
кол-во членов парламента - {self.parlament_members}."""
    

# Дочерний класс "Монархия" от класса "Государство".
class Monarchy(State):
    _count = 0
    item = []
    _FORM = 'Монархия' # форма правления. ВНИМАНИЕ! НЕ ИЗМЕНЯТЬ! КОНСТАНТА!
    def __init__(self, name:str, population:int, size:float, gdp:float, monarch_name:str, next_monarch_name:str, council_members:int):
        Monarchy._count += 1
        super().__init__(name, population, size, gdp)
        self.monarch_name = monarch_name
        self.next_monarch_name = next_monarch_name
        self.council_members = council_members
        Monarchy.item.append(self)
    
    def __str__(self):
        return f"""Государство {self.name} с численностью населения в {self.population} человек,
площадью {self.size} млн. кв. км. и объему Валового внутреннего продукта в {self.gdp} трл. $,
Имя монарха - {self.monarch_name}, имя след. монарха - {self.next_monarch_name},
кол-во советников - {self.council_members}."""


# Дочерний класс "Королевство" от класса "Государство".
class Kingdom(State):
    _count = 0
    item = []
    _FORM = 'Королевство' # форма правления. ВНИМАНИЕ! НЕ ИЗМЕНЯТЬ! КОНСТАНТА!
    def __init__(self, name:str, population:int, size:float, gdp:float, king_name:str, next_king_name:str, council_members:int):
        Kingdom._count += 1
        super().__init__(name, population, size, gdp)
        self.king_name = king_name
        self.next_king_name = next_king_name
        self.council_members = council_members
        Kingdom.item.append(self)

    def __str__(self):
        return f"""Государство {self.name} с численностью населения в {self.population} человек,
площадью {self.size} млн. кв. км. и объему Валового внутреннего продукта в {self.gdp} трл. $,
Имя короля - {self.king_name}, имя след. короля - {self.next_king_name}, кол-во советников - {self.council_members}"""


def main():
    '''Тест какашками'''

if __name__ == "__main__":
    main()