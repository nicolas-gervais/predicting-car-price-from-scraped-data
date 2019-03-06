import pandas as pd
import numpy as np

raw_data = pd.read_csv("", nrows=110, index_col=0).transpose()

# -------- replace na and tbd with np nan

raw_data.replace("NA", np.nan)
raw_data = raw_data.replace("- TBD –", 'NA')
raw_data = raw_data.replace("- TBD -", 'NA')
raw_data['EPA Fuel Economy Est - City (MPG)'] = raw_data['EPA Fuel Economy Est - City (MPG)'].str.replace(r"\(.*\)","")
raw_data = raw_data.replace("NA", np.nan)

# -------- cols with forbidden charac

raw_data = raw_data.rename(columns=lambda x: x.split(" (ft")[0])
raw_data['Passenger Volume'] = raw_data['Passenger Volume'].str.replace(r"\(.*\)","")

# -------- Clean MSRP and convert to float

raw_data.MSRP = raw_data.MSRP.str.replace("$", "")
raw_data.MSRP = raw_data.MSRP.str.replace(",", "")

# -------- Clean basic miles and convert to float

raw_data['Basic Miles/km'] = raw_data['Basic Miles/km'].str.replace(",", "")
raw_data['Basic Miles/km'] = raw_data['Basic Miles/km'].str.replace("Unlimited", "150000")
raw_data['Basic Miles/km'] = raw_data['Basic Miles/km'].str.replace("49999", "50000")

# -------- Clean Drivetrain Miles and convert to float

raw_data['Drivetrain Miles/km'] = raw_data['Drivetrain Miles/km'].str.replace(",", "")
raw_data['Drivetrain Miles/km'] = raw_data['Drivetrain Miles/km'].str.replace("Unlimited", "150000")

# -------- get Roadside Assistance Miles/km miles  as integer

raw_data['Roadside Assistance Miles/km'] = raw_data['Roadside Assistance Miles/km'].str.replace(",", "")
raw_data['Roadside Assistance Miles/km'] = raw_data['Roadside Assistance Miles/km'].str.replace("Unlimited", "100000")

# -------- get number of gears

