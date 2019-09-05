from datetime import date

from base import Base, Session, engine
from drone import Drone
Base.metadata.create_all(engine)


class Vegetation():
    def pushData(self,drone_id,date_info,line_id,graph_data=None,point_cloud=None):
        session = Session()  
        try:
            data = Drone(drone_id,date_info,line_id,graph_data,point_cloud)
            session.add(data)
            session.commit()
        except Exception as e:
            if session:
                session.rollback()
            print("Error printing ",e)
        finally:
            session.close()
        


