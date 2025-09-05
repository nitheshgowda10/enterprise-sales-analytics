from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

host = os.getenv("DB_HOST")
user =os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
dbname=os.getenv("DB_NAME")
port=os.getenv("DB_PORT")

engine=create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}")
print("Connected to database!")

# df=pd.read_csv("D:/project 2/enterprise sales analytics/data/Global_superstore2.csv")
df = pd.read_csv("D:/project 2/enterprise sales analytics/data/superstore.csv", encoding="latin1")


df = df.drop_duplicates()
df=df.dropna()

df.to_sql("superstore",con=engine, if_exists="replace",index=False)
print("Data loaded into MYSQL!!")