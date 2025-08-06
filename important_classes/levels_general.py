import sys
sys.path.append("classes")
from classes.only_once import OnlyOnce
import pygame
from important_classes.boss import DavidBoss, ThomasBoss
from important_classes.minions import DavidMinions, ThomasMinions

class LevelsGeneral:
    def __init__(self):
        # Things to only do once
        self.only_get_damaged_from_minion_once = [OnlyOnce() for _ in range(3)] # so that it happens to all players
        self.only_get_damaged_from_boss_once = [OnlyOnce() for _ in range(3)]
        self.thing_lands_on_other_thing_once = OnlyOnce()
        self.initiate_boss_prepairing = True # So that every time boss level starts this will be sett to false after first frame

        self.player_landed_on_boss = [False, False] # Legg til etter kvart som eg legg til fleire bossar
        self.the_player_who_landed_on_boss = None

        # Level score
        self.level_score_list = [0, 0] # Legg til etter kvart som eg legg til fleire level
        self.initial_level_score_list = self.level_score_list.copy()



    def start_current_level_func(self):
        # Player    
        for n, player in enumerate(self.player_group):
            player.remake_after_restart(person=self.account[3], left_coordinate=-150*n**2+250*n+120, lifebar_top_left=(self.WIDTH*1/40, self.HEIGHT*1/25+n*30))
        
        self.all_minions_group.empty() # Clears mobs
        self.all_boss_group.empty()
        self.wind_group.empty()

        if self.current_level - int(self.current_level) == 0:
            self.level_score_list[int(self.current_level)-1] = 0
        
        self.initiate_boss_prepairing = True

        #reset boss

        self.start_current_level = False
        self.start_next_level = False
    

    def start_next_level_func(self):
        self.all_minions_group.empty() # Clears mobs
        self.all_boss_group.empty() # Clear boss
        self.wind_group.empty()
        print("start next level")
        self.start_next_level = False
    

    def skip_to_boss_level(self, score_to_reach):
        if self.level_score_list[int(self.current_level)-1] >= score_to_reach:
            if self.initiate_boss_prepairing:
                self.initiate_boss_prepairing = False
                    

            for minion in self.all_minions_group:
                minion.back_wards = True

                minion.velocity = [600, 0]

                if minion.rect.left > self.WIDTH:
                    minion.kill()

            if len(self.all_minions_group) == 0:
                self.start_next_level = True
                self.update_level_and_maby_max_level()
                self.initiate_boss_prepairing = True


    def thing_lands_on_other_thing(self, thing, other_thing):
        # it does it once
        
        lands_on = other_thing.rect.top - 20 < thing.rect.bottom < other_thing.rect.top and other_thing.rect.left + 10 < thing.rect.right and other_thing.rect.right > thing.rect.left and thing.velocity[1] > 0
        return self.thing_lands_on_other_thing_once.dew_it(lands_on)




    def update_obstacle_sprites(self):
        for minion in self.all_minions_group:
            if minion.rect.right < 0:
                minion.kill()
            for player in self.player_group:    
                if self.thing_lands_on_other_thing(player, minion):
                    if isinstance(minion, DavidMinions):
                        player.velocity[1] = -250
                        minion.take_damage()
                        self.level_score_list[int(self.current_level)-1] += 1
                    elif isinstance(minion, ThomasMinions):
                        minion.take_damage()
                        player.velocity[1] = -250
                        if minion.rect.bottom == self.HEIGHT*0.65:
                            self.level_score_list[int(self.current_level)-1] += 2
                        elif minion.rect.bottom == self.HEIGHT*0.5:
                            self.level_score_list[int(self.current_level)-1] += 3
                        else:
                            print("Thomas er verken høgt oppe eller lavt nede")
        self.all_minions_group.update(ground=self.ground, dt=self.dt)
        self.all_minions_group.draw(self.screen)

    
    def update_boss_sprites(self):
        self.player_landed_on_boss = [False for _ in self.player_landed_on_boss]
        self.the_player_who_landed_on_boss = None
        for boss in self.all_boss_group:
            for player in self.player_group:
                if self.thing_lands_on_other_thing(player, boss):
                    self.the_player_who_landed_on_boss = player
                    if isinstance(boss, DavidBoss):
                        self.player_landed_on_boss[0] = True
                    elif isinstance(boss, ThomasBoss):
                        self.player_landed_on_boss[1] = True
                        
        self.all_boss_group.update(self.dt, self.ground)
        self.all_boss_group.draw(self.screen)


    def update_player_sprites(self):
        all_players_are_dead = True # So that if i go trough all players and none converts this value, all are dead 

        for n, player in enumerate(self.player_group):
            if player.update_player:
                all_players_are_dead = False
                if self.only_get_damaged_from_minion_once[n].dew_it(pygame.sprite.spritecollide(player, self.all_minions_group, False)):
                    player.take_damage()
                if self.only_get_damaged_from_boss_once[n].dew_it(pygame.sprite.spritecollide(player, self.all_boss_group, False)):
                    player.take_damage()

        if all_players_are_dead:
            self.stop = True
            self.game_over = True
    
    def update_projectile_sprites_and_its_player_interaction(self):
        self.wind_group.update(self.dt)
        for player in self.player_group:
            if player.update_player:
                for wind_sprite in self.wind_group:
                    if wind_sprite.collide_with_player.dew_it(pygame.sprite.collide_rect(player, wind_sprite)) and wind_sprite.hostile_for_player:
                        player.stunned = True


    def display_score(self, center_pos: tuple, text_color=(0, 0, 0), font=None, text_size=50):
        text_font = pygame.font.Font(font, text_size)
        image = text_font.render(f"Score: {self.level_score_list[int(self.current_level)-1]}", True, text_color)
        rect = image.get_rect(center=center_pos)
        self.screen.blit(image, rect)
    
    def update_level_and_maby_max_level(self):
        self.current_level += 0.5
        if self.max_level < self.current_level:
            self.max_level = self.current_level
        