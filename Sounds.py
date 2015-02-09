import os.path, sys
import pygame.mixer, pygame.time
time = pygame.time
mixer = pygame.mixer
mixer.init(11025)
main_dir = os.path.split(os.path.abspath(__file__))[0]

# use a global sound library to store the sound
_sound_library={}
def playSounds(S):
    if S==None:
        return
    for sound in S:
        if not sound==None:
            channel = sound.play()

# check to see the sound is already loaded before loading
def loadSoundFile(name):
    global _sound_library
    sound = _sound_library.get(name)
    if sound ==None:
        try:
            file_path = os.path.join(main_dir,'sounds',name)
            sound = mixer.Sound(file_path)
            _sound_library[name] = sound
        except:
            print("Cannot load sound: ", file_path)
    return sound

def playSound(s):
    if s==None:
        return
    channel = s.play()
