# Welcome to _The Car Connection Picture Dataset :tm:_!
It scrapes 297,000 pictures, of which around 198,000 unique URLs. Many of these are interior images, which are useless. You should have around 60,000 pictures in the end. 

| Size | Download | Author | Source | Dependencies | 
| --- | --- | --- | --- | --- |
| 681 MB | [Link](https://drive.google.com/open?id=1TQQuT60bddyeGBVfwNOk6nxYavxQdZJD) | Nicolas Gervais | [The Car Connection](https://www.thecarconnection.com/) | `pandas`, `PIL`, `requests`, `bs4`, `urllib`, `numpy` |

<img src=https://user-images.githubusercontent.com/46652050/71590299-ebd23f00-2af5-11ea-916f-f19ff6fad04a.jpg height=150 align=center img>

All filenames are tagged like this, separated by an underscore:

```
'Make', 'Model', 'Year', 'MSRP', 'Front Wheel Size (in)', 'SAE Net Horsepower @ RPM',
'Displacement', 'Engine Type', 'Width, Max w/o mirrors (in)', 'Height, Overall (in)',
'Length, Overall (in)', 'Gas Mileage', 'Drivetrain', 'Passenger Capacity', 'Passenger Doors',
'Body Style'
```
__There are 3 random characters in the end, to make a unique filename ID.__

Example:
```
Audi_A5_2013_43_18_210_20_4_73_54_182_24_FWD_4_2_Convertible_eUH.jpg
```
| Spec Name  | Value |
| ------------- | ------------- |
| `Make`  | Audi  |
| `Model`  | A5  |
| `Year`  | 2013  |
| `MSRP`  | $43,000  |
| `Front Wheel Size`  | 18 inches  |
| `Horsepower`  | 210 hp |
| `Displacement`  | 2.0L  |
| `Engine Type`  | 4 cylinders  |
| `Width`  | 73 inches  |
| `Height`  | 54 inches  |
| `Length`  | 182 inches  |
| `Gas Mileage`  | 24 mpg  |
| `Drivetrain`  | Front wheel drive  |
| `Passenger Capacity`  | 4  |
| `Passenger Doors` | 2 |
| `Body Style` | Convertible |
| `Random String` | eUH |


> __WARNING:__ Many pics have duplicates, even though I removed duplicate URLs.

## HOW TO RUN
1. Copy all `.py` files into a folder. 
    - Make sure you have all the dependencies installed _and up to date_ (e.g., `bs4`, `requests`, etc).
2. In `main.py`, set `path` to where the files are, and `directory` where you want the images to land
    - You do not need to create the directory yourself
3. Run `main.py`. I suggest you try it with a portion of the data first, in case an error emerges later. 
    - For instance, in `scrape.py` line 27, replace `for make in listed:` to `for make in listed[1:3]:`

__EXAMPLE__. [Example — Audi vs BMW ConvNet.ipynb](https://github.com/nicolas-gervais/predicting-car-price-from-scraped-data/blob/master/picture-scraper/Example%20%E2%80%94%20Audi%20vs%20BMW%20ConvNet.ipynb): example of a deep learning classification task with `Pytorch`

> __WARNING:__ You may have issues if you use Python 3.6

## FAQ
1. How do I get the large pictures? 
    - In `scrape.py`, row 68, change this line:
    - `for ix, photo in enumerate(re.findall('sml.+?_s.jpg', fetch_pics_url)[:150], 1):`
    - to this line:
    - `for ix, photo in enumerate(re.findall('lrg.+?_l.jpg', fetch_pics_url)[:150], 1):`
    - You can use _sml_, _med_, _lrg_ for your preferred image size
    
## FILES
| FILES | DESCRIPTION | EXPORT | 
| ---   | ---         | --- |
| `scrape.py` | Creates a `df` of all cars with their specs/pics URLs | `specs-and-pics.csv` |  
| `tag.py` | Turns the previous `df` into one tag per URL | `id_and_pic_url.csv` | 
| `save.py` | Turns all rows in the previous `df` to a picture named with the tag | `pictures/*.jpg`  | 
| `select.py` | Uses `numpy` to delete interior pictures, based on pixel color | `exterior/*.jpg` |
| `main.py` | Runs all other files | `None` | 

## RELATED WORKS
1. [Classifying Cars in the TCC Dataset](https://github.com/AshivDhondea/ENSC813_report/blob/master/paper/ENSC_813_paper%20Ashiv%20Hans%20Dhondea.pdf) by [Ashiv Hans Dondea](https://github.com/AshivDhondea/ENSC813_report).
