import os, os.path
from random import randint, random

# [x for x in a if not x.startswith('.') and not x.startswith('__')]

def mkranddir(place:str, deep:int) -> str:
    """return path to random maked dir with folders and text files
    
    Keyword arguments:
    place -- path to place, where dir will be made (default C:\\Users\\dimal\\Desctop)
    deep -- number of levels, which program will run to make dirs (default 2)
    """
    
    # validation of args
    if not place or type(place) is not str or not os.path.exists(place):
        print('===================================================================',\
            '\n= Something went wrong, so I override place to default: C:\\python =',\
            '\n===================================================================\n\n', sep ='')
        place = 'C:\\Users\\dimal\\Desctop'
    if not deep or type(deep) is not int:
        deep = 2

    # main part
    place = os.path.normpath(place)
    for dp in deep:
        pass


def tree(path:str, avoid_sys_dirs:bool, level=1) -> None:
    """walk through path and draw tree
    
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
    path = 'C:\\python'
    tree(path, True)
else:
    raise Exception("Use file like a program, not module. WIP.")