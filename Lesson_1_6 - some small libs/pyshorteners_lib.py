from pyshorteners import Shortener


if __name__ == "__main__":
    # Это по большей части всё, что нужно от этой библиотеки.
    # Она просто сокращает ссылки. Не очень полезно, но да ладно
    url = Shortener()
    short = url.tinyurl.short('www.google.com')
    print(short)
