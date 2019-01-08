class Train:
    def __init__(self, id):
        self.id = id
        self.position = 0

    def __str__(self):
        return 'T{}'.format(self.id)

    def __repr__(self):
        return 'T{}'.format(self.id)
