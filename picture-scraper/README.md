# Car Picture Scraper
It scrapes 297,000 pictures, of which around 198,000 unique URLs. Many of these are interior images, which are useless. You should have around 60,000 pictures in the end. 

<img src=https://user-images.githubusercontent.com/46652050/71590299-ebd23f00-2af5-11ea-916f-f19ff6fad04a.jpg width=200 img>
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
Copy all `.py` files into a folder. Make sure you have all the dependencies installed _and up to date_ (e.g., `bs4`, `requests`, etc). Then run `main.py`. Try it with a portion of the data first because there seems to be a problem with `save.py`. 

__EXAMPLE__. [Example — Audi vs BMW ConvNet.ipynb](https://github.com/nicolas-gervais/predicting-car-price-from-scraped-data/blob/master/picture-scraper/Example%20%E2%80%94%20Audi%20vs%20BMW%20ConvNet.ipynb): example of a deep learning classification task with `Pytorch`

> __WARNING:__ You may have issues if you use Python 3.6
