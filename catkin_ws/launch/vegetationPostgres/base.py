from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


username = 'postgres'
password = 'postgres'
hostname = 'localhost'
portnumber = 5432
dbName = 'datastore'


connection_string = "postgresql://"+username+":"+password+"@"+hostname+":"+str(portnumber)+"/"+dbName+""
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)

Base = declarative_base()