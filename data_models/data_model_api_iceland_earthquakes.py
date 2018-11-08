from data_models.data_model import DataModel

class DataModelApiIcelandEarthquakes(DataModel):
    @property
    def create_statement(self):
        return """
            create table iceland.earthquakes (
                latitude real not null,
                longitude real not null,
                magnitude float(2) not null,
                timestamp timestamp not null

            );
        """

    @property
    def drop_statement(self):
        return """
            drop table if exists iceland.earthquakes
        """
