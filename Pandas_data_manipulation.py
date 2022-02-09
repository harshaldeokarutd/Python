import re
import pandas as pd
import numpy as np

Energy = pd.read_excel("C:\\Users\\harsh\\Documents\\java\\Energy Indicators.xls", skiprows=17, skipfooter=1)
Energy.drop(columns=['Unnamed: 0', 'Unnamed: 1'], inplace=True)
Energy.rename(columns={'Unnamed: 2': 'Country', 'Petajoules': 'Energy Supply', 'Gigajoules': 'Energy Supply per Capita',
                       '%': '% Renewable'}, inplace=True)
Energy.replace({'...': np.nan}, inplace=True)
Energy['Energy Supply'] = Energy['Energy Supply'] * 1000000

Energy = Energy.dropna()

Energy.replace({"Republic of Korea": "South Korea",
                "United States of America": "United States",
                "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                "China, Hong Kong Special Administrative Region": "Hong Kong"}, inplace=True)


def test(x):
    y = re.findall("^([A-Z][a-z]+)", x)
    for i in y:
        z = i.replace("[", "")
        return z


Energy['Country'] = Energy['Country'].apply(lambda x: test(x))

GDP = pd.read_csv("C:\\Users\\harsh\\Documents\\java\\GDP.csv", skiprows=4)

GDP.replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"},
            inplace=True)
GDP = GDP.drop(columns=['Unnamed: 65'])
GDP = GDP.dropna()
GDP = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
GDP.columns = ['Country', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']

science = pd.read_excel("C:\\Users\\harsh\\Documents\\java\\science.xlsx")
science = science[:15]

df = pd.merge(science, Energy, how='inner', left_on='Country', right_on='Country')
final_df = pd.merge(df, GDP, how='inner', left_on='Country', right_on='Country')
final_df = final_df.set_index('Country')

new = final_df[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].mean(
    axis=1).sort_values(ascending=False)

print(final_df[final_df['Rank'] == 4]['2015'] - final_df[final_df['Rank'] == 4]['2006'])

final_df['Energy Supply'] = final_df['Energy Supply'] * 100000

print(final_df['Energy Supply'].mean())

final_df['Citation Ratio'] = final_df['Self-citations'] / final_df['Citations']

final_df['Population'] = final_df['Energy Supply'] / final_df['Energy Supply per Capita']

final_df['Population'].sort_values(ascending=True)

final_df['PopEst'] = final_df['Energy Supply'] / final_df['Energy Supply per Capita']

final_df['Citable docs per Capita'] = final_df['Citable documents'] / final_df['PopEst']

final_df.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])

ContinentDict = {'China': 'Asia',
                 'United States': 'North America',
                 'Japan': 'Asia',
                 'United Kingdom': 'Europe',
                 'Russian Federation': 'Europe',
                 'Canada': 'North America',
                 'Germany': 'Europe',
                 'India': 'Asia',
                 'France': 'Europe',
                 'South Korea': 'Asia',
                 'Italy': 'Europe',
                 'Spain': 'Europe',
                 'Iran': 'Asia',
                 'Australia': 'Australia',
                 'Brazil': 'South America'}

final_df = final_df.reset_index()
final_df['continent'] = [ContinentDict[i] for i in final_df['Country']]
