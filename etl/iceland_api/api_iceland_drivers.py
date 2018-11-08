from etl.etl import LocalJSONFileJob

class ApiIcelandDrivers(LocalJSONFileJob):
    @property
    def path_to_local_source_file(self):
        return 'data/api_iceland_samferda_drivers.json'

    @property
    def schema(self):
        return 'iceland'

    @property
    def table(self):
        return 'drivers_base'

    @property
    def properties_to_extract(self):
        return [
            'from',
            'to',
            'date',
            'time',
        ]
