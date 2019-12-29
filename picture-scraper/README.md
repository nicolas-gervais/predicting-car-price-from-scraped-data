# Car Picture Scraper
It scrapes 297,000 pictures, of which around 198,000 unique URLs. Many of these are interior images, which are useless. You should have around 60,000 pictures in the end. 

All labeled by:
- Make
- Model
- Year
- Price
- Horsepower
- Body style (pickup, convertible, 4dr car, etc)
- etc

Filename is tagged like this, separated by an underscore:

```
impt_cols = [
    'Make', 'Model', 'Year', 'MSRP', 'Front Wheel Size (in)', 'SAE Net Horsepower @ RPM',
    'Displacement', 'Engine Type', 'Width, Max w/o mirrors (in)', 'Height, Overall (in)',
    'Length, Overall (in)', 'Gas Mileage', 'Drivetrain', 'Passenger Capacity', 'Passenger Doors',
    'Body Style']
```
__There are 3 random characters in the end, to make a unique filename ID.__

Example:
```
Audi_A5_2013_43_18_210_20_4_73_54_182_24_FWD_4_2_Convertible_eUH.jpg
```
That's:
- Audi
- A5
- 2013 
- 43,000$
- 18" front wheel
- 210 horsepower
- 2.0 engine displacement
- 4 cylinder engine
- 73" width
- 54" height
- 182" length
- 24 mpg gas mileage
- Front wheel drive
- 4 passenger capacity
- 2 passenger doors
- random 3 character string
