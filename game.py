import sys
sys.path.append("important_classes")
sys.path.append("classes")
sys.path.append("art")
sys.path.append("progres_stored")
from important_classes.levels import Levels
from art.display import BackGround, Display, display_text
from art.animations import Animations, ExecuteAnimation
from classes.bindings import GlobalBindings
from important_classes.player import Player
from important_classes.ground import Ground
from classes.only_once import OnlyOnce
from progres_stored.account import Account
import pygame

class Game(Display, BackGround, GlobalBindings, Levels, ExecuteAnimation, Account):
    def __init__(self):

        self.animations = Animations(screen_size=(self.WIDTH, self.HEIGHT))
        ExecuteAnimation.__init__(self)
        Display.__init__(self)
        BackGround.__init__(self)
        GlobalBindings.__init__(self)
        Account.__init__(self)

        Levels.__init__(self, current_level=1, max_level=12)

        self.ground = Ground(self.screen, (self.WIDTH, self.HEIGHT), self.animations, [-200, 0])

        self.display_in_game_background()
        self.ground.update_ground(self.dt)

        # Pygame Groups
        self.all_minions_group = pygame.sprite.Group()
        self.all_boss_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.wind_group = pygame.sprite.Group()
        self.player_group.add(Player(self.screen, self.WIDTH, self.HEIGHT, self.animations, self.ground, life_amount=1, max_life=1, max_level=self.max_level, acceleration=[0, 3000], velocity=[0, 0], can_crouch=True, jump_amount=2, jump_strength=800, wind_group=self.wind_group, position_top_left=(200, 200)))
        
        
        # Menu states
        self.stop = True
        self.main_menu = True
        self.level_menu = False
        self.pause = False
        self.game_over = False
        self.select_player_animation_menu = False
        self.celebration_menu = False
        self.sign_upp_menu = False
        self.log_in_menu = False

        self.start_current_level = False
        self.skip = False
        # Things to only do once
        


    def in_game_loop(self):
        self.listen_for_key_strokes()
        self.update_account()

        if self.stop:
            self.display_menues(dt=self.dt)
            
        else:
            self.display_in_game_background()
            self.ground.update_ground(self.dt)
            
            if self.start_current_level:
                self.start_current_level_func()
            elif self.start_next_level:
                self.start_next_level_func()
            
            # Updating sprites
            self.player_group.update(ground=self.ground, dt=self.dt, max_level=self.max_level)
            
            self.update_level()



            
            


        