import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()


#import pygame
#pygame.mixer.init()
#pygame.base.init()
#pygame.mixer.music.load('ex21.mp3')
#pygame.mixer.music.play()

#import playsound
#musica = input('Queres ouvir alguma musica?:')
#playsound.playsound('ex21.mp3')

#from pygame import mixer
#mixer.init()
#mixer.music.load('ex21.mp3')
#mixer.music.play()
#input('Agora você escuta?')