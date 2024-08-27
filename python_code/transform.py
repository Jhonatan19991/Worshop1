import pandas as pd
import numpy as np
class DataTransform:
    """A class to transform and normalize candidate data."""
    def __init__(self, file):
        """_summary_

        Args:
            file (csvtype): Candidates csv
        """
        self.df = pd.read_csv(file, sep=';')
    

    def rename(self) -> None:
        """Renames DataFrame columns for easier handling."""

        self.columns ={            
            "First Name": "FirstName",
            "Last Name": "LastName",
            "Application Date": "ApplicationDate",
            "Code Challenge Score": "CodeChallengeScore",
            "Technical Interview Score": "TechnicalInterviewScore"
        }
        self.df.rename(columns=self.columns, inplace=True)
    

    def insert_id(self) -> None:
        """Inserts an 'id' column with sequential numbers for each row."""
        self.df['id'] = range(1,len(self.df)+1)
    

    def technology_by_category(self) -> None:
        """Maps technology to categories and updates the 'Technology' column."""
        self.technology_to_category = {
            'Game Development': 'Software Development',
            'DevOps': 'DevOps and System Administration',
            'Social Media Community Management': 'Management and Support',
            'System Administration': 'DevOps and System Administration',
            'Mulesoft': 'Other Areas',
            'Development - Backend': 'Software Development',
            'Development - FullStack': 'Software Development',
            'Adobe Experience Manager': 'Software Development',
            'Data Engineer': 'Data Engineering and Analytics',
            'Security': 'Security',
            'Business Intelligence': 'Data Engineering and Analytics',
            'Development - CMS Frontend': 'Software Development',
            'Database Administration': 'DevOps and System Administration',
            'Client Success': 'Management and Support',
            'Design': 'Design and QA',
            'QA Manual': 'Design and QA',
            'Technical Writing': 'Other Areas',
            'QA Automation': 'Design and QA',
            'Sales': 'Management and Support',
            'Development - Frontend': 'Software Development',
            'Development - CMS Backend': 'Software Development',
            'Business Analytics / Project Management': 'Data Engineering and Analytics',
            'Salesforce': 'Other Areas',
            'Security Compliance': 'Security'
            }
        
        self.df['Technology'] = self.df['Technology'].map(self.technology_to_category)
    
    
    def FullNameReplace(self) -> None:
        """Creates a 'FullName' column by combining 'FirstName' and 'LastName', then drops the original columns."""
        self.df['FullName'] = self.df['FirstName'] + ' ' + self.df['LastName']
        self.df.drop(columns=['FirstName','LastName'], inplace=True)


    def ApplicationDateToDateType(self) -> None:
        """Converts 'ApplicationDate' column to datetime type."""
        self.df['ApplicationDate'] = pd.to_datetime(self.df['ApplicationDate'])

    def NormalizeCountry(self) -> pd.DataFrame:
        """Normalizes the 'Country' column and creates a reference DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing unique countries and their IDs.
        """
        unique_countries = self.df['Country'].unique()

        country_df = pd.DataFrame({
            'id': range(1, len(unique_countries) + 1),
            'CountriesName': unique_countries
        })

        country_map = dict(zip(unique_countries, country_df['id']))

        self.df['CountryID'] = self.df['Country'].map(country_map)

        self.df.drop(columns=['Country'], inplace=True)

        return country_df
    
    def NomalizeTechnology(self) -> pd.DataFrame:
        """Normalizes the 'Technology' column and creates a reference DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing unique technologies and their IDs.
        """
        unique_technology = self.df['Technology'].unique()

        technology_df = pd.DataFrame({
            'id': range(1, len(unique_technology) + 1),
            'TechnologiesName': unique_technology
        })

        technology_map = dict(zip(unique_technology, technology_df['id']))

        self.df['TechonologyID'] = self.df['Technology'].map(technology_map)

        self.df.drop(columns=['Technology'], inplace=True)

        return technology_df
    
    def NomalizeSeniority(self) -> pd.DataFrame:
        """Normalizes the 'Seniority' column and creates a reference DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing unique seniorities and their IDs.
        """
        unique_Seniority = self.df['Seniority'].unique()

        Seniority_df = pd.DataFrame({
            'id': range(1, len(unique_Seniority) + 1),
            'SenioritiesName': unique_Seniority
        })

        Seniority_map = dict(zip(unique_Seniority, Seniority_df['id']))

        self.df['SeniorityID'] = self.df['Seniority'].map(Seniority_map)

        self.df.drop(columns=['Seniority'], inplace=True)

        return Seniority_df
    

    def HiredOrNotHired(self) -> None:
        #I consider a candidate HIRED when he has both scores greater than or equal to 7
        self.df['Hired'] = np.where((self.df['Code Challenge Score'] >= 7) & (self.df['Technical Interview Score'] >= 7), 1, 0)

    
    
        
