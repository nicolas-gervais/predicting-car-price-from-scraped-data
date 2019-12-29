# Car Picture Scraper
It scrapes 297,000 pictures, of which around 198,000 unique URLs. Many of these are interior images, which are useless. You should have around 60,000 pictures in the end. 

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


> <font color='red'>__WARNING:__</font> Many pics have duplicates. 

### HOW TO RUN
1. [image-scraper](https://github.com/nicolas-gervais/predicting-car-price-from-scraped-data/blob/master/picture-scraper/image-scraper): scrapes all specifications and pictures

.2 [id-and-pic-url](https://github.com/nicolas-gervais/predicting-car-price-from-scraped-data/blob/master/picture-scraper/id-and-picture-url): from the previous `csv`, turns it into just a picture url and id tag

3. [image-saver](https://github.com/nicolas-gervais/predicting-car-price-from-scraped-data/blob/master/picture-scraper/image-saver): turns all picture links in a picture, labeled

4. [interior-exterior-dispatcher](https://github.com/nicolas-gervais/predicting-car-price-from-scraped-data/blob/master/picture-scraper/interior-exterior-dispatcher): sends the pictures _unlikely_ to be interior to a new folder
You might have to manage your own directories.
