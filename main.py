
import pygame, time
from game import Game


class Main(Game):
    def __init__(self):
        pygame.init()

        self.WIDTH = 900
        self.HEIGHT = 500 
        self.dt = 0

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Hans game")
        hans_icon = pygame.image.load("art\general_art\general_hans_art\hans_face.png")
        pygame.display.set_icon(hans_icon)
        self.clock = pygame.time.Clock()


        
        Game.__init__(self) # Game mecanics to be initialised 



    def loop(self):
        running = True

        previous_time = time.time()
        while running:
            
            self.dt = time.time()-previous_time
            previous_time = time.time()
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    running = False

            self.in_game_loop() # Game mecanics to loop

            pygame.display.update()
            pygame.display.flip() 

            
if __name__ == "__main__":
    runn = Main()
    runn.loop()
