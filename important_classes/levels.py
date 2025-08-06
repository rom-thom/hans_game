import pygame
import random
import sys
sys.path.append("classes")
sys.path.append("art")
from art.animations import Animations
from important_classes.levels_general import LevelsGeneral
from important_classes.boss import DavidBoss, ThomasBoss
from important_classes.minions import DavidMinions, ThomasMinions
from classes.only_once import OnlyOnce
from classes.timer import Timer, Timer2
from important_classes.levels_boss import BossLevel1, BossLevel2

class Levels(LevelsGeneral, BossLevel1, BossLevel2):
    def __init__(self, current_level, max_level):
        LevelsGeneral.__init__(self)

        self.current_level = current_level
        self.max_level = max_level
        self.score_color = (0, 0, 0)
        self.score_to_reach = [10, 20]

        # timer
        self.spawn_minion_level_1 = Timer(1)
        self.spawn_minion_level_2 = Timer(1)

        self.end_boss_level_once = OnlyOnce()


    def normal_level_update(self):

        self.display_score((self.WIDTH/2, self.HEIGHT*0.1))
        self.skip_to_boss_level(self.score_to_reach[int(self.current_level)-1])
        

    def update_level_1(self):
        self.normal_level_update()
        if self.spawn_minion_level_1.time_it(self.dt):
            self.all_minions_group.add(DavidMinions(self.screen, self.WIDTH, self.HEIGHT, animation_instance=self.animations))


    def update_boss_level_david(self):
        if self.initiate_boss_prepairing:
            BossLevel1.__init__(self)
        self.update_boss_level_1()


    def update_level_2(self):
        self.normal_level_update()
        if self.spawn_minion_level_2.time_it(self.dt):
            if random.random() > 0.4:
                self.all_minions_group.add(ThomasMinions(self.screen, self.WIDTH, self.HEIGHT, animation_instance=self.animations))
            else:
                self.all_minions_group.add(DavidMinions(self.screen, self.WIDTH, self.HEIGHT, animation_instance=self.animations))

    
    def update_boss_level_thomas(self):
        if self.initiate_boss_prepairing:
            BossLevel2.__init__(self)
        self.update_boss_level_2()
        

        


    def update_level(self):
        if self.max_level < self.current_level:
            self.max_level = self.current_level
        self.update_player_sprites()
        self.update_obstacle_sprites()
        self.update_boss_sprites()
        self.update_projectile_sprites_and_its_player_interaction()
        
        if self.current_level == 1:
            self.update_level_1()
        elif self.current_level == 1.5:
            self.update_boss_level_david()
        elif self.current_level == 2:
            self.update_level_2()
        elif self.current_level == 2.5:
            self.update_boss_level_thomas()
    




