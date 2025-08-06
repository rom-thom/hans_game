from important_classes.boss import DavidBoss, ThomasBoss
from classes.timer import Timer, Timer2
from classes.only_once import OnlyOnce
import random
import pygame

class BossLevel1:
    def __init__(self):
        self.initiate_boss_prepairing = False

        self.all_boss_group.add(DavidBoss(self.screen, self.animations, (self.WIDTH, self.HEIGHT), botom_left_pos=(self.WIDTH, self.ground.rect.top)))  
        self.boss_level_1_aproach = True
        self.boss_level_1_lure_stage = False
        self.boss_level_1_timer_for_lure_before_charge = [Timer(4), Timer(5), Timer(6)]
        self.boss_level_1_charge = False
        self.boss_level_1_retreat = False
        self.boss_level_1_level_speed = [[-300, 0], [-500, 0], [-700, 0]]


    def update_boss_level_1(self):
        for boss in self.all_boss_group:
            if self.boss_level_1_aproach and boss.lives > 0:
                if boss.move_to(right=self.WIDTH, centery=self.ground.rect.top, speed=60):
                    boss.velocity = [0, 0]
                    self.boss_level_1_aproach = False
                    self.boss_level_1_lure_stage = True

            elif self.boss_level_1_lure_stage and boss.lives > 0:
                if random.choice([True, False]) and boss.rect.left > self.WIDTH*0.6 or boss.rect.left > self.WIDTH*0.9:
                    boss.rect.x -= 3
                else:
                    boss.rect.x += 3
                boss.execute_movement(just_move_pos=True)

                if self.boss_level_1_timer_for_lure_before_charge[-boss.lives+3].time_it(self.dt):
                    self.boss_level_1_lure_stage = False
                    self.boss_level_1_charge = True
                
            elif self.boss_level_1_charge and boss.lives > 0:
                boss.velocity = self.boss_level_1_level_speed[-boss.lives+3]

                if self.player_landed_on_boss[0] or boss.rect.right < 0:
                    self.boss_level_1_retreat = True
                    self.boss_level_1_charge = False
                    boss.velocity = [800, 0]
                    boss.back_wards = True

                    if self.player_landed_on_boss[0]:

                        self.the_player_who_landed_on_boss.velocity[1] = -600
                        boss.take_damage()
                        if boss.lives <= 0:
                            pass
                            # Her skal eg endre animasjonen til dødsanimasjon
            
            elif self.boss_level_1_retreat and boss.lives > 0:
                if boss.rect.right >= self.WIDTH:
                    boss.velocity = [0, 0]
                    self.boss_level_1_lure_stage = True
                    self.boss_level_1_retreat = False
                    boss.back_wards = False
            
            if boss.lives <= 0:
                if boss.rect.right >= self.WIDTH:
                    boss.dying = True
                    boss.velocity = [0, 100]
                    if boss.rect.top > self.HEIGHT:
                        boss.kill()
                        self.update_level_and_maby_max_level()
                        self.celebration_menu = True
                        self.stop = True
                      
                else:
                    boss.velocity = [800, 0]
    





