from progressbar import progressbar
from time import sleep


if __name__ == "__main__":
    for i in progressbar(range(100)):
        sleep(0.01)
    for i in progressbar(range(100), redirect_stdout=True):
        print('Some text', i)
        sleep(0.1)
