import pygame
pygame.inti()
pygame.mixer.inti()


# this need to be as an attribute to the constructor.
    self.waitingSound = pygame.mixer.Sound ("waiting.wav")
    self.buttonClicked = pygame.mixer.Sound ("click.wav")


# in the searching/sorting section:

pygame.mixer.Sound.play (waitingSound)


# button click
pygame.mixer.Sound.play (buttonClicked)
