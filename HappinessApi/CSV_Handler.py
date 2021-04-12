import pandas,os
default_csv_path='world-happiness-report-2021.csv'

class CsvHandler:
   # csv will in root directory 
    def __init__(self,path=default_csv_path):
        self.csv_path = path
    def read_csv_details(self):
       data = pandas.read_csv(self.csv_path,usecols = ['Country name','Ladder score','Healthy life expectancy','Generosity','Logged GDP per capita'])
       data = data.rename(columns={'Country name': 'CountryName', 
       'Ladder score':'LadderScore','Healthy life expectancy':'HealthyLifeExpectancy',
       'Logged GDP per capita':'Gdp'


       })
       # returns dataframe object only 
       return data

class CsvExecuter:
    # methods on csv will be executed

    def __init__(self):
        self.csv_object = CsvHandler()
        self.data = self.csv_object.read_csv_details()
   
    def get_country_details(self,country_name):
        # pandas series objects
        country_details = self.data[self.data.CountryName == country_name].iloc[0]  
        
        #series obj->dict
        return country_details.to_dict()#value is dict

    def get_countries_within_scores(self,from_score,to_score):
       country_list = self.data[(self.data.LadderScore >= from_score) & (self.data.LadderScore <= to_score)]
      # Dataframe object
       
       #dataframe obj->List of dictionary
       values=country_list.to_dict('records')
       
       return values# values is list of dict
       
     
       
