import sys
sys.path.append("art")
sys.path.append("classes")
from art.animations import Animations, ExecuteAnimation
from classes.movement import Movement
import pygame



class Ground(Movement, ExecuteAnimation):
    def __init__(self, screen, screen_size, animation_instance, velocity, acceleration=[0, 0], acceleration_acceleration=[0, 0]):
        self.screen = screen
        self.WIDTH = screen_size[0]
        self.HEIGHT = screen_size[1]
        self.dt = 0

        ExecuteAnimation.__init__(self)
        Movement.__init__(self, velocity, acceleration, acceleration_acceleration)

        self.animations = animation_instance
        self.ground_animation_dict = self.animations.in_game_ground_dict

        self.image = self.ground_animation_dict["normal"][0].copy()
        self.rect = self.image.get_rect(bottomleft=(0, self.HEIGHT))
        self.behind_rect = self.image.get_rect(topleft=self.rect.topright)


    
    def update_ground(self, dt, velocity=None, acceleration=None, acceleration_acceleration=None):
        self.dt = dt
        if velocity:
            self.velocity = velocity
        if acceleration:
            self.acceleration = acceleration
        if acceleration_acceleration:
            self.acceleration_acceleration = acceleration_acceleration
        if self.rect.right <= 0:
            self.rect.left = 0
            self.execute_movement(just_move_pos=True)
            

        self.execute_movement()
        self.behind_rect.topleft = self.rect.topright
        self.execute_animation(0.2, animation=self.ground_animation_dict["normal"], dt=self.dt)
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image, self.behind_rect)











class Main():
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.animations = Animations((self.WIDTH, self.HEIGHT))

        self.ground = Ground(self.screen, (self.WIDTH, self.HEIGHT), self.animations, [-1, 0])

        

        

    def loop(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((200, 200, 200))

            self.ground.update_ground()


            pygame.display.update()

            pygame.display.flip()
            

            self.clock.tick(60)


if __name__ == "__main__":
    runn = Main()
    runn.loop()

