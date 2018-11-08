import psycopg2
import os
import json

DATABASE_HOST = os.getenv('DB_HOST')
DATABASE_PORT = os.getenv('DB_PORT')
DATABASE_USERNAME = os.getenv('DB_USERNAME')
DATABASE_PASSWORD = os.getenv('DB_PASSWORD')
DATABASE_DBNAME = os.getenv('DB_DBNAME')

class DataModelApiIcelandTestCaseThree():

    def _establish_connection(self):

        try:
            self.connection = psycopg2.connect(
                dbname=DATABASE_DBNAME,
                user=DATABASE_USERNAME,
                host=DATABASE_HOST,
                port=DATABASE_PORT,
                password=DATABASE_PASSWORD
            )
        except Exception as err:
            raise err


    def test_case_three_concerts(self):

        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(
        """select column_name, data_type from information_schema.columns where table_name = 'concerts'
        """)
        columns = dict(cursor.fetchall())

        if columns['band'] == 'character varying' and columns['event'] == 'character varying' and columns['hall'] == 'character varying' and columns['timestamp'] == 'timestamp without time zone':
            print ("Test Cases 3 - Concerts - Successful")
            return;
        else:
            print ("Test Cases 3 - Concerts - Failed")


    def test_case_three_earthquakes(self):

        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(
        """select column_name, data_type from information_schema.columns where table_name = 'earthquakes'
        """)
        columns = dict(cursor.fetchall())

        if columns['latitude'] == 'real' and columns['longitude'] == 'real' and columns['magnitude'] == 'real' and columns['timestamp'] == 'timestamp without time zone':
            print ("Test Cases 3 - Earthquakes - Successful")
            return;
        else:
            print ("Test Cases 3 - Earthquakes - Failed")


    def test_case_three_drivers(self):


        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(
        """select column_name, data_type from information_schema.columns where table_name = 'drivers_base'
        """)
        columns = dict(cursor.fetchall())

        if columns['from'] == 'text' and columns['to'] == 'text' and columns['date'] == 'date' and columns['time'] == 'character varying':
            print ("Test Cases 3 - drivers - Successful")
            return;
        else:
            print ("Test Cases 3 - drivers - Failed")


    def test_case_three(self):

        test_case_three = DataModelApiIcelandTestCaseThree()

        test_case_three.test_case_three_concerts()
        test_case_three.test_case_three_earthquakes()
        test_case_three.test_case_three_drivers()
