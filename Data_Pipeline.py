
import pandas as pd
import os
import pyxlsb as xls


folder_path = 'RAW DATA/'
file_list = os.listdir()
file_list


get_file_name(0)


df = pd.read_excel(get_file_name(0), skiprows=2, nrows=30)
df.head()

class AbhilashDataFrame:
    """
    This class implements data cleaning on the dataset
    """
    def __init__(self, folder_path="RAW DATA//", nrows=20):
        """ Please enter the folder path and the number of rows you want to read
        """
        self.nrows = nrows
        os.getcwd()
        os.chdir(os.path.join(folder_path))
        self.files = os.listdir(folder_path)
        self.all_years = pd.DataFrame()

    def __call__(self, file_name=..., year=..., iterand=0):
        """This method takes file_name as string for the file name of the excel workbook .
        The second and third arguments are year as list of years needed to work on and the iterand argument
        """
        def get_file_name(workbooklist=0):
            return f"{file_list[workbooklist]}"


        for file in self.files:

            print(f"\n\n\n Opening XLSXB file for year {year} :- \n\n\n")

            self.df = pd.read_excel(f"{self.folder_path}{file}",
                                    nrows=self.nrows,
                                    skiprows=4,
                                    index_col=[2, 3],
                                    header=[0, 1],
                                    )
            pd.concat(self.all_years, self.flat_df)
            break

    def melt(self, save_file_path='Flattened Data Files//', save=True):

        self.flat_df = pd.melt(
            self.df,
            id_vars=[(0, 0), (1, 1)],
            col_level=1
        )
        return self.flat_df

    # cleandf.to_csv(f"{save_file_path}FlatData.csv",
    #                index=False)

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


data2000 = AbhilashDataFrame()
data2000.nrows
data2000()

data2000.df.iloc[0, 0]
data2000.df.columns[0]
data2000.all_years

data2000.df

data2000.flat_df = pd.melt(
    data2000.df,
    id_vars=[data2000.df.columns[0], data2000.df.columns[1]],
    col_level=1,
    ignore_index=False,
)
