![image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMoFxet9K9uMBhYpQyE_My9--989HZ4vCMSA&s)
### ETL - Workshop-01 - Data Engineer Interview by Jhonatan Steven Morales

### Tools used
- Python
- Jupyter
- SQLAlchemy
- PostgreSQL
- PowerBI
### About the data

*   **FirstName**: The candidate's first name
*   **LastName**: The candidate's last name
*   **Email**: The candidate's email address
*   **ApplicationDate**: The date the candidate applied for the job
*   **YOE**: Years of experience
*   **Seniority**: The position the candidate is applying for
*   **Technology**: The area or field the candidate is applying to
*   **Code Challenge Score**: A score from 0 to 10 for the practical test
*   **Technical Interview Score**: A score from 0 to 10 for the theoretical or technical interview

This dataset contains 50k rows abaout candidates
  
#### Applications Prerequiered :
1. Install Python : [Python Downloads](https://www.python.org/downloads/)
2. Install PostgreSQL : [PostgreSQL Downloads](https://www.postgresql.org/download/)
3. Install Power BI : [Install Power BI Desktop](https://www.microsoft.com/en-us/download/details.aspx?id=58494)

### Repository

data <- this folder contain the candidates.csv used in this project .

python_code <- this folder contain the data base setup and the transform.py witch is used to normalize the data.

notebooks <- this folder contain de nootebooks in this project, in this case the Data explolatory analysis 
and the processed data.

src <- in this folder we make the python codes where we used to connect to the database and to make de models about the tables.

### Workflow

![image](https://github.com/Jhonatan19991/images/blob/main/assets/workflow.png)

### How to Use this Project

1. Clone the project
```bash
  git clone https://github.com/Jhonatan19991/Worshop1.git
```

2. Go to the project directory
```bash
  cd Worshop1
```

3. make sure of made the .env file

    - PGDIALECT=The database dialect or type. In this case it is set to postgres
    - PGUSER=Your PostgreSQL database username.
    - PGPASSWD=Your PostgreSQL database password.
    - PGHOST=The host address or IP where your PostgreSQL database is running.
    - PGPORT=The port on which PostgreSQL is listening.
    - PGDB=The name of your PostgreSQL database.
    - WORK_DIR=the location for you root of the project

4. Create virtual environment for Python
```bash
  python -m venv venv
```
5. Activate the enviroment
```bash
  source .\venv\Scripts\Activate.ps1
```
6. Install libreries
```bash
  pip install -r requirements.txt
```
7. Create a database in PostgreSQL
8. Explore the project by starting with the files in numerical order to understand what was done and the procedures that were followed.
9. Now Open PowerBI
    
   9.1 start a new dashboard
   
![image](https://github.com/Jhonatan19991/images/blob/main/assets/power1.png)

   
   9.2 now select this opion and go to the option more...

   ![image](https://github.com/Jhonatan19991/images/blob/main/assets/powe2.png)

   
   9.3 now select you data base type, in my case is PostgresSQL

   ![image](https://github.com/Jhonatan19991/images/blob/main/assets/power3.png)

   
   9.4 put the information of your database

   ![image](https://github.com/Jhonatan19991/images/blob/main/assets/power4.png)

   
   9.5 and now select the tables you want import to PowerBI

   ![image](https://github.com/Jhonatan19991/images/blob/main/assets/power5.png)


Now the data is now synchronized with powerBI, and you can start make your own dashboards!

# Thank You for Visiting My Repository!

Thank you for taking the time to explore my ETL - Workshop-01 project for a Data Engineer Interview. I hope you found the tools, code, and data processes insightful and useful for your own projects. If you have any questions or suggestions, feel free to reach out.

Happy coding, and best of luck with your data engineering endeavors!




