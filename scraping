import bs4 as bs
from urllib.request import Request, urlopen
import pandas as pd

website = "https://www.thecarconnection.com"

def fetch(hostname, filename):
    return bs.BeautifulSoup(urlopen(Request(hostname + filename, headers={'User-Agent': 'X'})).read(), 'lxml')

def all_makes():
    all_makes_list = []
    for a in fetch(website, "/new-cars").find_all("a", {"class": "add-zip"}):
        all_makes_list.append(a['href'])
    return all_makes_list

def make_menu():
    make_menu_list = []
    for make in all_makes():
        for div in fetch(website, make).find_all("div", {"class": "name"}):
            make_menu_list.append(div.find_all("a")[0]['href'])
    return make_menu_list

def model_menu():
    model_menu_list = []
    for make in make_menu():
        soup = fetch(website, make)
        for div in soup.find_all("a", {"class": "btn avail-now first-item"}):
            model_menu_list.append(div['href'])
        for div in soup.find_all("a", {"class": "btn 1"}): 
            model_menu_list.append(div['href'])
    return model_menu_list

def year_model_overview():
    year_model_overview_list = []
    for make in model_menu():
        for id in fetch(website, make).find_all("a", {"id": "ymm-nav-specs-btn"}):
            year_model_overview().append(id['href'])
    year_model_overview_list.remove("/specifications/buick_enclave_2019_fwd-4dr-preferred")
    return year_model_overview_list

def trims():
    trim_list = []
    for row in year_model_overview():
        div = fetch(website, row).find_all("div", {"class": "block-inner"})[-1]
        div_a = div.find_all("a")
        for i in range(len(div_a)):
            trim_list.append(div_a[-i]['href'])
    return trim_list

pd.DataFrame(trims()).to_csv(<REDACTED>, index=False, header=None)
trims = pd.read_csv(<REDACTED>)

def specifications():
    specifications_table = pd.DataFrame()
    for row in trims.iloc[:, 0]:
        soup = fetch(website, row)
        specifications_df = pd.DataFrame(columns=[soup.find_all("title")[0].text[:-15]])
        msrp_text = soup.find_all("div", {"class": "price"})[0]
        if len(msrp_text.find_all("a")) >= 1:
            specifications_df.loc["MSRP"] = msrp_text.find_all("a")[0].text
        for div in soup.find_all("div", {"class": "specs-set-item"}):
            row_name = div.find_all("span")[0].text
            row_value = div.find_all("span")[1].text
            specifications_df.loc[row_name] = row_value
        specifications_table = pd.concat([specifications_table, specifications_df], axis=1, sort=False)
    return specifications_table

specifications().to_csv(<REDACTED>)
