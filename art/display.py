import pygame
import sys
sys.path.append("art")
sys.path.append("progres_stored")
from art.animations import Animations, ExecuteAnimation
from art.button import Button
from art.text_input import TextInputBox
from progres_stored.database import DatabaseProgress


class Display:
    def __init__(self):
        self.WIDTH = self.WIDTH
        self.HEIGHT = self.HEIGHT

        # Multiple use buttons
        self.back_button = Button(self.screen, "<<", 50, 30, (self.WIDTH*1.1/8, self.HEIGHT*7/50))

        # Menu back_ground
        self.animations.image = self.animations.menu_back_ground_dict["normal"][0]
        self.menu_back_ground_rect = self.animations.menu_back_ground_dict["normal"][0].get_rect(center=(self.WIDTH/2, self.HEIGHT/2))

        # Main menu
        self.levels_button = Button(self.screen, "Play", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*5/40, self.HEIGHT*0.28))
        self.player_amount_button = Button(self.screen, "Select player", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH*0.375, self.HEIGHT*0.4))
        self.log_in_button = Button(self.screen, "Log in", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH*0.375, self.HEIGHT*0.52))
        self.sign_upp_button = Button(self.screen, "Sign in", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH*0.375, self.HEIGHT*0.64))

        # Level menu
        self.level_1_button = Button(self.screen, "Level 1", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*1.5/8, self.HEIGHT*1.3/5))
        self.level_1_boss_button = Button(self.screen, "David boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*1/4, self.HEIGHT*1.8/5), text_size=18)
        self.level_2_button = Button(self.screen, "Level 2", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*1.5/8, self.HEIGHT*2.3/5))
        self.level_2_boss_button = Button(self.screen, "Thomas boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*1/4, self.HEIGHT*2.8/5), text_size=18)
        self.level_3_button = Button(self.screen, "Level 3", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*1.5/8, self.HEIGHT*3.3/5))
        self.level_3_boss_button = Button(self.screen, "Jaran boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*1/4, self.HEIGHT*3.8/5), text_size=18)

        self.level_4_button = Button(self.screen, "Level 4", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*5/8, self.HEIGHT*1.3/5))
        self.level_4_boss_button = Button(self.screen, "4 boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*5.5/8, self.HEIGHT*1.8/5), text_size=18)
        self.level_5_button = Button(self.screen, "Level 5", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*5/8, self.HEIGHT*2.3/5))
        self.level_5_boss_button = Button(self.screen, "5 boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*5.5/8, self.HEIGHT*2.8/5), text_size=18)
        self.level_6_button = Button(self.screen, "Level 6", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*5/8, self.HEIGHT*3.3/5))
        self.level_6_boss_button = Button(self.screen, "6 boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*5.5/8, self.HEIGHT*3.8/5), text_size=18)

        self.list_of_normal_level_buttons = [self.level_1_button, self.level_1_boss_button, self.level_2_button, self.level_2_boss_button,\
                                            self.level_3_button, self.level_3_boss_button, self.level_4_button, self.level_4_boss_button, \
                                            self.level_5_button, self.level_5_boss_button, self.level_6_button, self.level_6_boss_button]
        

        # Game over menu
        self.evil_hans_image = pygame.image.load("art\general_art\general_hans_art\evil_hans.png")
        self.evil_hans_image = pygame.transform.scale(self.evil_hans_image, (self.WIDTH*1/4, self.HEIGHT*2/5))
        self.evil_hans_rect = self.evil_hans_image.get_rect(center=(self.WIDTH*1/2, self.HEIGHT*1.2/5))
        self.game_over_main_menu_button = Button(self.screen, "Main menu", self.WIDTH*0.175, self.HEIGHT*0.12, (self.WIDTH/4, self.HEIGHT*0.6), font=None, hover_color=(0, 0, 0), hover_text_color=(255, 0, 0))
        self.game_over_restart_button = Button(self.screen, "Restart", self.WIDTH*0.175, self.HEIGHT*0.12, (self.WIDTH*0.55, self.HEIGHT*0.6), font=None, hover_color=(0, 0, 0), hover_text_color=(255, 0, 0))

        # Pause menu
        self.pause_main_menu_button = Button(self.screen, "Main menu", self.WIDTH*1/5, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*1/10, self.HEIGHT*0.44))
        self.pause_continue_level_button = Button(self.screen, "Continue", self.WIDTH*1/5, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*1/10, self.HEIGHT*0.28))
        self.pause_restart_level_button = Button(self.screen, "Restart", self.WIDTH*1/5, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*1/10, self.HEIGHT*0.6))

        """# Player amount menu
        self.select_player_buttons = [Button(self.screen, "Player 1", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH*0.375, self.HEIGHT*0.28))]
        self.add_player_button = Button(self.screen, "+", self.WIDTH*0.0625, self.HEIGHT*0.08, (self.WIDTH*0.75, self.HEIGHT*0.76), text_size=50)
        self.remove_player_button = Button(self.screen, "-", self.WIDTH*0.0625, self.HEIGHT*0.08, (self.WIDTH*0.75, self.HEIGHT*0.66), text_size=50)
        self.current_chosen_player_to_choose_animation = 0 # To know which player to give animation to"""

        # Select player animation menu
        self.move_to_right_player = Button(self.screen, ">", self.WIDTH*1/20, self.HEIGHT*3/50, (self.WIDTH*3/4, self.HEIGHT*47/100))
        self.move_to_left_player = Button(self.screen, "<", self.WIDTH*1/20, self.HEIGHT*3/50, (self.WIDTH*1/5, self.HEIGHT*47/100))
        self.player_to_show_in_select_player_menu = 0
        self.stand_animation = ExecuteAnimation()
        self.animation_speed = 1
        self.player_stand_rect = self.animations.all_player_animation_dicts_list[0]["standing"][0].get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        self.button_to_choose_player = [Button(self.screen, f"Choose {i}", self.WIDTH*1/4, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*1/8, self.HEIGHT*4/5))\
                                        for i in ["Hans", "David", "Thomas", "Jaran"]]
        self.chosen_player_animation_list = [0] # Visar kva animasjonar som er valgt til kvar spelar. default er hans og ein spelar

        # Celebration menu
        self.celebration_animation = ExecuteAnimation()
        self.celebration_main_menu_button = Button(self.screen, "Main menu", self.WIDTH*1/5, self.HEIGHT*4/50, (self.WIDTH/4, self.HEIGHT*0.7))
        self.celebration_continue_level_button = Button(self.screen, "Continue", self.WIDTH*1/5, self.HEIGHT*4/50, (self.WIDTH*0.55, self.HEIGHT*0.7))
        self.celebration_text_to_display = ["David"]
        self.celebration_color = [200, 100, 50]
        self.celebration_color_multiplyer = [1, 1, 1]
        self.celebration_confetti_animations = self.animations.confetti["normal"]
        self.celebration_confetti_animation = ExecuteAnimation()
        self.celebration_confetti_animation.image = self.celebration_confetti_animations[0]
        self.celebration_confetti_animation.rects = [self.celebration_confetti_animation.image.get_rect(center=(self.WIDTH/2+(i*2-1)*self.WIDTH*0.2, self.HEIGHT/2)) for i in range(2)]
        self.celebration_confetti_animation_speed = 1
        self.celebration_animation_speed = 1
        self.celebration_animation.rect = self.animations.all_player_animation_dicts_list[0]["celebrating"][0].get_rect(center=(self.WIDTH/2, self.HEIGHT/2-self.HEIGHT*0.04))
        self.celebration_animation.image = self.animations.all_player_animation_dicts_list[0]["celebrating"][0]

        # Log in menu
        self.log_in_error_message = ""
        self.username_log_in_text_box = TextInputBox(self.screen, (self.WIDTH, self.HEIGHT), (200, 40), (self.WIDTH/2, self.HEIGHT*0.45), inactive_empty_text="Username", can_use_space=False)
        self.password_log_in_text_box = TextInputBox(self.screen, (self.WIDTH, self.HEIGHT), (200, 40), (self.WIDTH/2, self.HEIGHT*0.70), inactive_empty_text="Password", can_use_space=False, secret=True)

        # Sign in menu
        self.sign_in_error_message = ""
        self.username_sign_in_text_box = TextInputBox(self.screen, (self.WIDTH, self.HEIGHT), (200, 40), (self.WIDTH/2, self.HEIGHT*0.45), inactive_empty_text="Username", can_use_space=False)
        self.password_sign_in_text_box = TextInputBox(self.screen, (self.WIDTH, self.HEIGHT), (200, 40), (self.WIDTH/2, self.HEIGHT*0.70), inactive_empty_text="Password", can_use_space=False, secret=True)

        self.database = DatabaseProgress()

    def display_menu_background(self):
        if self.game_over:
            self.screen.blit(self.evil_hans_image, self.evil_hans_rect)
            #self.animations.execute_animation(self.stand_animation.menu_back_ground_dict["normal"])
            #self.screen.blit(self.animations.image, self.menu_back_ground_rect)
        else:
            self.execute_animation(animation=self.animations.menu_back_ground_dict["normal"], animation_speed=0.3, dt=self.dt)
            self.screen.blit(self.animations.image, self.menu_back_ground_rect)

    def display_level_menu(self):
        self.display_menu_background()
        display_text(self.screen, "Level Menu", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.back_button.draw_and_check_click():
            self.level_menu = False
            self.main_menu = True

        for n, button in enumerate(self.list_of_normal_level_buttons):
            if n+1 < 2*self.max_level:
                if button.draw_and_check_click():
                    self.current_level = (n)/2 + 1
                    self.level_menu = False
                    self.stop = False
                    self.start_current_level = True
            else:
                button.draw_disabled_button()
        if self.max_level >= 7:
            # Show secret button
            print("Show secret button")
    

    def display_main_menu(self):
        self.display_menu_background()
        display_text(self.screen, "Main Menu", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.levels_button.draw_and_check_click():
            self.main_menu = False
            self.level_menu = True
        if self.player_amount_button.draw_and_check_click():
            self.main_menu = False
            self.select_player_animation_menu = True
        if self.sign_upp_button.draw_and_check_click():
            self.main_menu = False
            self.sign_upp_menu = True
        if self.log_in_button.draw_and_check_click():
            self.main_menu = False
            self.log_in_menu = True


    def display_pause_menu(self):
        self.display_menu_background()
        display_text(self.screen, "Pause", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.pause_main_menu_button.draw_and_check_click():
            self.main_menu = True
            self.pause = False
        if self.pause_continue_level_button.draw_and_check_click():
            self.pause = False
            self.stop = False
        if self.pause_restart_level_button.draw_and_check_click():
            self.pause = False
            self.stop = False
            self.start_current_level = True


    def display_game_over_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.menu_back_ground_rect)
        display_text(self.screen, "You died", (self.WIDTH/2, self.HEIGHT/2), text_color=(255, 0, 0), font=None, text_size=60)
        self.display_menu_background()

        self.level_score_list = self.initial_level_score_list.copy()

        if self.game_over_main_menu_button.draw_and_check_click():
            self.main_menu = True
            self.game_over = False
        if self.game_over_restart_button.draw_and_check_click():
            self.game_over = False
            self.stop = False
            self.start_current_level = True
    
    """def display_select_player_menu(self):
        self.display_menu_background()
        display_text(self.screen, "Player Menu", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.back_button.draw_and_check_click():
            self.main_menu = True
            self.select_player_menu = False
        for number, player in enumerate(self.select_player_buttons):
            if player.draw_and_check_click():
                self.select_player_animation_menu = True
                self.select_player_menu = False
                self.current_chosen_player_to_choose_animation = number # To know which player to give animation

        if len(self.select_player_buttons) < 3 and self.add_player_button.draw_and_check_click():
            self.select_player_buttons.append(Button(self.screen, f"Player {len(self.select_player_buttons)+1}", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH*0.375, self.HEIGHT*0.28+len(self.select_player_buttons)*self.HEIGHT*0.12)))
            self.chosen_player_animation_list.append(0)
        if len(self.select_player_buttons) > 1 and self.remove_player_button.draw_and_check_click():
            self.select_player_buttons.pop(-1)
            self.chosen_player_animation_list.pop(-1)"""



    def display_select_player_animation_menu(self):
        self.display_menu_background()
        display_text(self.screen, "Select your Animation", (self.WIDTH/2, self.HEIGHT*9/50), text_color=(0, 0, 0), text_size=50)
        if self.back_button.draw_and_check_click():
            self.main_menu = True
            self.select_player_animation_menu = False
        if self.move_to_right_player.draw_and_check_click():
            if self.player_to_show_in_select_player_menu < len(self.animations.all_player_animation_dicts_list)-1:
                self.player_to_show_in_select_player_menu += 1
            else:
                self.player_to_show_in_select_player_menu = 0
        if self.move_to_left_player.draw_and_check_click():
            if self.player_to_show_in_select_player_menu > 0:
                self.player_to_show_in_select_player_menu -= 1
            else:
                self.player_to_show_in_select_player_menu = len(self.animations.all_player_animation_dicts_list)-1
                
        self.stand_animation.execute_animation(self.animation_speed, animation=self.animations.all_player_animation_dicts_list[self.player_to_show_in_select_player_menu]["standing"], back_and_forth=True, dt=self.dt)
        self.screen.blit(self.stand_animation.image, self.player_stand_rect)
        if self.button_to_choose_player[self.player_to_show_in_select_player_menu].draw_and_check_click():
            self.account[3] = self.player_to_show_in_select_player_menu
        
    def display_celebration_menu(self):
        self.display_menu_background()
        if self.celebration_continue_level_button.draw_and_check_click():
            self.stop = False
            self.celebration_menu = False
        
        if self.celebration_main_menu_button.draw_and_check_click():
            self.main_menu = True
            self.celebration_menu = False

        self.celebration_confetti_animation.execute_animation(self.celebration_confetti_animation_speed, animation=self.celebration_confetti_animations, dt=self.dt)
        for i in range(2):
            self.screen.blit(self.celebration_confetti_animation.image, self.celebration_confetti_animation.rects[i])

        self.celebration_color[0] += self.celebration_color_multiplyer[0]*0.1
        self.celebration_color[1] += self.celebration_color_multiplyer[1]*1
        self.celebration_color[2] += self.celebration_color_multiplyer[2]*0.5
        for n, i in enumerate(self.celebration_color):
            if i >= 255 or i < 40:
                self.celebration_color_multiplyer[n] *= -1

        display_text(self.screen, "You defeated "+self.celebration_text_to_display[int(self.current_level-1.5)]+"!!!", center_pos=(self.WIDTH/2, self.HEIGHT*0.2), text_color=self.celebration_color, text_size=40)
        self.celebration_animation.execute_animation(self.celebration_animation_speed, animation=self.animations.all_player_animation_dicts_list[self.account[3]]["celebrating"], back_and_forth=True, dt=self.dt)
        self.screen.blit(self.celebration_animation.image, self.celebration_animation.rect)

    def display_log_in_menu(self):
        self.display_menu_background()
        if self.back_button.draw_and_check_click():
            self.main_menu = True
            self.log_in_menu = False
            self.log_in_error_message = ""
            self.username_log_in_text_box.text = ""
            self.password_log_in_text_box.text = ""

        username = self.username_log_in_text_box.update(self.events)
        password = self.password_log_in_text_box.update(self.events)

        event_keys = [event.key for event in self.events if event.type == pygame.KEYDOWN]
        if pygame.K_RETURN in event_keys:
            if username != "" and password != "":
                if self.account[0] == None:
                    self.account = self.database.access_account(username, password)
                    self.log_in_error_message = "Account does not exist" if self.account[0] == None else ""
                else:
                    self.log_in_error_message = "You can't log inn while in another account"

        elif pygame.K_SPACE in event_keys:
            self.log_in_error_message = "You can't use space"

        if self.log_in_error_message != "":
            print(self.log_in_error_message)

        display_text(self.screen, "Log in", (self.WIDTH/2, self.HEIGHT*9/50), text_color=(0, 0, 0), text_size=50)
        display_text(self.screen, "Username", (self.WIDTH/2, self.HEIGHT*0.35), text_color=(0, 0, 0), text_size=30)
        display_text(self.screen, "Password", (self.WIDTH/2, self.HEIGHT*0.60), text_color=(0, 0, 0), text_size=30)


    def display_sign_in_menu(self):
        self.display_menu_background()
        if self.back_button.draw_and_check_click():
            self.main_menu = True
            self.log_in_menu = False
            self.sign_in_error_message = ""
            self.username_sign_in_text_box.text = ""
            self.password_sign_in_text_box.text = ""
        username = self.username_sign_in_text_box.update(self.events)
        password = self.password_sign_in_text_box.update(self.events)

        event_keys = [event.key for event in self.events if event.type == pygame.KEYDOWN]
        if pygame.K_RETURN in event_keys:
            if username != "" and password != "":
                sign_in_info = self.database.check_if_valid_password_and_username_and_signing_in(username, password, self.max_level, self.account[3])
                if sign_in_info[1] == True:
                    self.account = self.database.access_account(username, password)
                else:
                    self.sign_in_error_message = sign_in_info[0]
                    print("Error")

        elif pygame.K_SPACE in event_keys:
            self.sign_in_error_message = "You can't use space"

        """if self.sign_in_error_message != "":
            print(self.sign_in_error_message)"""

        display_text(self.screen, "Sign in", (self.WIDTH/2, self.HEIGHT*9/50), text_color=(0, 0, 0), text_size=50)
        display_text(self.screen, "Username", (self.WIDTH/2, self.HEIGHT*0.35), text_color=(0, 0, 0), text_size=30)
        display_text(self.screen, "Password", (self.WIDTH/2, self.HEIGHT*0.60), text_color=(0, 0, 0), text_size=30)


    def display_menues(self, dt):
        self.dt = dt
        if self.main_menu:
            self.display_main_menu()
        elif self.level_menu:
            self.display_level_menu()
        elif self.pause:
            self.display_pause_menu()
        elif self.game_over:
            self.display_game_over_menu()
        elif self.select_player_animation_menu:
            self.display_select_player_animation_menu()
        elif self.celebration_menu:
            self.display_celebration_menu()
        elif self.log_in_menu:
            self.display_log_in_menu()
        elif self.sign_upp_menu:
            self.display_sign_in_menu()





class BackGround(ExecuteAnimation):
    def __init__(self):
        ExecuteAnimation.__init__(self)

        self.in_game_background_image = self.animations.in_game_background_dict["normal"][0].copy()
    
    def display_in_game_background(self):
        self.execute_animation(animation=self.animations.in_game_background_dict["normal"], animation_speed=2, dt=self.dt)
        self.screen.blit(self.in_game_background_image, (0, 0))


def display_text(screen, text: str, center_pos: tuple, text_color=(255, 255, 255), font="art/font\Canterbury.ttf", text_size=30):
    text_font = pygame.font.Font(font, text_size)
    image = text_font.render(text, True, text_color)
    rect = image.get_rect(center=center_pos)
    screen.blit(image, rect)


def display_bar(screen, width, height, curent, maximum, bar_radius, top_left_pos, top_color, bottom_color):
    bottom_rect = pygame.Rect(top_left_pos, (width, height))
    top_rect = pygame.Rect(top_left_pos, (width*curent/maximum, height))
    pygame.draw.rect(screen, bottom_color, bottom_rect, border_radius=bar_radius)
    pygame.draw.rect(screen, top_color, top_rect, border_radius=bar_radius) 


        

