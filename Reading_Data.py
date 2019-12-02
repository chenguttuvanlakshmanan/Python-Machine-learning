#Reading Data from oracle
#____________________________________________________________________________________________________

import pandas as pd
from sqlalchemy import create_engine

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

# database name used with SID name

engine = create_engine(
    oracle_connection_string.format(
        username='hr',
        password='python3l',
        hostname='localhost',
        port='1521',
        database='orcl',
    )
)

data = pd.read_sql("select * from countries", engine)

# Another way of reading data from the oracle DB when service name most needed
#_____________________________________________________________________________________________________
import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle

oracle_connection_string = (
    'oracle+cx_oracle://{username}:{password}@' +
    cx_Oracle.makedsn('{hostname}', '{port}', service_name='{service_name}')
)

engine = create_engine(
    oracle_connection_string.format(
        username='CALCULATING_CARL',
        password='12345',
        hostname='all.thedata.com',
        port='1521',
        service_name='every.piece.ofdata',
    )
)

data = pd.read_sql("SELECT * FROM …", engine)

# Reading data using pandas

# from CSV
d = pd.read_csv('Data/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv')

# write to csv df is the dataframe we are going to write to csv
df.to_csv('sample_data.csv')

# from excel
d=pd.read_excel('Data/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.xls')
 
# write to excel df is the dataframe we are going to write to excel
df.to_excel('sample_data.xls')
  
# read html file and convert to json
import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))
print(df[0].to_json(orient='records'))
 
# read html with beautifull soup and store as pandas dataframe
 
import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))[0]
