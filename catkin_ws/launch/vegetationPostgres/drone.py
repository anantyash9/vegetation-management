from sqlalchemy import Column, String, Integer, Date, BLOB
from sqlalchemy.dialects.postgresql import JSON,JSONB,BYTEA
from base import Base

class Drone(Base):
    __tablename__ = 'vegetationTest3'

    id = Column(Integer, primary_key=True)
    drone_id = Column(String)
    date = Column(Date)
    line_id = Column(String)
    graph_data = Column(JSON)
    point_cloud = Column(BYTEA)

    def __init__(self, drone_id,date,line_id,graph_data=None,point_cloud = None):
        self.drone_id = drone_id
        self.date = date
        self.line_id = line_id
        self.graph_data =graph_data
        self.point_cloud =point_cloud
        