raw_data['Transmission'] = raw_data['Transmission'].str.lower()
raw_data['Gears'] = raw_data['Transmission'].str.split("-speed", expand=True, n = 1)[0].str[-2:].str.strip()
raw_data.Gears = raw_data['Gears'].str.replace("le", "1")
raw_data.Gears = raw_data['Gears'].str.replace("ed", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("ic", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("es", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("er", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("ls", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("ve", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("to", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("de", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("ch", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("ct", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("rs", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("ft", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("al", "NA")
raw_data.Gears = raw_data['Gears'].str.replace("s,", "NA")

# -------- get max horsepower

raw_data['Net Horsepower'] = raw_data['SAE Net Horsepower @ RPM'].str.split("@",expand=True)[0]
raw_data['Net Horsepower'] = raw_data['Net Horsepower'].astype(float)
raw_data.replace("NA", np.nan, inplace=True)

# -------- get max horsepower rpm

raw_data['Net Horsepower RPM'] = raw_data['SAE Net Horsepower @ RPM'].str.split("@",expand=True)[1].str.strip()
raw_data['Net Horsepower RPM'] = raw_data['Net Horsepower RPM'].str.replace("- TBD -", "NA")

# -------- get max torque

raw_data['Net Torque'] = raw_data['SAE Net Torque @ RPM'].str.split("@", expand=True)[0]
raw_data.replace("NA", np.nan, inplace=True)
raw_data['Net Torque'] = raw_data['Net Torque'].astype(float)

# -------- get max torque rpm

raw_data['Net Torque RPM'] = raw_data['SAE Net Torque @ RPM'].str.split().str.get(-1).str[-4:].str.strip()
raw_data['Net Torque RPM'] = raw_data['Net Torque RPM'].str.replace("- TBD -", "NA").str.replace('-', 'NA')
raw_data.replace("NA", np.nan, inplace=True)
raw_data['Net Torque RPM'] = raw_data['Net Torque RPM'].astype(float)
raw_data['Net Torque RPM'] = raw_data['Net Torque RPM'].clip(lower=1000)

# -------- number of cylinders

raw_data['Cylinders'] = raw_data['Engine Type'].str.split("-", expand=True)[1]
raw_data['Cylinders'] = raw_data['Cylinders'].str.replace("Cyl", "4")
raw_data['Cylinders'] = raw_data['Cylinders'].str.replace("in Electric I4", "4")

# -------- engine configuration

raw_data['Engine Configuration'] = raw_data['Engine Type'].str.split(" ").str.get(-1).str[0]
raw_data['Engine Configuration'] = raw_data['Engine Configuration'].str.replace("4", "NA")
raw_data['Engine Configuration'] = raw_data['Engine Configuration'].str.replace("T", "NA")
raw_data['Engine Configuration'] = raw_data['Engine Configuration'].str.replace("D", "NA")
raw_data['Engine Configuration'] = raw_data['Engine Configuration'].str.replace("G", "NA")

# -------- engine class

raw_data["Engine Class"] = raw_data["Engine Type"].str.split(' ').str.get(0)
raw_data["Engine Class"] = raw_data["Engine Class"].replace('Turbo', 'Turbocharged')
raw_data["Engine Class"] = raw_data["Engine Class"].replace('Electric/Gas', 'Electric')
raw_data["Engine Class"] = raw_data["Engine Class"].replace('Turbo/Supercharger', 'Supercharger')
raw_data["Engine Class"] = raw_data["Engine Class"].replace('Electric/Gas', 'Electric')
raw_data["Engine Class"] = raw_data["Engine Class"].replace('Supercharged', 'Supercharger')

# -------- displacement - liters

raw_data['Displacement (L)'] = raw_data['Displacement'].str.split("/", expand=True)[0].str[:3]
raw_data['Displacement (L)'] = raw_data['Displacement (L)'].str.replace('39.', '3.9')

# -------- displacement - cc

raw_data['Displacement (cc)'] = raw_data['Displacement'].str.split("/", expand=True)[1]
raw_data['Displacement (cc)'] = raw_data['Displacement (cc)'].str.replace('- TBD -', 'NA')
raw_data['Displacement (cc)'] = raw_data['Displacement (cc)'].str.replace('- TBD –', 'NA')
# raw_data.loc['2018 Buick Envision Specs: AWD 4-Door Essence':'2018 Buick Envision Specs: AWD 4-Door Preferred',
# "Displacement (cc)"] = 'NA'

# -------- get rear tire width

raw_data["Rear Tire Width"] = raw_data["Rear Tire Size"].str.split("/").str.get(0).str[-3:].str.strip()
raw_data["Rear Tire Width"] = raw_data["Rear Tire Width"].replace('R20', 'NA')
raw_data.replace("NA", np.nan, inplace=True)
raw_data["Rear Tire Width"] = raw_data["Rear Tire Width"].astype(float)

# -------- get front tire width

raw_data["Front Tire Width"] = raw_data["Front Tire Size"].str.split("/").str.get(0).str[-3:].str.strip()
raw_data["Front Tire Width"] = raw_data["Front Tire Width"].replace('R20', 'NA')
raw_data.replace("NA", np.nan, inplace=True)
raw_data["Front Tire Width"] = raw_data["Front Tire Width"].astype(float)

# -------- get rear wheel size

raw_data["Rear Wheel Size"] = raw_data["Rear Wheel Size (in)"].str[:2].astype(float)

# -------- get front wheel size

raw_data["Front Wheel Size"] = raw_data["Front Wheel Size (in)"].str[:2].astype(float)

# -------- get tire rating

raw_data["Tire Rating"] = raw_data["Front Tire Size"].str.split("/").str.get(-1).str[-4]
raw_data["Tire Rating"] = raw_data["Tire Rating"].replace('5', 'NA')
raw_data["Tire Rating"] = raw_data["Tire Rating"].replace('0', 'NA')
raw_data["Tire Rating"] = raw_data["Tire Rating"].replace('1', 'NA')
raw_data["Tire Rating"] = raw_data["Tire Rating"].replace('2', 'NA')

# -------- get width ratio

raw_data["Tire Width Ratio"] = raw_data["Rear Tire Width"]/raw_data["Front Tire Width"]

# -------- get size ratio

raw_data["Wheel Size Ratio"] = raw_data["Rear Wheel Size"] / raw_data["Front Wheel Size"]

# -------- get tire ratio

raw_data["Tire Ratio"] = raw_data["Front Tire Size"].str.split("/").str.get(1).str[0]
raw_data["Tire Ratio"] = raw_data["Tire Ratio"].replace('Y', 'NA')

# -------- get year

raw_data["Year"] = raw_data.index.str[:4].astype(float)

# -------- edit drivetrain values

raw_data['Drivetrain'] = raw_data['Drivetrain'].str.replace('4-Wheel Drive', 'Four Wheel Drive')
raw_data['Drivetrain'] = raw_data['Drivetrain'].str.replace('Front wheel drive', 'Front Wheel Drive')
raw_data['Drivetrain'] = raw_data['Drivetrain'].str.replace('Four-Wheel Drive', 'Four Wheel Drive')

# -------- edit fuel system values

raw_data['Fuel System'] = raw_data['Fuel System'].str.replace('Turbocharged EFI', 'Electronic Fuel Injection')
raw_data['Fuel System'] = raw_data['Fuel System'].str.replace('Electric', 'Electronic Fuel Injection')
raw_data['Fuel System'] = raw_data['Fuel System'].str.replace('Sequential MPI (injection)', 'Sequential MPI')
raw_data['Fuel System'] = raw_data['Fuel System'].str.replace('SMPI', 'Sequential MPI')
raw_data['Fuel System'] = raw_data['Fuel System'].str.replace('EFI', 'Electronic Fuel Injection')
raw_data['Fuel System'] = raw_data['Fuel System'].str.replace('Direct Gasoline Injection', 'Direct Injection')

# -------- replace na by npnan

raw_data.replace("NA", np.nan, inplace=True)

# -------- convert all to float

raw_data.MSRP = raw_data.MSRP.astype(float)
raw_data["Tire Ratio"] = raw_data["Tire Ratio"].astype(float)
raw_data['Displacement (cc)'] = raw_data['Displacement (cc)'].astype(float)
raw_data['Displacement (L)'] = raw_data['Displacement (L)'].astype(float)
raw_data['Cylinders'] = raw_data['Cylinders'].astype(float)
raw_data['Net Horsepower RPM'] = raw_data['Net Horsepower RPM'].astype(float)
raw_data['Gears'] = raw_data['Gears'].astype(float)
raw_data['Roadside Assistance Miles/km'] = raw_data['Roadside Assistance Miles/km'].astype(float)
raw_data['Drivetrain Miles/km'] = raw_data['Drivetrain Miles/km'].astype(float)
raw_data['Basic Miles/km'] = raw_data['Basic Miles/km'].astype(float)

# -------- delete useless specs


specs_to_numeric = ['MSRP', 'Passenger Capacity', 'Passenger Doors',
                    'Base Curb Weight (lbs)', 'Second Shoulder Room (in)',
                    'Second Head Room (in)', 'Front Shoulder Room (in)',
                    'Second Hip Room (in)', 'Front Head Room (in)', 'Second Leg Room (in)', 'Front Hip Room (in)',
                    'Front Leg Room (in)', 'Width, Max w/o mirrors (in)', 'Track Width, Rear (in)',
                    'Height, Overall (in)', 'Wheelbase (in)', 'Track Width, Front (in)',
                    'Fuel Tank Capacity, Approx (gal)', 'EPA Fuel Economy Est - City (MPG)',
                    'EPA Fuel Economy Est - Hwy (MPG)',
                    'Fuel Economy Est-Combined (MPG)', 'Fourth Gear Ratio (:1)',
                    'Second Gear Ratio (:1)', 'Reverse Ratio (:1)', 'Fifth Gear Ratio (:1)',
                    'Third Gear Ratio (:1)', 'Final Drive Axle Ratio (:1)', 'First Gear Ratio (:1)',
                    'Sixth Gear Ratio (:1)', 'Passenger Volume',
                    'Front Brake Rotor Diam x Thickness (in)', 'Disc - Front (Yes or   )',
                    'Rear Brake Rotor Diam x Thickness (in)', 'Rear Wheel Size (in)',
                    'Rear Wheel Material', 'Spare Wheel Size (in)', 'Front Wheel Size (in)', 'Basic Miles/km',
                    'Basic Years', 'Corrosion Years', 'Drivetrain Miles/km', 'Drivetrain Years',
                    'Roadside Assistance Miles/km', 'Roadside Assistance Years', 'Year', 'Tire Ratio',
                    'Front Tire Width', 'Rear Tire Width', 'Displacement (cc)', 'Displacement (L)', 'Net Torque RPM',
                    'Net Torque', 'Gears', 'Net Horsepower', 'Net Horsepower RPM', 'Cylinders']

for i in specs_to_numeric:
    raw_data[i] = pd.to_numeric(raw_data[i], errors='coerce')
    
specs_to_delete = ['Gas Mileage', 'Engine', 'Engine Type', 'SAE Net Horsepower @ RPM', 'SAE Net Torque @ RPM',
                  'Displacement', 'Trans Description Cont.', 'Rear Tire Size', 'Front Tire Size', 'Rear Wheel Size (in)',
                  'Front Wheel Size (in)', 'Transmission', 'EPA Class', 'Brake ABS System', 'Disc - Front (Yes or   )',
                  'Brake Type', 'Disc - Rear (Yes or   )', 'Spare Tire Size', 'Spare Wheel Size (in)', 'Spare Wheel Material']
raw_data.drop(specs_to_delete, axis=1, inplace=True)

# -------- Identifying columns with NaN totalling more than 50% of elements

col_to_delete = raw_data.columns[raw_data.isna().sum() >= 0.5*len(raw_data)].tolist()

# -------- removing columns with NaNs totalling more than 50% of elements

raw_data.drop(col_to_delete, axis=1, inplace=True)

# -------- deleting old cars

raw_data = raw_data.loc[raw_data['Year'] >= 2016]
