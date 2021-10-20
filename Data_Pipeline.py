from os import rename
import pandas as pd
#Following code melts the data from the inputoutput array to a single column.....
#This means that the Tiva is stacked column wise ie complete AUS r1 to Total entries are stacked together for each column ie AUS c1 through Total c62
i=2000
for i in (2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014):
    print("\n\n\nOpening CSV file for year {}\n\n\n".format(i))
    df = pd.read_csv("C:\\VS Projects\\DATA CLEANING practice\\Major project practice\\Data\\CSVs\\{}.csv".format(i), low_memory=False)
    df
    df.iloc[0,4]
    type(df.iloc[0,4])
    cleandf = pd.melt(df, id_vars = ['convention','inddes','hcountry','hindustry'])
    variables = cleandf['variable'].str.split('_')
    cleandf['fcountry'] = variables.str.get(0)
    cleandf['findustry'] = variables.str.get(1)
    del cleandf['variable']
    del cleandf['convention']
    cleandf.head(5)
    cleandf.to_csv("C:\\VS Projects\\DATA CLEANING practice\\Major project practice\\Data\\CSVs\\finalprocesseddata\\{}_cleaned.csv".format(i),index=False)
    
#Following is a pipeline to extract the data from each year and put in one file 
# CAUTION: ODF should be read out of for loop 
    odf =pd.read_csv("C:\\VS Projects\\DATA CLEANING practice\\Major project practice\\Data\\CSVs\\finalprocesseddata\\2000_cleaned.csv", low_memory=False)
    odf = odf[['inddes', 'hcountry', 'hindustry','fcountry', 'findustry','value']]
    odf = odf.rename(columns = {'value':'t2000'})    


for i in (2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014):
    df = pd.read_csv("C:\\VS Projects\\DATA CLEANING practice\\Major project practice\\Data\\CSVs\\finalprocesseddata\\{}_cleaned.csv".format(i))
    # df = df[['inddes', 'hcountry', 'hindustry','fcountry', 'findustry','value']]
    df = df.rename(columns = {'value':"t{}".format(i)})
    odf["t{}".format(i)] = df["t{}".format(i)]
    odf.head(5)


odf.to_csv("C:\\VS Projects\\DATA CLEANING practice\\Major project practice\\Data\\CSVs\\finalprocesseddata\\allyear.csv", index=False)





