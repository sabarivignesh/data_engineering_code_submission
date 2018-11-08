from etl.etl import LocalJSONFileJob

class ApiIcelandEarthquakes(LocalJSONFileJob):
    @property
    def path_to_local_source_file(self):
        return 'data/api_iceland_earthquakes.json'

    @property
    def schema(self):
        return 'iceland'

    @property
    def table(self):
        return 'earthquakes'

    @property
    def properties_to_extract(self):
        return [
            'latitude',
            'longitude',
            'size',
            'timestamp',
        ]
