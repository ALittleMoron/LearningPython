import sys


Nothing = None


def common_methods_and_other_from_sys_module() -> Nothing:
    """функция не делает ничего серьезного. Просто проверяю модуль sys"""
    print(sys.version)
    print(sys.argv) if len(sys.argv) > 1 else print('no')
    print(sys.getsizeof(common_methods_and_other_from_sys_module))
    print(sys.hash_info)
    print(sys.executable)
    print(sys.maxsize)
    print(sys.platform)
    print(sys.modules)

if __name__ == "__main__":
    common_methods_and_other_from_sys_module()
