import pygame

class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, screen, screen_size, empty_box_size: tuple, center: tuple, font=None, inactive_color=(0, 100, 100), active_color=(0, 100, 200), border_radius=5, inactive_empty_text="", inactive_empty_text_color=(160, 160, 160), can_use_space=True, secret=False):
        self.screen = screen
        self.WIDTH = screen_size[0]
        self.HEIGHT = screen_size[1]

        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.Font(font, int(empty_box_size[1]))
        self.active = False
        self.text = ""
        self.inactive_empty_text = inactive_empty_text

        self.border_radius = border_radius
        top_left_pos = (center[0]-empty_box_size[0]/2, center[1]-empty_box_size[1]/2)
        self.rect = pygame.Rect((top_left_pos), (empty_box_size))

        self.color_inactive = inactive_color
        self.color_active = active_color
        self.color = inactive_color
        self.inactive_empty_text_color = inactive_empty_text_color

        self.can_use_space = can_use_space

        self.secret = secret

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False
                self.color = self.color_active if self.active else self.color_inactive

            if event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN:
                if self.active:
                    if event.key == pygame.K_SPACE:
                        if self.can_use_space:
                            self.text += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
        

        if self.active or self.text != "":
            if self.secret:
                self.text_surf = self.font.render("*"*len(self.text), True, self.color)
            else:
                self.text_surf = self.font.render(self.text, True, self.color)
        else:
            self.text_surf = self.font.render(self.inactive_empty_text, True, self.inactive_empty_text_color)

        self.rect.width = max(self.WIDTH*0.25, self.text_surf.get_width()+10)


        self.screen.blit(self.text_surf, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(self.screen, self.color, self.rect, 3, border_radius=self.border_radius)
        return self.text









import time
class Main():
    def __init__(self):
        pygame.init()

        self.WIDTH = 900
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()


        self.text_box = TextInputBox(self.screen, (self.WIDTH, self.HEIGHT), (200, 30), (400, 200), inactive_empty_text="Username")

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
            self.screen.fill((200, 200, 200))

            text_info = self.text_box.update(self.events)
            if text_info != None:
                print(text_info)


            pygame.display.update()
            pygame.display.flip()


if __name__ == "__main__":
    runn = Main()
    runn.loop()





