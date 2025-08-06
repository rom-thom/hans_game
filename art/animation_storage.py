import pygame
import os
from PIL import ImageOps, Image

def importing_image_animations(dir_path:str):
    
    raw_path = r'{}'.format(dir_path)
    animation = []
    #border_animation = []
    for root_dir, cur_dir, files in os.walk(raw_path):
        for i in files:
            animation.append(pygame.image.load(root_dir+ "/" + i))

            #border_animation.append(pygame.image.load(ImageOps.expand(Image.open(root_dir + "/" + i) ,border=1,fill=(255, 0, 0))))

        
    return animation



class StoredAnimationDictionaries:
    def __init__(self):

        # Background
        self.menu_back_ground_dict = {"normal": [pygame.transform.scale(i, (self.WIDTH*3/4, self.HEIGHT*4/5)) for i in importing_image_animations("art/back_ground\menu_background")]}
        self.in_game_background_dict = {"normal": [pygame.transform.scale(i, (self.WIDTH, self.HEIGHT)) for i in importing_image_animations("art/back_ground\in_game_background/normal_in_game_background")]}
        self.in_game_ground_dict = {"normal": [pygame.transform.scale(i, (self.WIDTH, self.HEIGHT*1/4)) for i in importing_image_animations("art\general_art\ground/normal")]}

        # Projectiles
        self.wind_animation_dict = {"normal": [pygame.transform.scale(i, (40, 50)) for i in importing_image_animations("art\general_art\Projectile/tornado")]}

        # Props
        self.confetti = {"normal": [pygame.transform.scale(i, (200, 200)) for i in importing_image_animations("art\props\Confetti")]}

        # Players
        self.player_stand_size = (self.WIDTH*0.156, self.HEIGHT*0.5)
        self.player_run_size = (self.WIDTH*0.09, self.HEIGHT*0.26)
        self.player_crouch_size = (self.WIDTH*0.09, self.HEIGHT*0.1)
        self.player_celebrate_size = (self.WIDTH*0.15, self.HEIGHT*0.4)
        self.empty_player = {"standing": [pygame.transform.scale(i, self.player_stand_size) for i in [pygame.image.load("art\player_animations\empty.png")]],
                             "running": [pygame.transform.scale(i, self.player_run_size) for i in [pygame.image.load("art\player_animations\empty.png")]]}
        
        hans_player_animation_dict = {"standing": [pygame.transform.scale(i, self.player_stand_size) for i in importing_image_animations("art\player_animations\Hans\hans_stand")], 
                                        "running": [pygame.transform.scale(i, self.player_run_size) for i in importing_image_animations("art\player_animations\Hans\hans_run")],
                                        "crouching": [pygame.transform.scale(i, self.player_crouch_size) for i in importing_image_animations("art\general_art\place_holder/blue")],
                                        "celebrating": [pygame.transform.scale(i, self.player_celebrate_size) for i in importing_image_animations("art\general_art\place_holder/blue")],
                                        "stunned": [pygame.transform.scale(i, self.player_run_size) for i in importing_image_animations("art\general_art\place_holder/blue")],
                                        "jumping_ground": [pygame.transform.scale(i, self.player_run_size) for i in importing_image_animations("art\general_art\place_holder/red")],
                                        "jumping_sky": [pygame.transform.scale(i, self.player_run_size) for i in importing_image_animations("art\general_art\place_holder/blue")],
                                        "falling": [pygame.transform.scale(i, self.player_run_size) for i in importing_image_animations("art\general_art\place_holder/green")]}

        david_player_animation_dict = {"standing": [pygame.transform.scale(i, self.player_stand_size) for i in importing_image_animations("art\player_animations\David/david_stand")]}
        thomas_player_animation_dict = {"standing": []}
        jaran_player_animation_dict = {"standing": []}

        self.all_player_animation_dicts_list = [hans_player_animation_dict, david_player_animation_dict,\
                                                thomas_player_animation_dict, jaran_player_animation_dict]

        
        # Minions
        self.david_minion_size = (self.WIDTH*0.15, self.HEIGHT*0.1)
        self.thomas_minion_size = (self.WIDTH*0.15, self.HEIGHT*0.1)

        david_minion_animation_dict = {"crawling": [pygame.transform.scale(i, self.david_minion_size) for i in importing_image_animations("art\minion_animations\david_minion\david_crawl")]}
        thomas_minion_animation_dict = {"flying": [pygame.transform.scale(i, self.thomas_minion_size) for i in importing_image_animations("art\minion_animations/thomas_minion/thomas_fly")]}
        
        self.all_minion_animation_dicts_list = [david_minion_animation_dict, thomas_minion_animation_dict]


        # Bosses
        self.david_bos_size = (self.WIDTH*0.4, self.HEIGHT*0.2667)
        self.thomas_bos_size = (self.WIDTH*0.5, self.HEIGHT*0.3)
        self.thomas_bos_size_vertical = (self.WIDTH*0.2, self.HEIGHT*0.3)

        david_boss_animation_dict = {"crawling": [pygame.transform.scale(i, self.david_bos_size) for i in importing_image_animations("art/boss_animations\David_boss\david_boss_crawl")],
                                        "dying": [pygame.transform.scale(i, self.david_bos_size) for i in importing_image_animations("art\general_art\place_holder/green")]}
        thomas_boss_animation_dict = {"flying": [pygame.transform.scale(i, self.thomas_bos_size) for i in importing_image_animations("art/boss_animations\Thomas_boss/thomas_boss_fly")],
                                        "blowing_forward": [pygame.transform.scale(i, self.thomas_bos_size_vertical) for i in importing_image_animations("art\general_art\place_holder/red")],
                                        "blowing_upp": [pygame.transform.scale(i, self.thomas_bos_size_vertical) for i in importing_image_animations("art\general_art\place_holder/green")],
                                        "blowing_down": [pygame.transform.scale(i, self.thomas_bos_size_vertical) for i in importing_image_animations("art\general_art\place_holder/blue")],
                                        "blowing": [pygame.transform.scale(i, self.thomas_bos_size_vertical) for i in importing_image_animations("art\general_art\place_holder/blue")],
                                        "dying": [pygame.transform.scale(i, self.thomas_bos_size) for i in importing_image_animations("art\general_art\place_holder/green")],
                                        "charging": [pygame.transform.scale(i, self.thomas_bos_size) for i in importing_image_animations("art\general_art\place_holder/green")]}

        
        self.all_boss_amination_dicts_list = [david_boss_animation_dict, thomas_boss_animation_dict]
        

    
    