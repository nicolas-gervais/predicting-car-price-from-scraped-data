import pandas as pd
pd.options.display.max_rows = 999

df = pd.read_csv("", index_col=0)

specs_to_dummies = ['Drivetrain', 'Body Style', 'EPA Classification', 'Fuel System', 'Trans Type', 'Steering Type',
                    'Front Wheel Material', 'Suspension Type - Rear', 'Suspension Type - Front (Cont.)', 'Suspension Type - Front',
                    'Suspension Type - Rear (Cont.)', 'Air Bag-Frontal-Driver', 'Air Bag-Frontal-Passenger',
                    'Air Bag-Passenger Switch (On/Off)', 'Air Bag-Side Body-Front', 'Air Bag-Side Body-Rear',
                    'Air Bag-Side Head-Front', 'Air Bag-Side Head-Rear', 'Brakes-ABS', 'Child Safety Rear Door Locks',
                    'Daytime Running Lights', 'Traction Control', 'Night Vision', 'Rollover Protection Bars', 'Fog Lamps',
                    'Parking Aid', 'Tire Pressure Monitor', 'Back-Up Camera', 'Stability Control', 'Engine Configuration',
                    'Engine Class','Tire Rating', 'Tire Ratio']

for item in specs_to_dummies:
    dummies = pd.get_dummies(df[item], prefix_sep=': ', prefix=item)
    df = pd.concat([df, dummies], sort=False, axis=1)

df = df.drop(specs_to_dummies, axis=1)

# -------- export and inspect

df.to_csv(r'')
