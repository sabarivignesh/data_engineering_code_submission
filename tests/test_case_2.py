import psycopg2
import os
import json

DATABASE_HOST = os.getenv('DB_HOST')
DATABASE_PORT = os.getenv('DB_PORT')
DATABASE_USERNAME = os.getenv('DB_USERNAME')
DATABASE_PASSWORD = os.getenv('DB_PASSWORD')
DATABASE_DBNAME = os.getenv('DB_DBNAME')

class DataModelApiIcelandTestCaseTwo():

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


    def test_case_two_concerts(self):


        with open('data/api_iceland_concerts.json') as json_data:
	           data = json.load(json_data,)

        dateOfShow = []
        temp = []

        for x in range(len(data['results'])):
	           temp = data['results'][x]['dateOfShow']
	           dateOfShow.append(temp)

        total_unique_events = len(set(dateOfShow))

        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(
        """select cast(count(distinct a.timestamp) as integer) from iceland.concerts as a
        """)
        count = cursor.fetchall()

        if count[0][0] == total_unique_events:
            print ("Test Cases 2 - Concerts - Successful")
            return;
        else:
            print ("Test Cases 2 - Concerts - Failed")


    def test_case_two_earthquakes(self):


        with open('data/api_iceland_earthquakes.json') as json_data:
	           data = json.load(json_data,)

        total_size = []
        temp = []

        for x in range(len(data['results'])):
	           temp = data['results'][x]['size']
	           total_size.append(temp)

        max_magnitude = max(total_size)

        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(
        """select max(magnitude) from iceland.earthquakes
        """)
        count = cursor.fetchall()

        if count[0][0] == max_magnitude:
            print ("Test Cases 2 - Earthquakes - Successful")
            return;
        else:
            print ("Test Cases 2 - Earthquakes - Failed")


    def test_case_two_drivers(self):


        with open('data/api_iceland_samferda_drivers.json') as json_data:
	           data = json.load(json_data,)

        fromCity = []
        temp = []

        for x in range(len(data['results'])):
	           temp = data['results'][x]['from']
	           fromCity.append(temp)

        total_unique_departure_city = len(set(fromCity))

        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(
        """select count(distinct a.from) from iceland.samferda_drivers as a
        """)
        count = cursor.fetchall()

        if count[0][0] == total_unique_departure_city:
            print ("Test Cases 2 - Drivers - Successful")
            return;
        else:
            print ("Test Cases 2 - Drivers - Failed")


    def test_case_two(self):

        test_case_two = DataModelApiIcelandTestCaseTwo()

        test_case_two.test_case_two_concerts()
        test_case_two.test_case_two_earthquakes()
        test_case_two.test_case_two_drivers()
