

class OnlyOnce:
    # While presing a button it makes it only do the ting once until you release it
    def __init__(self):
        self.done = False
    
    def dew_it(self, thing: bool):
        if not self.done and thing:
            self.done = True
            return True
        elif thing:
            return False
        else:
            self.done = False
            return False


    