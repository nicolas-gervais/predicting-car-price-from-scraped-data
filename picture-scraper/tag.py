import pandas as pd
import os
import sys

os.chdir(sys.argv[1])

template = 'https://images.hgmsites.net/'


def run():
    df = pd.read_csv('specs-and-pics.csv', dtype=str, index_col=0).T.iloc[:100, :]  # REMOVE REMOVE

    df = df.iloc[:, :-121]

    df = (df.melt(id_vars=df.columns[:108],value_name='Picture', value_vars=df.columns[108:])
          .set_index(['Picture']).reset_index())

    impt_cols = [
        'Make', 'Model', 'Year', 'MSRP', 'Front Wheel Size (in)', 'SAE Net Horsepower @ RPM',
        'Displacement', 'Engine Type', 'Width, Max w/o mirrors (in)', 'Height, Overall (in)',
        'Length, Overall (in)', 'Gas Mileage', 'Drivetrain', 'Passenger Capacity', 'Passenger Doors',
        'Body Style', 'Picture']

    df = df[impt_cols]

    df['Picture'] = template + df['Picture']

    df = df.dropna(subset=['Picture'])

    # ----- // Cleaning Columns

    df['MSRP'] = df['MSRP'].str.replace(',', '').str.replace('$', '').str[:-3]

    df['Front Wheel Size (in)'] = df['Front Wheel Size (in)'].str[:2]

    df['SAE Net Horsepower @ RPM'] = df['SAE Net Horsepower @ RPM'].str[:2] + '0'

    df['Displacement'] = df['Displacement'].str[:3].str.replace('.', '')

    df['Engine Type'] = df['Engine Type'].str.extract('(\d+)')
    df.loc[df['Engine Type'] == '15', 'Engine Type'] = '4'

    df['Width, Max w/o mirrors (in)'] = df['Width, Max w/o mirrors (in)'].str[:2]

    df['Height, Overall (in)'] = df['Height, Overall (in)'].str[:2]

    df['Length, Overall (in)'] = df['Length, Overall (in)'].str[:3]

    df['Gas Mileage'] = df['Gas Mileage'].str[:2]

    df['Drivetrain'] = df['Drivetrain'].str.replace('-', ' ').str.replace('Four', '4').str.upper()
    df['Drivetrain'] = df['Drivetrain'].str[0] + 'WD'

    df.loc[df['Body Style'].str.contains('Pickup', na=False), 'Body Style'] = 'Pickup'
    df['Body Style'] = df['Body Style'].str.replace(' Car', '')
    df.loc[df['Body Style'].str.lower().str.contains('van', na=False), 'Body Style'] = 'Van'
    df['Body Style'] = df['Body Style'].str.replace('Sport Utility', 'SUV')
    df['Body Style'] = df['Body Style'].str.replace('Hatchback', '2dr')

    df['ID'] = df.iloc[:, :-1].apply(lambda x: '_'.join(x.astype(str)), axis=1)

    final_df = df[['ID', 'Picture']]

    final_df.to_csv('id_and_pic_url.csv', index=None)


if __name__ == '__main__':
    print('%s started running.' % os.path.basename(__file__))
    run()
    print('%s finished running.' % os.path.basename(__file__))
