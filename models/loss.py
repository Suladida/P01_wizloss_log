class Loss:
    
    def __init__(self, date, time, details, wizard_id, item_id, recovered = False, id = None):
        self.date = date
        self.time = time
        self.details = details
        self.wizard_id = wizard_id
        self.item_id = item_id
        self.recovered = recovered
        self.id = id