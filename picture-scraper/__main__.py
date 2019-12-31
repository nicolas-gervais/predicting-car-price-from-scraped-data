import os
path = 'c:/users/nicolas/documents/data/thecarconnection/picturescraper/'

os.chdir(path)

directory = 'c:/users/nicolas/desktop/scrap/'

files = ['scrape', 'tag', 'save', 'select']

if __name__ == '__main__':
    if not os.path.isdir(directory):
        os.mkdir(directory)

    [os.system('python ' + path + f'{file}.py ' + directory) for file in files]
