import bs4 as bs
from urllib.request import Request, urlopen
import pandas as pd
import os
import re
import sys
website = 'https://www.thecarconnection.com'
template = 'https://images.hgmsites.net/'


def fetch(page, addition=''):
    return bs.BeautifulSoup(urlopen(Request(page + addition,
                            headers={'User-Agent': 'Opera/9.80 (X11; Linux i686; Ub'
                                     'untu/14.10) Presto/2.12.388 Version/12.16'})).read(),
                                     'lxml')


def all_makes():
    all_makes_list = []
    for a in fetch(website, "/new-cars").find_all("a", {"class": "add-zip"}):
        all_makes_list.append(a['href'])
    return all_makes_list


def make_menu(listed):
    make_menu_list = []
    for make in listed[1:3]: # REMOVE REMOVE REMOVE REMOVE REMOVE
        for div in fetch(website, make).find_all("div", {"class": "name"}):
            make_menu_list.append(div.find_all("a")[0]['href'])
    return make_menu_list


def model_menu(listed):
    model_menu_list = []
    for make in listed:
        soup = fetch(website, make)
        for div in soup.find_all("a", {"class": "btn avail-now first-item"}):
            model_menu_list.append(div['href'])
        for div in soup.find_all("a", {"class": "btn 1"})[:8]:
            model_menu_list.append(div['href'])
    model_menu_list = [i.replace('overview', 'specifications') for i in model_menu_list]
    return model_menu_list


def specs_and_pics(listed):
    picture_tab = [i.replace('specifications', 'photos') for i in listed]
    specifications_table = pd.DataFrame()
    for row, pic in zip(listed, picture_tab):
        soup = fetch(website, row)
        specifications_df = pd.DataFrame(columns=[soup.find_all("title")[0].text[:-15]])

        try:
            specifications_df.loc['Make', :] = soup.find_all('a', {'id': 'a_bc_1'})[0].text.strip()
            specifications_df.loc['Model', :] = soup.find_all('a', {'id': 'a_bc_2'})[0].text.strip()
            specifications_df.loc['Year', :] = soup.find_all('a', {'id': 'a_bc_3'})[0].text.strip()
            specifications_df.loc['MSRP', :] = soup.find_all('span', {'class': 'msrp'})[0].text
        except:
            print('Problem with {}.'.format(website + row))

        for div in soup.find_all("div", {"class": "specs-set-item"}):
            row_name = div.find_all("span")[0].text
            row_value = div.find_all("span")[1].text
            specifications_df.loc[row_name] = row_value

        fetch_pics_url = str(fetch(website, pic))

        try:
            for ix, photo in enumerate(re.findall('sml.+?_s.jpg', fetch_pics_url)[:150], 1):
                specifications_df.loc[f'Picture {ix}', :] = photo.replace('\\', '')
            specifications_table = pd.concat([specifications_table, specifications_df], axis=1, sort=False)
        except:
            print('Error with {}.'.format(template + photo))
    return specifications_table


def run(directory):
    os.chdir(directory)
    a = all_makes()
    b = make_menu(a)
    c = model_menu(b)
    pd.DataFrame(c).to_csv('c.csv', header=None)
    d = pd.read_csv('c.csv', index_col=0, header=None).values.ravel()
    e = specs_and_pics(d)
    e.to_csv('specs-and-pics.csv')


if __name__ == '__main__':
    if not os.path.isdir(sys.argv[1]):
        os.mkdir(sys.argv[1])

    print('%s started running.' % os.path.basename(__file__))
    run(sys.argv[1])
    print('%s finished running.' % os.path.basename(__file__))
