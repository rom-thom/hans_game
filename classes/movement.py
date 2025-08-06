
import math
import pygame


class Movement:
    def __init__(self, velocity: list, acceleration: list, acceleration_acceleration=[0, 0]):
        self.velocity = velocity
        self.acceleration = acceleration
        self.acceleration_acceleration = acceleration_acceleration

    
    def execute_movement(self, desimal_movement=True, just_move_pos=False):

        if just_move_pos: # Must be called after changing rect pos
            self.rect_topleft = list(self.rect.topleft)
            return
            
        try:
            self.rect_topleft
        except:
            self.rect_topleft = list(self.rect.topleft)
        

        self.acceleration[0] += self.acceleration_acceleration[0]*self.dt
        self.acceleration[1] += self.acceleration_acceleration[1]*self.dt
        self.velocity[0] += self.acceleration[0]*self.dt
        self.velocity[1] += self.acceleration[1]*self.dt
        if desimal_movement:
            self.rect_topleft[0] += self.velocity[0]*self.dt
            self.rect_topleft[1] += self.velocity[1]*self.dt

            self.rect.topleft = tuple(self.rect_topleft)
        
        else:
            self.rect.x += self.velocity[0]*self.dt
            self.rect.y += self.velocity[1]*self.dt

            self.rect_topleft = list(self.rect.topleft)

    def move_to(self, speed, top=None, centerx=None, bottom=None, left=None, centery=None, right=None):
        # Returns True if it is where it is supposed to be on

        top_left_pos = [None, None]
        if top != None:
            top_left_pos[1] = top
        elif centery != None:
            top_left_pos[1] = centery-self.rect.height/2
        elif bottom != None:
            top_left_pos[1] = bottom-self.rect.height
        if left != None:
            top_left_pos[0] = left
        elif centerx != None:
            top_left_pos[0] = centerx-self.rect.width/2
        elif right != None:
            top_left_pos[0] = right - self.rect.width
        top_left_pos = tuple(top_left_pos)
        if any([True for i in top_left_pos if i == None]):
            raise Error("There must be 1 value for both x and y position that is to be traveled to")
        


        try:
            self.rect_topleft
        except:
            self.rect_topleft = list(self.rect.topleft)
        
        if self.rect_topleft == top_left_pos:
            return True

        direction = [top_left_pos[0]-self.rect_topleft[0], top_left_pos[1]-self.rect_topleft[1]]
        length = math.sqrt(direction[0]**2+direction[1]**2)

        length_per_frame = speed*self.dt
        if length <= length_per_frame:
            self.rect.topleft = top_left_pos
            self.execute_movement(just_move_pos=True)
            return True

        direction_with_speed_one = [direction[0]/length, direction[1]/length]

        self.velocity = [direction_with_speed_one[0]*speed, direction_with_speed_one[1]*speed]
        
        return False
        

    def turn_around(self, animation: list, flip_x=True, flip_y = False):
        return [pygame.transform.flip(image.copy(), flip_x=flip_x, flip_y=flip_y) for image in animation]
    


