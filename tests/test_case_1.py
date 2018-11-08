import psycopg2
import os
import json

DATABASE_HOST = os.getenv('DB_HOST')
DATABASE_PORT = os.getenv('DB_PORT')
DATABASE_USERNAME = os.getenv('DB_USERNAME')
DATABASE_PASSWORD = os.getenv('DB_PASSWORD')
DATABASE_DBNAME = os.getenv('DB_DBNAME')

class DataModelApiIcelandTestCaseOne():

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



    def test_case_one_concerts(self):


        with open('data/api_iceland_concerts.json') as json_data:
	           data = json.load(json_data,)

        concerts_data = data['results']
        concerts_count = len(concerts_data)

        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(
        """select cast(count(*) as integer) from iceland.concerts
        """)
        count = cursor.fetchall()

        if count[0][0] == concerts_count:
            print ("Test Cases 1 - Concerts - Successful")
            return;
        else:
            print ("Test Cases 1 - Concerts - Failed")

    def test_case_one_earthquakes(self):


        with open('data/api_iceland_earthquakes.json') as json_data:
	           data = json.load(json_data,)

        earthquakes_data = data['results']
        earthquakes_count = len(earthquakes_data)

        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(
        """select cast(count(*) as integer) from iceland.earthquakes
        """)
        count = cursor.fetchall()

        if count[0][0] == earthquakes_count:
            print ("Test Cases 1 - Earthquakes - Successful")
            return;
        else:
            print ("Test Cases 1 - Earthquakes - Failed")

    def test_case_one_drivers(self):


        with open('data/api_iceland_samferda_drivers.json') as json_data:
	           data = json.load(json_data,)

        drivers_data = data['results']
        drivers_count = len(drivers_data)

        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(
        """select cast(count(*) as integer) from iceland.drivers
        """)
        count = cursor.fetchall()

        if count[0][0] == drivers_count:
            print ("Test Cases 1 - Drivers - Successful")
            return;
        else:
            print ("Test Cases 1 - Drivers - Failed")

    def test_case_one(self):

        test_case_one = DataModelApiIcelandTestCaseOne()

        test_case_one.test_case_one_concerts()
        test_case_one.test_case_one_earthquakes()
        test_case_one.test_case_one_drivers()
