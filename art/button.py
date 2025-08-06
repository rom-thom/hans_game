import pygame

class Button():
    def __init__(self, screen, text: str, width: float, height: float, pos: tuple, text_size=30, font="art/font\Canterbury.ttf", text_color=(255, 255, 255), hover_text_color=(255, 255, 255), default_bg_color=(90, 90, 80), border_radius=8, hover_color=(255, 0, 0), press_height=5, disabled_color=(110, 110, 110), disabled_text_color=(200, 200, 200)):
        
        text_font = pygame.font.Font(font, text_size)
        self.screen = screen
        self.width = width
        self.height = height

        # color
        self.top_color = default_bg_color
        self.top_color_default = default_bg_color
        self.hover_color = hover_color
        self.bottom_color = default_bg_color
        self.disabled_color = disabled_color

        # text
        self.text_info = text
        self.text_image = text_font.render(text, True, text_color)
        self.text_image_default = text_font.render(text, True, text_color)
        self.hover_text_image = text_font.render(text, True, hover_text_color)
        self.disabled_text_image = text_font.render(text, True, disabled_text_color)
        self.border_radius = border_radius

        # Top rect
        self.top_rect = pygame.Rect(pos, (width, height))
        
        self.top_rect_default = pygame.Rect((pos[0]+abs(press_height)/2, pos[1]-abs(press_height)), (width, height))
        
        self.text_rect = self.text_image.get_rect(center=self.top_rect.center)
        self.default_y_pos = pos[1]
        self.default_x_pos = pos[0]

        # Bottom rect
        self.bottom_rect = pygame.Rect(pos, (width, height))

        # Click
        self.cliked = False
        self.press_height = abs(press_height)
        self.press_height_default = abs(press_height)

        # Image
        self.locked_image = pygame.image.load("art\general_art\pngegg.png")
        self.locked_image.set_alpha(200)
        
        self.locked_image = pygame.transform.scale(self.locked_image, (width/2, height))


    
    def draw_and_check_click(self, new_pos=None):
        if new_pos:
            self.default_y_pos = new_pos[1]
            self.default_x_pos = new_pos[0]
            self.bottom_rect.topleft = new_pos 

        clicking = self.check_click()

        self.top_rect.y = self.default_y_pos - self.press_height
        self.top_rect.x = self.default_x_pos + self.press_height/2
        self.text_rect = self.text_image.get_rect(center=self.top_rect.center)
            
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, border_radius=self.border_radius)
        self.screen.blit(self.text_image, self.text_rect)
        return clicking

    def draw_disabled_button(self, new_pos=None):
        if new_pos:
            self.default_y_pos = new_pos[1]
            self.default_x_pos = new_pos[0]

        self.top_rect.y = self.default_y_pos - self.press_height
        self.top_rect.x = self.default_x_pos + self.press_height/2
        self.text_rect = self.text_image.get_rect(center=self.top_rect.center)
        locked_rect = self.locked_image.get_rect(center=self.top_rect.center)

        pygame.draw.rect(self.screen, self.disabled_color, self.top_rect, border_radius=self.border_radius)
        self.screen.blit(self.disabled_text_image, self.text_rect)
        self.screen.blit(self.locked_image, locked_rect)

    

    def check_click(self):

        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos) or self.top_rect_default.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.bottom_color, self.bottom_rect, border_radius=self.border_radius)
            self.text_image = self.hover_text_image
            self.top_color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                self.cliked = True
                self.press_height = 0
            else:
                if self.cliked:
                    self.press_height = self.press_height_default
                    self.cliked = False
                    return True
        else:
            self.top_color = self.top_color_default
            self.press_height = self.press_height_default
            self.text_image = self.text_image_default
            if self.cliked:
                if not pygame.mouse.get_pressed()[0]:
                    self.cliked = False
                    

        return False
    
    def __repr__(self):
        return "Button saying (" + self.text_info + ")"
