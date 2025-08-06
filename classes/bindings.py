import pygame
from classes.only_once import OnlyOnce

class PlayerBindings:
    def __init__(self):
        self.default_bindings_dict = {"jump": [pygame.K_UP, pygame.K_SPACE], "crouch": [pygame.K_DOWN, pygame.K_LSHIFT, pygame.K_RSHIFT]}
        self.bindings_dict = self.default_bindings_dict.copy()

    def change_binding(self):
        pass

class GlobalBindings:
    def __init__(self):
        self.global_default_bindings_dict = {"pause": [pygame.K_p, pygame.K_ESCAPE, pygame.K_HOME],
                                            "skip": [pygame.K_RETURN, pygame.K_END]}
        self.global_bindings_dict = self.global_default_bindings_dict.copy()

        # Things to only do once
        self.only_pause_once = OnlyOnce()
        self.only_skip_once = OnlyOnce()
        

    def change_global_bindings(self):
        pass

    
    def listen_for_key_strokes(self):
        self.keys = pygame.key.get_pressed()

        if self.only_pause_once.dew_it(any(self.keys[pause] for pause in self.global_bindings_dict["pause"])):
            if not self.pause and not self.stop:
                self.stop = True
                self.pause = True
            elif self.pause:
                self.stop = False
                self.pause = False
        if self.only_skip_once.dew_it(any(self.keys[skip] for skip in self.global_bindings_dict["skip"])):
            self.skip = True
        else:   self.skip = False

                