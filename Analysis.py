import pandas as pd
# import numpy as np
df = pd.read_csv("C:\\VS Projects\\DATA CLEANING practice\\All_Years.csv", low_memory=False)
df
df = df.rename(columns={'hindustry':'exindustry','hcountry':'excountry','fcountry':'imcountry','findustry':'imindustry'})
df
df.to_csv("C:\\VS Projects\\DATA CLEANING practice\\All_Years.csv", index=False)
type(df.iloc[0,3])
cntrylist = df['hcountry'].unique()
cntrylist
hindlist = df['hindustry'].unique()
hindlist

findlist = df['findustry'].unique()

fcntrylist = df['fcountry'].unique()

findlist

print("\n\nPlease select from the following(as is) \n\n Country",
cntrylist,"\n\n\n r1 to r56 are intermediaries... ignore after them\n",hindlist,
"\n\n\n c1 to c56 are intermediaries and after that are final consumptions\n",findlist)



# import pandas as pd


# axis = []
# for i in (2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014):
#     axis.append(str(i))
# type(axis[0])
df

# for i in axis:

# import pandas as pd

class gvcOOP():

    def __init__(self,ex_country,ex_industry,im_country,im_industry,year):
        self.ex_country = ex_country      #if the variables are not declared using self, then we cant use the object later
        self.ex_industry = ex_industry
        self.im_country = im_country
        self.im_industry = im_industry
        self.year = year
        self.df = pd.read_csv("C:\\VS Projects\\DATA CLEANING practice\\All_Years.csv", low_memory=False)

        self.inter_ex_list = []
        for i in range(56): #To get intermediaries for export is 'c1 , c2 ,c3,c4....c56'
            self.inter_ex_list.append("c{}".format(i+1))
        print("\n\n",self.inter_ex_list,"\n\n")
        
    def DVX(self): # Works Well
        print("Calculating DVX for {}'s {} industry for the year {}".format(self.ex_country,self.ex_industry,self.year))

        self.dvxlist = self.df.loc[(self.df['excountry']==self.ex_country)&(self.df['exindustry']==self.ex_industry)&(self.df['imcountry']!=self.ex_country)]
        self.dvxdf = self.dvxlist.loc[(self.dvxlist['excountry']!="TOT")&(self.dvxlist['imcountry']!="TOT")]
        del self.dvxlist
        self.dvxdf2 = self.dvxdf.loc[(self.dvxdf['imindustry'].isin((self.inter_ex_list)))]
        del self.dvxdf
        print("Your DVX data is in table <dvxdf2> dataframe")
        print("Dtype of dvxdf2==>", type(self.dvxdf2.iloc[4,8]),'\n\n')
        self.findvx = (self.dvxdf2['t{}'.format(self.year)].sum())
        print("DVX Value stored in variable   findvx, \n\nDataframe stored in variable dvxdf2\n")
        return self.findvx

    def GX(self): #Works well
        print("Calculating Gross Exports for {}'s {} industry for the year {}".format(self.ex_country,self.ex_industry,self.year))
        #S
        self.inter_gx_list = self.inter_ex_list + ['c57','c58','c59']

        self.gxlist = self.df.loc[(self.df['excountry']==self.ex_country)&(self.df['exindustry']==self.ex_industry)&(self.df['imcountry']!=self.ex_country)]
        self.gxdf = self.gxlist.loc[(self.gxlist['excountry']!="TOT")&(self.gxlist['imcountry']!="TOT")]
        del self.gxlist
        self.gxdf2 = self.gxdf.loc[(self.gxdf['imindustry'].isin((self.inter_gx_list)))]
        del self.gxdf
        print("Your GX data is in table <gxdf2> dataframe")
        print("Dtype of gxdf2==>", type(self.gxdf2.iloc[4,8]),'\n\n')
        self.fingx = (self.gxdf2['t{}'.format(self.year)].sum())
        print("GX Value stored in variable   fingx, \n\nDataframe stored in variable gxdf2\n")
        return self.fingx

    def FVA(self):
        self.inter_im_list = []
        for i in range(56): #To get intermediaries for import is 'r1 , r2 ,r3,r4....r56'
            self.inter_im_list.append('r{}'.format(i+1))

        print("Calculating DVX for {}'s {} industry for the year {}".format(self.ex_country,self.ex_industry,self.year))

        self.fvalist = self.df.loc[(self.df['excountry']!=self.ex_country)&(self.df['exindustry'].isin((self.inter_im_list)))]
        print(self.fvalist.tail(10))
        self.fvadf = self.fvalist.loc[(self.fvalist['excountry']!="TOT")&(self.fvalist['imcountry']==self.ex_country)]
        print(self.fvadf.tail(10))

        del self.fvalist
        #calculate purpose we take another variable and make it equal to ex_industry and remove the r to c

        self.fvadf2 = self.fvadf.loc[self.fvadf['imindustry']==self.ex_industry.replace('r', 'c')]
        del self.fvadf
        print("\n\n",self.fvadf2.tail(10))
        print("Your FVA data is in table <fvadf2> dataframe")
        print("Dtype of fvadf2==>", type(self.fvadf2.iloc[4,8]),'\n\n')
        self.finfva = self.fvadf2['t{}'.format(self.year)].sum()
        print("FVA Value stored in variable findvx, \n\nDataframe stored in variable dvxdf2\n")
        return self.finfva
       
    

# a.inter_im_list


a = gvcOOP('AUS','r6','AUT','c6',2014)

# a.GX()

# a.DVX()
a.FVA()
# # a.dvxdf2.to_csv("m1.csv",index=False)
# a.fvadf2
# a.df




