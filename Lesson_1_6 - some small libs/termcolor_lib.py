from termcolor import colored, cprint


if __name__ == "__main__":
    print(colored('Это все, для чего нужна эта библиотека...', 'cyan', ))
    cprint('А ещё можно вот так писать, так даже читабельнее...', 'red',
                                                                  'on_white')
    cprint('Вернее, не читабельно в консоли, но читабельно в коде', 'yellow',
                                                            attrs=['underline'])
    for i in ['white', 'green', 'yellow', 'red', 'cyan']:
        cprint('а ещё можно так!', i)
