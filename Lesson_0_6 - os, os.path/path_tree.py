import os, os.path
from random import randint, random


def mkranddir(place:str, deep:int, num:int) -> None:
    """Make path to random maked dir with folders and text files, return None
    
    Keyword arguments:
    place -- path to place, where dir will be made (default C:\\Users\\dimal\\Desctop\\test)
    deep -- number of levels, which program will run to make dirs (default 1)
    num -- number of folders+files on every deep level (default 5)
    """
    
    # validation of args
    if not place or type(place) is not str or not os.path.exists(place):
        print('===================================================================',\
            '\n= Something went wrong, so I override place to default: C:\\python =',\
            '\n===================================================================\n\n', sep ='')
        place = 'C:\\python\\test'
    if not deep or type(deep) is not int or deep < 1:
        deep = 1
    if not num or type(num) is not int or num < 1:
        num = 5
    if deep == 5:
        return

    # main part
    place = os.path.normpath(place)
    file_or_folder = [randint(0,1) for _ in range(num)]
    for fof in file_or_folder:
        try:
            if deep == 1:
                if fof:
                    os.mkdir(place+'\\'+f'{randint(100, 262717)}{randint(100, 262717)}')
                else:
                    with open(place+'\\'+f'{randint(100, 262717)}{randint(100, 262717)}.txt', 'w') as f:
                        f.write(place+'\\'+f'{randint(100, 262717)}{randint(100, 262717)}')
            elif deep > 1:
                if fof:
                    os.mkdir(place+'\\'+f'{randint(100, 262717)}{randint(100, 262717)}')
                else:
                    continue
            else:
                return
        except (FileNotFoundError, NotADirectoryError):
            continue
    for ls in os.listdir(place):
        mkranddir(place+'\\'+ls, deep+1, num)


def tree(path:str, avoid_sys_dirs:bool, level=1) -> None:
    """walk through path and draw tree, return None
    
    Keyword arguments:
    path -- place, which will be drew (default C:\\python)
    avoid_sys_dirs -- will ignore folders, starting with __ or . or $ (default True)
    level -- show the depth of recursion in function and is used for print (default 1)
    """
    
    # validation of args
    if not path or type(path) is not str or not os.path.exists(path):
        print('==================================================================',\
              '\n= Something went wrong, so I override path to default: C:\\python =',\
              '\n==================================================================\n\n', sep ='')
        path = 'C:\\python'
    if not avoid_sys_dirs or type(avoid_sys_dirs) is not bool:
        avoid_sys_dirs = True
    if level < 1 or type(level) is not int:
        level = 1

    # main part
    path = os.path.normpath(path)
    if avoid_sys_dirs == True:
        for item in [x for x in os.listdir(path) if not x.startswith('.') and not x.startswith('__') and not x.startswith('$')]:
            if os.path.isdir(path+'\\'+item):
                if level == 1:
                    print('-'*(level-1), item, ':', sep='')
                if level > 1:
                    print('  '*(level-1), '|-', item, sep='')
                tree(path+'\\'+item, True, level+1)
            elif os.path.isfile(path+'\\'+item):
                print('  '*level, '|--', item, sep='')
            else:
                print('  '*level, '|--'*level, '<underfind file>', sep='')
    else:
        for item in os.listdir(path):
            if os.path.isdir(path+'\\'+item):
                if level == 1:
                    print('-'*(level-1), item, ':', sep='')
                if level > 1:
                    print('  '*(level-1), '|-', item, ':', sep='')
                tree(path+'\\'+item, True, level+1)
            elif os.path.isfile(path+'\\'+item):
                print('  '*level, '|--', item, sep='')
            else:
                print('  '*level, '|--'*level, '<underfind file>', sep='')


if __name__ == "__main__":
    tree('C:\\python\\test', True, 1)
