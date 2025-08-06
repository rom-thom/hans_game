from progres_stored.database import DatabaseProgress

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted

class Account(DatabaseProgress):
    def __init__(self):
        DatabaseProgress.__init__(self)
        self.account = [None, None, 0, 0]
        self.name_coresponding_dict = {"CT-7567": "Captain Rex", "CT-27-5555": "Arc Trooper Fives", 
            "CC-2224": "Commander Cody", "CT-21-0408": "Arc Trooper Echo", "CT-1049": "Arc Trooper Echo",
            "CC-5576-39": "Clone Commando Gregor", "CC-3636": "Commander Wolffe", "CT-6116": "Kix", 
            "CT-5597": "Jesse", "CC-8826": "Commander Neyo", "CC-1004": "Commander Gree", "CT-2377": "Commander Oddball",
            "CC-411": "Commander Ponds", "CT-00-2010": "Droidbait", "CT-4040": "Cutup"}
        self.name_coresponding_dict.update(invert_dict(self.name_coresponding_dict))


    def update_account(self):
        if self.account[0] != None:
            self.account[2] = max(self.account[2], self.max_level)
            self.max_level = max(self.account[2], self.max_level)
        
        self.update_account_info()
