import pandas as pd


class AbhilashDataFrame:

    def __init__(self, folder_path="RAW DATA//", nrows=20):
        """ Please enter the folder path and the number of rows you want to read
        """
        self.folder_path = folder_path
        self.nrows = nrows

    def __call__(self, file_name="WIOT2000_Nov16_ROW.xlsb", years=[2000], iterand=0):
        """This method takes file_name as string for the file name of the excel workbook .
        The second and third arguments are year as list of years needed to work on and the iterand argument
        """

        print(f"\n\n\n Opening XLSXB file for year {years[iterand]} \n\n\n")
        self.df = pd.read_excel(f"{self.folder_path}{file_name}",
                                nrows=self.nrows,
                                skiprows=4,
                                index_col=[2, 3],
                                header=[0, 1]
                                )
        self.df
        self.geographies = self.df.columns
        self.df.iloc[0, 4]
        type(self.df.iloc[0, 4])
        pass

    def melt(self):
        cleandf = pd.melt(
            self.df, id_vars=['convention', 'inddes', 'hcountry', 'hindustry'])
        variables = cleandf['variable'].str.split('_')
        cleandf['fcountry'] = variables.str.get(0)
        cleandf['findustry'] = variables.str.get(1)
        del cleandf['variable']
        del cleandf['convention']
        cleandf.head(5)
        cleandf.to_csv(
            "C:\\VS Projects\\DATA CLEANING practice\\Major project practice\\Data\\CSVs\\finalprocesseddata\\{}_cleaned.csv".format(i), index=False)

    # # Following is a pipeline to extract the data from each year and put in one file
    # # CAUTION: ODF should be read out of for loop
    #     odf = pd.read_csv(
    #         "C:\\VS Projects\\DATA CLEANING practice\\Major project practice\\Data\\CSVs\\finalprocesseddata\\2000_cleaned.csv", low_memory=False)
    #     odf = odf[['inddes', 'hcountry', 'hindustry',
    #                'fcountry', 'findustry', 'value']]
    #     odf = odf.rename(columns={'value': 't2000'})

    # for i in (2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014):
    #     df = pd.read_csv(
    #         "C:\\VS Projects\\DATA CLEANING practice\\Major project practice\\Data\\CSVs\\finalprocesseddata\\{}_cleaned.csv".format(i))
    #     # df = df[['inddes', 'hcountry', 'hindustry','fcountry', 'findustry','value']]
    #     df = df.rename(columns={'value': "t{}".format(i)})
    #     odf["t{}".format(i)] = df["t{}".format(i)]
    #     odf.head(5)

    # odf.to_csv("C:\\VS Projects\\DATA CLEANING practice\\Major project practice\\Data\\CSVs\\finalprocesseddata\\allyear.csv", index=False)


data2000 = AbhilashDataFrame
data2000.__call__()
data2000.df
