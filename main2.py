import pygame
import time
import math
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Easy Peasy Uni')


clock = pygame.time.Clock()


def text_objects(text, font):
   textSurface = font.render(text, True, black)
   return textSurface, textSurface.get_rect()

#test
start_img = pygame.image.load('level_button.png').convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        gameDisplay.blit(self.image, (self.rect.x, self.rect.y))


level_button = Button(350, 320, start_img, 0.1)

#introduction page
def game_intro():
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill("LightBlue")
        largeText = pygame.font.SysFont('TimesNewRoman',100)
        TextSurf, TextRect = text_objects("Easy Peasy Uni", largeText)
        TextRect.center = ((display_width/2),(display_height/2 - 60))
        gameDisplay.blit(TextSurf, TextRect)
        
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            time.sleep(1)
            game_loop()
        
        

        level_button.draw()

        
        clock.tick(60)
  
        pygame.display.update() 
        

    pygame.quit()
    quit()

#game page
def game_loop():
  
    screen = pygame.display.set_mode((800,360))
    
    bg = pygame.image.load('background.jpg').convert()
    bg_width = bg.get_width()
    scroll = 0
    tiles = math.ceil(display_width / bg_width) + 1
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        clock.tick(60)   
    
        #draw scrolling background image
        for i in range (0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
        pygame.display.update()

        #scroll background
        scroll -= 5

        #scroll reset
        if abs(scroll) > bg_width:
            scroll = 0


game_intro()