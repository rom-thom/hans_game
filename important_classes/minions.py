import pygame
import sys
sys.path.append("art")
sys.path.append("classes")
from art.animations import Animations, ExecuteAnimation
from classes.general import General
from important_classes.ground import Ground
from random import randint, choice
from classes.timer import Timer





class Minions(pygame.sprite.Sprite, General, ExecuteAnimation):
    def __init__(self, screen, WIDTH, HEIGHT, life_amount, max_life, velocity, acceleration, animation_speed, botom_left_coordinate, animation_instance, minion, min_distance_from_previous_minion=2):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen

        self.back_wards = False

        pygame.sprite.Sprite.__init__(self)
        General.__init__(self, life_amount, max_life, acceleration, velocity)
        ExecuteAnimation.__init__(self)
        self.animation_instance = animation_instance


        self.animation_types = [i for i in self.animation_dict]
        self.image = list(self.animation_dict.values())[0][0].copy()
        self.rect = self.image.get_rect(bottomleft=botom_left_coordinate)

        self.current_animation = self.animation_dict[self.animation_types[0]]
        self.animation_speed = animation_speed

        self.min_distance_from_previous_minion = min_distance_from_previous_minion


    def update(self, ground, dt):
        self.ground = ground
        self.dt = dt

        if __name__=="__main__":
            if self.rect.left < 0:
                self.rect.right = self.WIDTH
                self.execute_movement(just_move_pos=True)

        self.spesific_minion_update()
        self.execute_movement()
        self.execute_animation(self.animation_speed)
        if self.lives <= 0:
            self.kill()
        if self.lives < self.max_lives:
            self.display_normal_life_bar(30, 10)

        # Must see what it is doing and change rect and animation list accordingly
        self.update_damage()


    def spawn_inn(self,screen, WIDTH, HEIGHT, animation_instance, minion_type: int, left_bottom: tuple, velocity=[-300, 0], acceleration=[0, 0], life_amount=1, max_life=1, animation_speed=3, limit_distance_from_last_sprite=False):
        if limit_distance_from_last_sprite and self.all_minions_group.len() > 0: # finn ut korleis du skal bruke alle minion gruppa
            smallest = self.all_minions_group[-1].right() + self.min_distance_from_previous_minion
            return Minions.__init__(self, screen, WIDTH, HEIGHT, life_amount=life_amount, max_life=max_life, velocity=velocity, acceleration=acceleration, animation_speed=animation_speed, botom_left_coordinate=(randint(int(smallest), int(WIDTH*1.38)), left_bottom[1]), animation_instance=animation_instance, minion=minion_type)
        else:
            return Minions.__init__(self, screen, WIDTH, HEIGHT, life_amount=life_amount, max_life=max_life, velocity=velocity, acceleration=acceleration, animation_speed=animation_speed, botom_left_coordinate=left_bottom, animation_instance=animation_instance, minion=minion_type)
        
        

class DavidMinions(Minions):
    def __init__(self, screen, WIDTH, HEIGHT, animation_instance):
        self.animation_dict = animation_instance.all_minion_animation_dicts_list[0]
        #super().__init__(screen, WIDTH, HEIGHT, life_amount=1, max_life=1, velocity=[-300, 0], acceleration=[0, 0], animation_speed=2, botom_left_coordinate=(randint(int(WIDTH*1.32), int(WIDTH*1.38)), int(HEIGHT/4*3+40)), animation_instance=animation_instance, minion=0)
        self.spawn_inn(screen, WIDTH, HEIGHT, animation_instance, minion_type=0, left_bottom=(randint(int(WIDTH*1.32), int(WIDTH*1.38)), int(HEIGHT/4*3+40)), animation_speed=2)

        self.crawling = True

    def spesific_minion_update(self):
        self.update_animation()

    def update_animation(self):
        if self.crawling:
            self.current_animation = self.animation_dict["crawling"]
        if self.back_wards:
            self.current_animation = self.turn_around(self.current_animation)
    
        

class ThomasMinions(Minions):
    def __init__(self, screen, WIDTH, HEIGHT, animation_instance):
        self.animation_dict = animation_instance.all_minion_animation_dicts_list[1]
        self.spawn_inn(screen, WIDTH, HEIGHT, animation_instance, left_bottom=(randint(int(WIDTH*1.25), int(WIDTH*1.38)), choice([int(HEIGHT*0.5), int(HEIGHT*0.65)])), minion_type=1)

        self.flying = True

    def spesific_minion_update(self):
        self.update_animation()

    def update_animation(self):
        if self.flying:
            self.current_animation = self.animation_dict["flying"]
        if self.back_wards:
            self.current_animation = self.turn_around(self.current_animation)


import time
class Main():
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 500
        self.dt = 0
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.animations = Animations((self.WIDTH, self.HEIGHT))
        self.ground = Ground(self.screen, (self.WIDTH, self.HEIGHT), self.animations, [-50, 0])

        self.david_minions = DavidMinions(self.screen, self.WIDTH, self.HEIGHT, self.animations)
        self.thomas_minion = ThomasMinions(self.screen, self.WIDTH, self.HEIGHT, self.animations)
        self.minion_group = pygame.sprite.Group()
        self.minion_group.add(self.david_minions)
        self.minion_group.add(self.thomas_minion)
        self.start_time = time.time()


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
            self.ground.update_ground(self.dt)

            
            self.minion_group.update(self.ground, self.dt)
            self.minion_group.draw(self.screen)

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(200)
if __name__ == "__main__":
    runn = Main()
    runn.loop()
        
