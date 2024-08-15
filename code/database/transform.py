import pandas as pd
import numpy as np
class DataTransform:
    """_summary_
    """
    def __init__(self, file):
        """_summary_

        Args:
            file (csvtype): Candidates csv
        """
        self.df = pd.read_csv(file, sep=';')
    

    def rename(self) -> None:
        """_summary_
        """

        self.columns ={            
            "First Name": "FirstName",
            "Last Name": "LastName",
            "Application Date": "ApplicationDate",
            "Code Challenge Score": "CodeChallengeScore",
            "Technical Interview Score": "TechnicalInterviewScore"
        }
        self.df.rename(columns=self.columns, inplace=True)
    

    def insert_id(self) -> None:
        """_summary_
        """
        self.df['id'] = range(1,len(self.df)+1)
    

    def technology_by_category(self) -> None:
        """_summary_
        """
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
        
        self.df['CategoryOfTechnology'] = self.df['Technology'].map(self.technology_to_category)
    
    
    def full_name_replace(self) -> None:
        self.df['FullName'] = self.df['FirstName'] + ' ' + self.df['LastName']
        self.df.drop(columns=['FirstName','LastName'], inplace=True)



    def hired_or_not_hired(self) -> None:
        #I consider a candidate HIRED when he has both scores greater than or equal to 7
        self.df['Hired'] = np.where((self.df['Code Challenge Score'] >= 7) & (self.df['Technical Interview Score'] >= 7), 1, 0)
    
        
