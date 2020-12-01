class Loss:
    
    def __init__(self, day, month, year, details, wizard, item, recovered = False, id = None):
        self.day = day
        self.month = month
        self.year = year
        self.details = details
        self.wizard = wizard
        self.item = item
        self.recovered = recovered
        self.id = id