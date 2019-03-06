import pandas as pd
from scipy import stats
import numpy as np

raw_data = pd.read_csv("", index_col=0)
imputed_data = raw_data.copy()

# -------- specs to be imputed with mean, and the rest with mode

specs_to_mean = ['MSRP', 'Base Curb Weight (lbs)', 'Second Shoulder Room (in)', 'Second Head Room (in)', 'Front Shoulder Room (in)',
                'Second Hip Room (in)', 'Front Head Room (in)', 'Second Leg Room (in)', 'Front Hip Room (in)',
                'Front Leg Room (in)', 'Width, Max w/o mirrors (in)', 'Track Width, Rear (in)', 'Height, Overall (in)',
                'Wheelbase (in)', 'Track Width, Front (in)', 'Fuel Tank Capacity, Approx (gal)', 'Fourth Gear Ratio (:1)',
                'Second Gear Ratio (:1)', 'Reverse Ratio (:1)', 'Fifth Gear Ratio (:1)', 'Third Gear Ratio (:1)',
                'Final Drive Axle Ratio (:1)', 'First Gear Ratio (:1)', 'Sixth Gear Ratio (:1)',
                'Front Brake Rotor Diam x Thickness (in)', 'Rear Brake Rotor Diam x Thickness (in)', 'Displacement (cc)',
                'Displacement (L)', 'Net Torque RPM', 'Net Torque', 'Net Horsepower', 'Net Horsepower RPM',
                'Passenger Volume', 'Turning Diameter - Curb to Curb']

for i in specs_to_mean:
    raw_data[i] = pd.to_numeric(raw_data[i])

list_col = imputed_data.columns.tolist()

specs_to_mode = list_col.copy()

for item in specs_to_mean:
    specs_to_mode.remove(item)

# -------- imputer func

def imputer_mean(x, y):
    temp_list_model = raw_data.loc[raw_data["Model"] == raw_data.loc[x, "Model"]].loc[:, y].dropna()
    if len(temp_list_model) > 0:
        imputed_data.loc[x, y] = np.round(temp_list_model.mean(), 2)
    else:
        temp_list_epa = raw_data.loc[raw_data["EPA Classification"]
                                            == raw_data.loc[x, "EPA Classification"]].loc[:, y].dropna()
        if len(temp_list_epa) > 0:
            imputed_data.loc[x, y] = np.round(temp_list_epa.mean(), 2)
        else:
            temp_list_bodystyle = raw_data.loc[raw_data["Body Style"] ==
                                                    raw_data.loc[x, "Body Style"]].loc[:, y].dropna()
            if len(temp_list_bodystyle) > 0:
                imputed_data.loc[x, y] = np.round(temp_list_bodystyle.mean(), 2)

def imputer_mode(x, y):
    temp_list_model = pd.Series(raw_data.loc[raw_data["Model"] == raw_data.loc[x, "Model"]].loc[:, y].dropna())
    if len(temp_list_model) > 0:
        imputed_data.loc[x, y] = stats.mode(temp_list_model)[0][0]
    else:
        temp_list_epa = raw_data.loc[raw_data["EPA Classification"]
                                            == raw_data.loc[x, "EPA Classification"]].loc[:, y].dropna()
        if len(temp_list_epa) > 0:
            imputed_data.loc[x, y] = stats.mode(temp_list_epa)[0][0]
        else:
            temp_list_bodystyle = raw_data.loc[raw_data["Body Style"] ==
                                                    raw_data.loc[x, "Body Style"]].loc[:, y].dropna()
            if len(temp_list_bodystyle) > 0:
                imputed_data.loc[x, y] = stats.mode(temp_list_bodystyle)[0][0]

# -------- iterator - mean

for col in specs_to_mean:
    for row in imputed_data.index:
        val = imputed_data.get_value(row, col)
        if pd.isnull(val):
            raw_data.set_value(row,col, imputer_mean(row, col))

# -------- iterator - mode

for col in specs_to_mode:
    for row in imputed_data.index:
        val = imputed_data.get_value(row, col)
        if pd.isnull(val):
            raw_data.set_value(row,col, imputer_mode(row, col))

# -------- drop missing values

imputed_data = imputed_data.dropna()

# -------- export 

imputed_data.to_csv(r'')
