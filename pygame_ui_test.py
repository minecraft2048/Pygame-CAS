import pygame
import time
import random

pygame.init()

display_width = 800 #Window size
display_height = 600

black = (0,0,0) #Color definition, maps color name to RGB tuple
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height)) #initialize screen
pygame.display.set_caption('A bit Racey') #Program name
clock = pygame.time.Clock()

def clamp(n, minn, maxn):
    '''Keep values in between values
        Arguments:
        n: Value
        minn: Minimum value
        maxn: Maximum value
    '''
    return max(min(maxn, n), minn)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

def button(msg,x,y,w,h,ic,ac,font='comicsansms',action=None):
    ''' Makes button in the screen and draw it
        Arguments:
        msg: Text for the button
        x: X coordinate in pixels
        y: Y coordinate in pixels
        w: Button width in pixels
        h: Button height in pixels
        ic: The button inital color
        ac: Button color on hover
        font: Text font
        action: Function name without ()
    '''
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont(font,20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def bar(x,y,w,h,color_init,color_border,color_bg=white,border_thickness=1,percent=100,msg=None):
    ''' Creates bar like loading bar
        Arguments:
        x : X coordinate
        y : Y coordinate
        w : Bar length
        h : Bar height
        color_init: The initial color of the bar
        color_border: The color of the border
        color_bg: Background color of the bar when it is empty
        border_thickness: Border thickness in pixels
        percent: How many percent does the bar fill inside the border
        msg: The text inside the bar
    '''
    w_inner = w * clamp((percent/100),0,1)
    pygame.draw.rect(gameDisplay,color_border,(x-border_thickness,y-border_thickness,w+(border_thickness*2),h+(border_thickness*2)))
    pygame.draw.rect(gameDisplay,color_bg,(x,y,w,h))
    pygame.draw.rect(gameDisplay,color_init,(x,y,w_inner,h))
    smallText = pygame.font.Font('freesansbold.ttf',15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    return

def value_bar(x,y,w,h,value,max_value,color_init,color_border,color_bg,border_thickness=1):
    ''' Creates status bar
        Arguments:
        x : X coordinate
        y : Y coordinate
        w : Bar length
        h : Bar height
        value: Current value
        max_value: Maximum value
        color_init: The initial color of the bar
        color_border: The color of the border
        color_bg: Background color of the bar when it is empty
        border_thickness: Border thickness in pixels
    '''
    msg = str(value) + '/' + str(max_value)
    percent = value/max_value*100
    bar(x, y, w, h, color_init, color_border, color_bg, border_thickness, percent, msg)

def main_loop():
    frame = 0
    crashed = False
    gameDisplay.fill(white)
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            #print(event)

        frame +=1
        secondframe = int(frame/20)
        #print(secondframe)
        pygame.draw.rect(gameDisplay,red,(150,450,100,20),1)
#        bar(150, 200, 100, 20, green,black,white,3, frame,'100/100')
        value_bar(150,200,100,20,frame,200,green,black,white,border_thickness=1)
        pygame.display.update()
        clock.tick(60)

main_loop()
pygame.quit()
quit()