class BossLevel2:
    def __init__(self):
        #self.boss_level_2 = None
        self.initiate_boss_prepairing = False

        self.all_boss_group.add(ThomasBoss(self.screen, self.animations, (self.WIDTH, self.HEIGHT), botom_left_pos=(self.WIDTH*1.2, self.ground.rect.top-self.HEIGHT*0.3)))
        self.boss_level_2_approach = True
        self.boss_level_attack_stage_nr = [False, False, False]
        self.boss_level_2_charge = False
        self.boss_level_2_retreat = False
        self.boss_level_2_damaged_player = False
        self.boss_level_2_blow_count = 0
        self.boss_level_2_laughter = False

        self.boss_level_2_blowing = False
        self.boss_level_2_blowing_stage = False # For stage 2
        self.boss_level_2_move_upp = False

        # Timers
        self.boss_level_2_timer_for_blowing = Timer(0.6)

        # Only once
        self.boss_level_2_only_blow_wind_forward_once = OnlyOnce()
        self.boss_level_2_only_blow_wind_upp_or_down_once = OnlyOnce()
        
    def update_boss_level_2(self):
        for boss in self.all_boss_group:
            if self.boss_level_2_approach and boss.lives >= 3:
                if boss.move_to(100, bottom=boss.rect.bottom, left=self.WIDTH*0.6):
                    # La thomas snakke
                    if self.skip: # eller dersom eg er ferdig å snakke
                        self.boss_level_2_approach = False
                        self.boss_level_attack_stage_nr[0] = True
                        self.boss_level_2_charge = True

            elif self.boss_level_attack_stage_nr[0]:
                stage_1_finished = self.boss_level_2_first_stage(boss)
                if stage_1_finished:
                    if boss.lives < 3:
                        self.boss_level_attack_stage_nr[0] = False
                        self.boss_level_attack_stage_nr[1] = True
                        # Setting upp stage 2
                        self.boss_level_2_approach=True
                        boss.blowing = True
                        boss.flying = False
                        boss.blowing_direction = [0, 0]
                    else:
                        self.boss_level_2_laughter = True



            elif self.boss_level_attack_stage_nr[1]:
                if not self.boss_level_2_laughter and self.boss_level_2_second_stage(boss):
                    if boss.lives < 2:
                        self.boss_level_attack_stage_nr[1] = False
                        self.boss_level_attack_stage_nr[2] = True
                        # Setting upp level 3:
                        self.boss_level_2_approach=True
                            #meir
                    else:
                        self.boss_level_2_laughter = True
                


            elif self.boss_level_attack_stage_nr[1]:
                if not self.boss_level_2_laughter and self.boss_level_2_third_stage(boss):
                    if boss.lives < 1:
                        #Han er død
                        pass
                    else:
                        self.boss_level_2_laughter = True
        

            if self.boss_level_2_laughter: # Ha ha ha ha ha ha ha ha ha
                # spel thomas' latter lyd
                if True: # if latteren er ferdig:
                    if self.boss_level_attack_stage_nr[0]:
                        self.boss_level_2_charge = True
                    self.boss_level_2_laughter = False



    def boss_level_2_first_stage(self, boss):
        if self.boss_level_2_charge:
            self.boss_level_2_do_charge(boss)
            
            if self.player_landed_on_boss[1]:
                boss.take_damage()
                self.the_player_who_landed_on_boss.velocity[1] = -600
                self.boss_level_2_charge = False
                self.boss_level_2_retreat = True
                boss.back_wards = True
            else:
                for player in self.player_group:
                    if player.is_being_damaged:
                        boss.back_wards = True
                        self.boss_level_2_charge = False
                        self.boss_level_2_retreat = True


        elif self.boss_level_2_retreat:
            boss.acceleration = [0, 0]
            if boss.move_to(900, bottom=self.ground.rect.top-self.HEIGHT*0.3, left=self.WIDTH*0.6):

                boss.back_wards = False
                boss.velocity = [0, 0]
                self.boss_level_2_retreat = False
                return True

        return False


    def boss_level_2_second_stage(self, boss):
        if self.boss_level_2_approach:
            # is going to talk
            if boss.move_to(100, top=self.HEIGHT*0.4, right=self.WIDTH):# and is finished talking
                self.boss_level_2_approach = False
                self.boss_level_2_blowing_stage = True
                all_players_stunned = False
                self.skipp_a_blow = False
                self.player_level_2_move_to_start = False
                boss.velocity = [0, 0]
        elif self.boss_level_2_blowing_stage:
            if self.boss_level_2_timer_for_blowing.time_it(self.dt):
                self.boss_level_2_move_upp = random.choice([True, False])
                self.boss_level_2_only_blow_wind_forward_once.done = False
                self.boss_level_2_only_blow_wind_upp_or_down_once.done = False
                boss.start_once_animation = True # Slik at animasjonen til bossen startar igjen
            boss.animation_once = True

            def move_upp_or_down_and_blow_forward(down):
                boss.animation_speed = 9
                boss.blowing = True
                
                if not boss.move_to(1000, bottom=self.HEIGHT*(0.6+0.3*down), right=self.WIDTH):
                    if self.boss_level_2_only_blow_wind_upp_or_down_once.dew_it(True):
                        boss.execute_blow(self.wind_group, velocity=[0, 900-1800*down], acceleration=[0, 0], hostile_for_players=True, wind_size=self.WIDTH*0.12)
                    boss.blowing_direction = [0, 1-2*down]
                else:
                    if self.boss_level_2_only_blow_wind_forward_once.dew_it(True):
                        if not self.skipp_a_blow:
                            boss.execute_blow(self.wind_group, velocity=[-600, 0], acceleration=[0, 0], hostile_for_players=True, wind_size=self.WIDTH*0.12)
                            self.boss_level_2_blow_count += 1
                        else:
                            self.skipp_a_blow = False
                    boss.blowing_direction = [-1, 0]
                    boss.velocity = [0, 0]

            all_players_stunned = False
            for player in self.player_group:
                if player.stunned != False and player.update_player:
                    all_players_stunned = True
            
            if self.boss_level_2_charge:
                if self.player_landed_on_boss[1]:
                    boss.take_damage()
                    self.the_player_who_landed_on_boss.velocity[1] = -600
                    self.boss_level_2_charge = False
                    boss.charging = False
                    boss.flying = True
                    self.boss_level_2_retreat = True
                    boss.back_wards = True
                    self.boss_level_2_blow_count = 0
                else:
                    for player in self.player_group:
                        if player.is_being_damaged:
                            boss.back_wards = True
                            boss.charging = False
                            boss.flying = True
                            self.boss_level_2_charge = False
                            self.boss_level_2_retreat = True
                            self.boss_level_2_blow_count = 0
            
            if all_players_stunned or self.boss_level_2_blow_count >= 10:
                self.boss_level_2_charge = True
                self.skipp_a_blow = True

                if all_players_stunned:
                    for player in self.player_group:
                        boss.rect.top = player.rect.top-20
                    boss.velocity = [-300, 0]
                    boss.flying = False
                    boss.blowing = False
                    boss.charging = True
                else:
                    self.boss_level_2_do_charge(boss)

                for player in self.player_group:
                    if player.is_being_damaged:
                        self.player_level_2_move_to_start = True
            else:

                move_upp_or_down_and_blow_forward(self.boss_level_2_move_upp)

        if self.boss_level_2_retreat:
            boss.acceleration = [0, 0]
            if boss.move_to(900, bottom=self.ground.rect.top-self.HEIGHT*0.3, left=self.WIDTH*0.6):
                boss.flying = True
                boss.back_wards = False
                boss.velocity = [0, 0]
                self.boss_level_2_retreat = False
                return True
        
        #boss.execute_blow(self.wind_group, velocity=[-100, 100], acceleration=[0, 0], hostile_for_players=True, wind_size=self.WIDTH*0.1)
        return False

    def boss_level_2_third_stage(self, boss):
        pass

    def boss_level_2_do_charge(self, boss):
        # Animation
        boss.charging = True
        boss.flying = False
        boss.blowing = False

        for player in self.player_group:
            if boss.rect.top < player.rect.bottom-10:  # Am above
                boss.acceleration[1] = 2000
                boss.velocity[0] = -150

            elif boss.rect.top >= player.rect.bottom-10:  # Am below
                if boss.velocity[1] > 600:
                    boss.velocity[1] = 300

                boss.acceleration[1] = -2000
                boss.velocity[0] = -100
            break
    