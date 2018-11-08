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

if __name__ == "__main__":
    main()
