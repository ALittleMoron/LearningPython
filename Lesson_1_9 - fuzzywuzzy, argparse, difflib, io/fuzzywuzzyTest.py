from fuzzywuzzy import process, fuzz


print(fuzz.ratio('hello world!', 'hello, world!'))  #96
print(fuzz.ratio('some random string', 'more randomed string, that not s1'))#63
print(fuzz.partial_ratio('batMAN', 'MAN')) #100
print(fuzz.token_sort_ratio('I am your father!', 'your father am I!'))#100

city = ["Москва",
        "Санкт-Петербург",
        "Саратов", "Краснодар",
        "Воронеж",
        "Омск",
        "Екатеринбург",
        "Орск",
        "Красногорск",
        "Красноярск",
        "Самара"]
print(process.extractOne("Краногрск", city))#90
