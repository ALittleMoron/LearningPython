import os, os.path
import random

# [x for x in a if not x.startswith('.') and not x.startswith('__')]

def mkranddir() -> str:
    """return random maked dir with folders and text files"""
    pass


def tree(path:str, avoid_sys_dirs:bool, level=1) -> None:
    """walk through path and draw tree"""
    # validation of args
    if not path or type(path) is not str or not os.path.exists(path):
        print('==================================================================',\
              '\n= Something went wrong, so I override path to default: C:\\python =',\
              '\n==================================================================', sep ='')
        path = 'C:\\python'
    if type(avoid_sys_dirs) is not bool:
        avoid_sys_dirs = True
    
    # main part
    path = os.path.normpath(path)
    if avoid_sys_dirs == True:
        for item in [x for x in os.listdir(path) if not x.startswith('.') and not x.startswith('__')]:
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