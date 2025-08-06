
from art.animation_storage import StoredAnimationDictionaries


class Animations(StoredAnimationDictionaries):
    def __init__(self, screen_size=None):
        if screen_size:
            self.WIDTH = screen_size[0]
            self.HEIGHT = screen_size[1]
        self.animation_index = 0

        # Geting stored animations
        StoredAnimationDictionaries.__init__(self)



class ExecuteAnimation:
    def __init__(self):
        self.animation_index = 0
        self.start_once_animation = True
        
    def execute_animation(self, animation_speed, animation=None, back_and_forth=False, dt=None):

        if animation == None:
            animation = self.current_animation

        self.start_once_animation = True
        if dt != None:
            self.dt = dt
        if not back_and_forth:

            self.animation_index += animation_speed*self.dt*len(animation)

            if int(self.animation_index) >= len(animation):
                self.animation_index = 0
            elif self.animation_index < 0:
                self.animation_index = len(animation)-0.0000000000001
            self.image = animation[int(self.animation_index)].copy()

        else:
            long_animation = animation + animation[::-1][1:-1]

            self.animation_index += animation_speed*self.dt*len(long_animation)

            if int(self.animation_index) >= len(long_animation):
                self.animation_index = 0
            elif self.animation_index < 0:
                self.animation_index = len(long_animation)-0.0000000000001
            self.image = long_animation[int(self.animation_index)].copy()
        
    def execute_animation_once(self, animation_speed, animation=None, dt=None):
        # Goes trough the animation once and returns True when it is done and False when it is not
        # This gets reset after executing normal execute_animation() funksjon, so
        # it stays at the final picture until execute_animation() is ran or until you 
        # set self.start_once_animation to True

        if animation == None:
            animation = self.current_animation

        if dt != None:
            self.dt = dt

        if self.start_once_animation:
            self.start_once_animation = False
            self.animation_index_once = 0
        
        if int(self.animation_index_once) < len(animation)-1:
            self.animation_index_once += animation_speed*self.dt*len(animation)
        elif int(self.animation_index_once) > len(animation)-1:
            self.animation_index_once = len(animation)-1
        self.image = animation[int(self.animation_index_once)].copy()

        return int(self.animation_index_once) == len(animation)-1
        





