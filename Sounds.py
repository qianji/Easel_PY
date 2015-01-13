import os.path, sys
import pygame.mixer, pygame.time
time = pygame.time
mixer = pygame.mixer
mixer.init(11025)
main_dir = os.path.split(os.path.abspath(__file__))[0]

def playSounds(S):
    if S==None:
        return
    sounds = ["ding","boing","clap","click","bang"]
    #file_paths = [os.path.join(main_dir,'sounds',sou+".wav") for sound in sounds]
    for sou in S:
        if sou in sounds:
            file_path = os.path.join(main_dir,'sounds',sou+".wav")
            # load the sound
            sound = mixer.Sound(file_path)
            # play the sound
            channel = sound.play()

