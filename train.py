class Train:
    def __init__(self, id, station_obj):
        self.id = id
        self.station_obj = station_obj
        self.position = 0

    def __str__(self):
        return 'T{}'.format(self.id)

    def __repr__(self):
        return 'T{}'.format(self.id)
