from classes.movement import Movement
from classes.lives import Lives


class General(Lives, Movement):
    def __init__(self, life_amount, max_life, acceleration: list, velocity: list, acceleration_acceleration=[0, 0]):
        Lives.__init__(self, life_amount, max_life)
        Movement.__init__(self, velocity, acceleration, acceleration_acceleration)













    


    




    

