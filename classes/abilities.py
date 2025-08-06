

from classes.projectile import Wind


class Crouch:
    def __init__(self, can_crouch: bool):
        self.can_crouch = can_crouch

    def execute_crouch(self):
        self.is_crouching = True



class Jump():
    def __init__(self, jump_amount, jump_strength):
        self.max_jump_amount = jump_amount
        self.current_jump_amount = jump_amount

        self.jump_strength = jump_strength

    
    def execute_jump(self, ground, just_jump=False):
        
        if not self.tuching_ground_before_jump and not just_jump:
            self.execute_blow(self.wind_group, velocity=[0, 800], acceleration=[0, 100], hostile_for_players=False)

        self.rect.bottom -= 1 # To make shure it does jump when you press jump, and it doesn't loose its velosity due to tuching of ground
        self.execute_movement(just_move_pos=True)

        self.velocity[1] -= self.jump_strength
        self.current_jump_amount -= 1



class Blow:
    def __init__(self):
        self.Wind = Wind

    def execute_blow(self, wind_group, velocity:list, acceleration, hostile_for_players, wind_size=64, kill_if_of_screen=True):
        center_pos = [None, None]
        if velocity[0] > 0:
            center_pos[0] = self.rect.right + wind_size*0.625/2
        elif velocity[0] == 0:
            center_pos[0] = self.rect.centerx
        elif velocity[0] < 0:
            center_pos[0] = self.rect.left - wind_size*0.625/2

        if velocity[1] > 0:
            center_pos[1] = self.rect.bottom + wind_size*0.781/2
        elif velocity[1] == 0:
            center_pos[1] = self.rect.centery
        elif velocity[1] < 0:
            center_pos[1] = self.rect.top - wind_size*0.781/2

        wind_group.add(self.Wind(self.screen, (self.WIDTH, self.HEIGHT), self.animations, animation_speed=3, velocity=velocity, acceleration=acceleration, center_pos=center_pos, hostile_for_player=hostile_for_players, wind_size=wind_size, kill_if_of_screen=kill_if_of_screen))









