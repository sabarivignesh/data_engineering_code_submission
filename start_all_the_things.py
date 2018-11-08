""" Entrypoint that gets things going. Necessary because the exercise needs
    to be self-contained.
"""
import os
import logging
from database.database import Database

def main():
    # Initialise logging
    logger = logging.getLogger('assignment-etl')

    # Set up the schema (for this exercise, it's OK to just do this)
    db = Database()
    logger.info({ 'message': 'Creating `iceland` schema' })
    print ("hwooooo!!!!!")
    db.execute("create schema if not exists iceland")

    # Concerts
    from data_models.data_model_api_iceland_concerts import DataModelApiIcelandConcerts
    iceland_concerts_data_model = DataModelApiIcelandConcerts()
    iceland_concerts_data_model.drop_table() # Start fresh every time
    iceland_concerts_data_model.create_table() # This creates the table

    from etl.iceland_api.api_iceland_concerts import ApiIcelandConcerts
    iceland_concerts_etl = ApiIcelandConcerts()
    if not iceland_concerts_etl.run(): # This populates the table
        raise Exception("ETL Job failed: api_iceland_concerts")

    #Earthquakes
    from data_models.data_model_api_iceland_earthquakes import DataModelApiIcelandEarthquakes
    iceland_earthquakes_data_model = DataModelApiIcelandEarthquakes()
    iceland_earthquakes_data_model.drop_table() # Start fresh every time
    iceland_earthquakes_data_model.create_table() # This creates the table

    from etl.iceland_api.api_iceland_earthquakes import ApiIcelandEarthquakes
    iceland_earthquakes_etl = ApiIcelandEarthquakes()
    if not iceland_earthquakes_etl.run(): # This populates the table
        raise Exception("ETL Job failed: api_iceland_earthquakes")  
        
    #Drivers base table - created with date and time as separate columns
    from data_models.data_model_api_iceland_drivers import DataModelApiIcelandDrivers
    iceland_drivers_data_model = DataModelApiIcelandDrivers()
    iceland_drivers_data_model.drop_table() # Start fresh every time
    iceland_drivers_data_model.create_table() # This creates the table

    from etl.iceland_api.api_iceland_drivers import ApiIcelandDrivers
    iceland_drivers_etl = ApiIcelandDrivers()
    if not iceland_drivers_etl.run(): # This populates the table
        raise Exception("ETL Job failed: api_iceland_drivers")

    #drivers table - created with timestamp column from date and time
    from data_models.data_model_drivers_custom import DataModelApiIcelandDriversCustom
    iceland_drivers_custom_data_model = DataModelApiIcelandDriversCustom()
    iceland_drivers_custom_data_model.drop_drivers()
    iceland_drivers_custom_data_model.create_drivers()    
        
if __name__ == "__main__":
    main()
