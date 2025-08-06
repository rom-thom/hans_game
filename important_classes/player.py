
import sys
sys.path.append("classes")
sys.path.append("art")

import pygame
from classes.only_once import OnlyOnce
from classes.bindings import PlayerBindings
from classes.general import General
from important_classes.ground import Ground
from classes.abilities import Crouch, Jump, Blow
from art.animations import Animations, ExecuteAnimation


class Player(General, pygame.sprite.Sprite, Crouch, Jump, Blow, PlayerBindings, ExecuteAnimation):
    def __init__(self, screen, WIDTH, HEIGHT, animations, ground, life_amount, max_life, max_level, acceleration: list, velocity: list, can_crouch: bool, jump_amount: int, jump_strength, position_top_left: tuple, wind_group,person=None):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.animations = animations
        self.dt = 0
        self.max_level = max_level
        self.wind_group = wind_group

        self.animation_once = False
        self.animation_executed_once_done = False
        self.send_wind_at_end_of_animation = False

        General.__init__(self, life_amount, max_life, acceleration, velocity)

        ExecuteAnimation.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        # Abilities:
        Crouch.__init__(self, can_crouch)
        Jump.__init__(self, jump_amount, jump_strength)
        Blow.__init__(self)
        PlayerBindings.__init__(self)

        self.ground = ground
        self.tuching_ground = True
        self.tuching_ground_before_jump = False


        self.update_player = True

        if person == None:
            self.animation_dict = self.animations.empty_player.copy()
        else:
            self.animation_dict = self.animations.all_player_animation_dicts_list[person].copy()
        self.image = self.animations.empty_player["running"][0].copy()
        self.rect = self.image.get_rect(topleft=position_top_left)
        self.current_animation = self.animation_dict["running"]
        

        # Things to do only once
        self.only_jump_once = OnlyOnce()

        # Things it is currently doing
        self.is_crouching = False
        self.stunned = False
    

    def update(self, ground, dt, max_level):
        self.ground = ground
        self.dt = dt
        self.max_level = max_level

        
        self.input()
        self.execute_movement()
        self.chosse_and_change_animation()
        self.display_player_life_bar(120, 20)

        self.tuching_ground = self.rect.bottom >= self.ground.rect.top # Must be after self.execute_movement() 
        if self.tuching_ground:
            self.when_tuching_ground()

        self.screen.blit(self.image, self.rect)

        self.add_every_ability()

        if self.lives <= 0:
            self.lives = 0
            self.update_player = False
            return

    def chosse_and_change_animation(self):
        if self.stunned:
            self.animation_once = False
            self.current_animation = self.animation_dict["stunned"]
        elif self.is_crouching:
            self.current_animation = self.animation_dict["crouching"]
        elif self.tuching_ground:
            self.current_animation = self.animation_dict["running"]
        elif self.jump_button_down:
            self.animation_once = True
            if self.tuching_ground_before_jump:
                self.current_animation = self.animation_dict["jumping_ground"]
            else:
                self.current_animation = self.animation_dict["jumping_sky"]
        elif not self.tuching_ground:
            self.animation_once = False
            self.current_animation = self.animation_dict["falling"]

        self.rect = self.current_animation[0].get_rect(bottomleft=self.rect.bottomleft)

        self.execute_movement(just_move_pos=True)
        if self.animation_once:
            self.animation_executed_once_done = self.execute_animation_once(3)
        else:
            self.animation_executed_once_done = False
            self.execute_animation(3, back_and_forth=True)
        self.update_damage()
        if self.is_being_damaged:
            self.stunned = False


    def input(self):
        keys = pygame.key.get_pressed()

        # Crouch
        self.is_crouching = False
        if any([keys[i] for i in self.bindings_dict["crouch"]]):
            if self.can_crouch and self.tuching_ground and not self.stunned:
                self.execute_crouch()
        
        # Jump
        self.jump_button_down = any([keys[i] for i in self.bindings_dict["jump"]])
        if self.only_jump_once.dew_it(self.jump_button_down):
            if self.tuching_ground:
                self.tuching_ground_before_jump = True
            else:
                self.tuching_ground_before_jump = False
            if self.current_jump_amount > 0 and not self.is_crouching and not self.stunned:
                self.execute_jump(self.ground)
        
    
    def add_every_ability(self):
        # Må legge til fleire evner
        if self.max_level >= 2:
            self.can_crouch = True
            if self.max_level >= 3:
                self.max_jump_amount = 2

    def when_tuching_ground(self):
        self.velocity = [0, 0]
        self.rect.bottom = self.ground.rect.top

        self.only_jump_once.done = False
        self.current_jump_amount = self.max_jump_amount

    
    def remake_after_restart(self, person, left_coordinate, lifebar_top_left):
        if person == None:
            self.update_player = False
            self.animation_dict = None
            self.stunned = False
        else:
            self.update_player = True
            self.stunned = False
            self.animation_dict = self.animations.all_player_animation_dicts_list[person]
            self.current_animation = self.animation_dict["running"]
        
            self.rect.bottomleft = (left_coordinate, self.ground.rect.top)
            self.velocity = [0, 0]

            self.execute_movement(just_move_pos=True)
            
            self.lives = self.max_lives
            self.player_top_left_lifebar = lifebar_top_left

            # Bars

        
    

    





import time
class Main():
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.animastions = Animations((self.WIDTH, self.HEIGHT))


        self.ground = Ground(self.screen, (self.WIDTH, self.HEIGHT), self.animastions, [-100, 0])
        self.player = Player(self.screen, self.WIDTH, self.HEIGHT, self.animastions, self.ground, 1, 1, 1, [0, 100], [0, 0], True, 3, 800, (200, 200), wind_group=None, person=0)


    def loop(self):
        running = True
        previous_time = time.time()
        while running:
            self.dt = time.time()-previous_time
            previous_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((200, 200, 200))

            self.player.update(ground=self.ground, dt=self.dt, max_level=7)
            self.ground.update_ground(self.dt)
            

            pygame.display.update()

            pygame.display.flip()


if __name__ == "__main__":
    runn = Main()
    runn.loop()
        


