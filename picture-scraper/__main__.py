import os
path = 'c:/users/nicolas/documents/data/thecarconnection/picturescraper/'

os.chdir(path)

directory = 'c:/users/nicolas/desktop/scrap/'
py = 'python '


if __name__ == '__main__':
    os.system(py + path + 'scrape.py ' + directory)
    os.system(py + path + 'tag.py ' + directory)
    os.system(py + path + 'save.py ' + directory)
    os.system(py + path + 'select.py ' + directory)
