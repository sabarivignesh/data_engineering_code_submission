from data_models.data_model import DataModel
import psycopg2
import os

DATABASE_HOST = os.getenv('DB_HOST')
DATABASE_PORT = os.getenv('DB_PORT')
DATABASE_USERNAME = os.getenv('DB_USERNAME')
DATABASE_PASSWORD = os.getenv('DB_PASSWORD')
DATABASE_DBNAME = os.getenv('DB_DBNAME')

class DataModelApiIcelandDriversCustom():

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



    def create_drivers(self):

        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(
        """
            create table iceland.samferda_drivers as
            select x.from, x.to, to_timestamp(extract(epoch from (x.date+x.time)))::timestamp without time zone as timestamp
            from
            (select a.from, a.to, a.date, to_timestamp(case when lower(a.time) like 'any%' then '01:00:00' when lower(a.time) like 'morning%' then '09:00:00' when lower(a.time) like 'afternoon%' then '13:00:00' when lower(a.time) like 'evening%' then '18:00:00' when lower(a.time) like '%am' then case when lower(a.time) like '1%' then '01:00:00'
	when lower(a.time) like '2%' then '02:00:00'
	when lower(a.time) like '3%' then '03:00:00'
	when lower(a.time) like '4%' then '04:00:00'
	when lower(a.time) like '5%' then '05:00:00'
	when lower(a.time) like '6%' then '06:00:00'
	when lower(a.time) like '7%' then '07:00:00'
	when lower(a.time) like '8%' then '08:00:00'
	when lower(a.time) like '9%' then '09:00:00'
	when lower(a.time) like '10%' then '10:00:00'
	when lower(a.time) like '11%' then '11:00:00'
	else '00:00:00' end
	when lower(a.time) like '%pm'
	then case when lower(a.time) like '1%' then '13:00:00'
	when lower(a.time) like '2%' then '14:00:00'
	when lower(a.time) like '3%' then '15:00:00'
	when lower(a.time) like '4%' then '16:00:00'
	when lower(a.time) like '5%' then '17:00:00'
	when lower(a.time) like '6%' then '18:00:00'
	when lower(a.time) like '7%' then '19:00:00'
	when lower(a.time) like '8%' then '20:00:00'
	when lower(a.time) like '9%' then '21:00:00'
	when lower(a.time) like '10%' then '22:00:00'
	when lower(a.time) like '11%' then '23:00:00'
	else '00:00:00' end else a.time end, 'HH24:MI:SS')::TIME as time from iceland.drivers_base as a
	) as x
        """)
        self.connection.commit()


    def drop_drivers(self):


        self._establish_connection()
        cursor = self.connection.cursor()

        cursor.execute(

         """
            drop table if exists iceland.samferda_drivers
        """)
        self.connection.commit()
