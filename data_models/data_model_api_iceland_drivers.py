from data_models.data_model import DataModel

class DataModelApiIcelandDrivers(DataModel):
    @property
    def create_statement(self):
        return """
            create table iceland.drivers_base (
                "from" text not null,
                "to" text null,
                "date" date not null,
                "time" varchar(30) default null

            );
        """

    @property
    def drop_statement(self):
        return """
            drop table if exists iceland.drivers_base
        """
