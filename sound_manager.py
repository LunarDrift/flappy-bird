import pygame
from constants import BG_MUSIC, FLAP_SOUND, DIE_SOUND, POINT_SOUND

class SoundManager:
    def __init__(self):
        # Load and set up sounds
        pygame.mixer.music.load(BG_MUSIC)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.07)
        pygame.mixer.set_num_channels(32)

        # Bird sounds
        self.flap_sound = pygame.mixer.Sound(FLAP_SOUND)
        self.flap_sound.set_volume(0.15)
        self.die_sound = pygame.mixer.Sound(DIE_SOUND)
        self.die_sound.set_volume(0.15)
        self.point_sound = pygame.mixer.Sound(POINT_SOUND)
        self.point_sound.set_volume(0.03)


    def play_flap(self):
        self.flap_sound.play()

    def play_die(self):
        self.die_sound.play()

    def play_point(self):
        self.point_sound.play()

    def rewind_music(self):
        pygame.mixer.music.rewind()        