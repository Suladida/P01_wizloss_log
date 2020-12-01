class Loss:
    
    def __init__(self, date, details, wizard_id, item_id, recovered = False, id = None):
        self.date = date
        self.details = details
        self.wizard_id = wizard_id
        self.item_id = item_id
        self.recovered = recovered
        self.id = id