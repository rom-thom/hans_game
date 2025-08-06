import pygame
import sys
sys.path.append("art")
from art.animations import Animations, ExecuteAnimation
from classes.general import General
from classes.only_once import OnlyOnce

    
    

class Projectile(pygame.sprite.Sprite, Animations, General):
    def __init__(self, screen, screen_size, velocity: list, acceleration: list, center_pos: tuple, animation_dict: dict, animation_speed, hostile_for_player=False, acceleration_acceleration=[0, 0], life_amount=1, max_life=1, projectile_size: float=None, kill_if_of_screen=True):
        self.screen = screen
        self.WIDTH = screen_size[0]
        self.HEIGHT = screen_size[1]

        self.kill_if_of_screen = kill_if_of_screen

        self.collide_with_player = OnlyOnce()
        
        self.animation_dict = animation_dict.copy()
        if projectile_size != None:
            for animation_type in self.animation_dict:
                self.animation_dict[animation_type] = [pygame.transform.scale(image, (0.625*projectile_size, 0.781*projectile_size))for image in self.animation_dict[animation_type].copy()]
        self.current_animation = self.animation_dict["normal"]
        self.animation_speed = animation_speed

        self.hostile_for_player = hostile_for_player

        self.image = self.current_animation[0].copy()
        self.rect = self.image.get_rect(center=center_pos)

        # Initialise
        pygame.sprite.Sprite.__init__(self)
        General.__init__(self, life_amount, max_life, acceleration, velocity, acceleration_acceleration=acceleration_acceleration)


    def update(self, dt):
        self.dt = dt
        self.execute_movement()
        if self.kill_if_of_screen and self.outside_of_screen():
            self.kill()
        self.spesific_boss_update()
        self.execute_animation(self.animation_speed)
        self.screen.blit(self.image, self.rect)
    
    def outside_of_screen(self):
        return self.rect.left > self.WIDTH or self.rect.right < 0 or self.rect.bottom < 0 or self.rect.top > self.HEIGHT




class Wind(Projectile, ExecuteAnimation):
    def __init__(self, screen, screen_size, animations_instance: Animations, animation_speed: list, velocity: list, acceleration: list, center_pos: tuple, hostile_for_player, wind_size: float = None, acceleration_acceleration=[0, 0], kill_if_of_screen=True):
        ExecuteAnimation.__init__(self)
        Projectile.__init__(self, screen, screen_size, velocity, acceleration, center_pos, animations_instance.wind_animation_dict, animation_speed, hostile_for_player=hostile_for_player, acceleration_acceleration=acceleration_acceleration, projectile_size=wind_size, kill_if_of_screen=kill_if_of_screen)
        
    def spesific_boss_update(self):
        pass
        


        
        
import time
class LocalMain():
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.animations = Animations((self.WIDTH, self.HEIGHT))

        self.wind = Wind(self.screen, (self.WIDTH, self.HEIGHT), self.animations, 3, [-200, 100], [0, 0], (self.WIDTH/2, self.HEIGHT/2), hostile_for_player=False)
        self.wind2 = Wind(self.screen, (self.WIDTH, self.HEIGHT), self.animations, 3, [-100, 100], [0, 0], (self.WIDTH/2, self.HEIGHT/2), hostile_for_player=False)
        

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

            self.wind.update(self.dt)
            self.wind2.update(self.dt)




            pygame.display.update()

            pygame.display.flip()
            

            self.clock.tick(60)


if __name__ == "__main__":
    runn = LocalMain()
    runn.loop()
        