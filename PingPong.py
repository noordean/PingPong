import pygame
import time
import random
import math

pygame.init()
clock = pygame.time.Clock()
pygame.mixer.music.load('misc127.wav')
done = False
screen_width=400
screen_height=400
white=(255,255,255)
black = (0,0,0)
deepblack=(100,100,100)
red = (255,0,0)
lightred= (150,0,0)
green=(0,220,0)
lightgreen = (0,150,0)
blue = (0,0,255)
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ping Pong')
background = pygame.image.load('ping-pong.jpg')
surface = pygame.image.load('ping.jpg')
pygame.display.set_icon(surface)

fonta = pygame.font.Font(None,40)
fontb = pygame.font.Font(None,25)
lbk = fontb.render('Back',True,white)
label = fonta.render('Controls:',True,white)
label1 = fontb.render('Button Arrow-Up: Move the bat up',True,white)
label2 = fontb.render('Button Arrow-Down: Move the bat down',True,white)
label3 = fontb.render('Button P : Pause the game',True,white)
def gameover():
    over = False
    while over==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gamov = fonta.render('GAME OVER',True,red)
        screen.blit(gamov,(120,180))
        pygame.draw.rect(screen,red,(150,220,100,25))
        startagain = fontb.render('start again',True,white)
        if mouse[0] in range(150,250) and mouse[1] in range(220,245):
            pygame.draw.rect(screen,lightred,(150,220,100,25))
        if mouse[0] in range(150,250) and mouse[1] in range(220,245) and click[0]==1:
            over = True
        screen.blit(startagain,(150+4,220+3))
        pygame.display.update()
        
def contact():
    labelc1 = fonta.render('Contact us:',True,white)
    labelc2 = fontb.render('Email: ebroyeem90@gmail.com',True,white)
    labelc3 = fontb.render('Phone-number: 07065834175',True,white)
    labelc4 = fontb.render('Back',True,white)
    cont = False
    while cont== False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse=pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.fill(green)
        screen.blit(labelc1,(120,20))
        screen.blit(labelc2,(20,120))
        screen.blit(labelc3,(20,160))
        pygame.draw.rect(screen,black,(175,255,50,25))
        if mouse[0] in range(175,175+50) and mouse[1] in range(255,255+25):
            pygame.draw.rect(screen,deepblack,(175,255,50,25))
        if mouse[0] in range(175,175+50) and mouse[1] in range(255,255+25) and click[0]==1:
            cont = True
        screen.blit(labelc4,(175+4,255+3))
        pygame.display.update()
def helppp():
    helpp = False
    back_x=175
    back_y=240
    while helpp == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse=pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.fill(green) 
        screen.blit(label,(110,20))
        screen.blit(label1,(20,100))
        screen.blit(label2,(20,140))
        screen.blit(label3,(20,180))
        pygame.draw.rect(screen,black,(back_x,back_y,50,25))
        if mouse[0] in range(back_x,back_x+50) and mouse[1] in range(back_y,back_y+25):
            pygame.draw.rect(screen,deepblack,(back_x,back_y,50,25))
        if mouse[0] in range(back_x,back_x+50) and mouse[1] in range(back_y,back_y+25) and click[0]==1:
            helpp = True
        screen.blit(lbk,(back_x+4,back_y+3))
        pygame.display.update()
        
def homepage():
    font = pygame.font.Font(None,25)
    label1 = font.render('Play',True,white)
    label2 = font.render('Help',True,white)
    label3 = font.render('Contact',True,white)
    
    play_x=100
    play_y=130
    help_x=205
    help_y=130
    contact_x=155
    contact_y=165
    begin = False
    while begin == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(background,(0,0))
        pygame.draw.rect(screen,green,(play_x,play_y,100,30))
        pygame.draw.rect(screen,green,(help_x,help_y,100,30))
        pygame.draw.rect(screen,green,(contact_x,contact_y,100,30))
        if mouse[0] in range(play_x,play_x+100) and mouse[1] in range(play_y,play_y+30):
            pygame.draw.rect(screen,lightgreen,(play_x,play_y,100,30))
        if mouse[0] in range(help_x,help_x+100) and mouse[1] in range(help_y,help_y+30):
            pygame.draw.rect(screen,lightgreen,(help_x,help_y,100,30))
        if mouse[0] in range(contact_x,contact_x+100) and mouse[1] in range(contact_y,contact_y+30):
            pygame.draw.rect(screen,lightgreen,(contact_x,contact_y,100,30))

        if mouse[0] in range(play_x,play_x+100) and mouse[1] in range(play_y,play_y+30) and click[0]==1:
            begin = True
        if mouse[0] in range(help_x,help_x+100) and mouse[1] in range(help_y,help_y+30) and click[0]==1:
            helppp()
        if mouse[0] in range(contact_x,contact_x+100) and mouse[1] in range(contact_y,contact_y+30) and click[0]==1:
            contact()
        screen.blit(label1,(play_x+32,play_y+5))
        screen.blit(label2,(help_x+32,help_y+5))
        screen.blit(label3,(contact_x+15,contact_y+5))

        pygame.display.update()
def pause():
    pause_rect_x=120
    pause_rect_y=190
    pause_rect_width=60
    pause_rect_height=20
    font = pygame.font.Font(None,20)
    label = font.render('Resume',True,white)
    label2 = font.render('Exit',True,white)
    pause=False
    while pause==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            #elif event.type==pygame.KEYDOWN:
             #   if event.key==pygame.K_p:
        mouse=pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        pygame.draw.rect(screen,blue,(100,150,200,100))            
        pygame.draw.rect(screen,red,(pause_rect_x,pause_rect_y,pause_rect_width,pause_rect_height))
        pygame.draw.rect(screen,red,(220,190,60,20))
        if mouse[0] in range(220,280) and mouse[1] in range(190,210):
            pygame.draw.rect(screen,lightred,(220,190,60,20))
        if mouse[0] in range(220,280) and mouse[1] in range(190,210) and click[0]==1:
            pygame.quit()
            quit()
        if mouse[0] in range(120,180) and mouse[1] in range(190,210):
            pygame.draw.rect(screen,lightred,(120,190,60,20))
        if mouse[0] in range(120,180) and mouse[1] in range(190,210) and click[0]==1:
            pause = True
        screen.blit(label,(pause_rect_x+3,pause_rect_y+3))
        screen.blit(label2,(236,193))

                
        pygame.display.update()
def player_score(p):
    font = pygame.font.Font(None,25)
    label= font.render('P: '+str(p),True,black)
    screen.blit(label,(0,0))
def computer_score(c):
    font = pygame.font.Font(None,25)
    label= font.render('C: '+str(c),True,red)
    screen.blit(label,(screen_width-45,0))
def bat(color,bat_x,bat_y,bat_width,bat_height):
    pygame.draw.rect(screen,color,(bat_x,bat_y,bat_width,bat_height))
def ball(ball_x,ball_y,ball_r):
    pygame.draw.circle(screen,white,(ball_x,ball_y),ball_r)
def game():
    bat_color = black
    bat_x = 0
    bat_y= int((screen_height/2))-30
    bat_width=4
    bat_height=50
    comp_bat_color = red
    comp_bat_x = screen_width-bat_width
    comp_bat_y = random.randint(bat_height,screen_height-2*bat_height)
    pygame.key.set_repeat(10,10)
    ball_x=comp_bat_x
    ball_y= comp_bat_y+int((bat_height/2))
    ball_r=6
    values=[1,-1]
    value = values[random.randint(0,1)]
    ball_x_incr = 1
    comp_bat_y_incr = 0
    p,c=0,0
    homepage()
    pygame.mixer.music.play()
   # x = random.randint(0,screen_width)
    #y = random.randint(0,screen_height)
    #z=math.sqrt(x**2+y**2)
    lev = 1
    n=200
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_UP:
                    if bat_y==0 or bat_y < 0:
                        bat_y-=0
                    else:
                        bat_y-=1
                if event.key == pygame.K_DOWN:
                    if bat_y==(screen_height-bat_height) or bat_y > (screen_height-bat_height):
                        bat_y+=0
                    else:
                        bat_y+=1
                    

        ball_x-= ball_x_incr
        ball_y-=value
        comp_bat_y-=comp_bat_y_incr
        if value==-1 and ball_y==(screen_height-ball_r) or ball_y > (screen_height-ball_r):
            value = 1
        if value==1 and ball_y== 0:
            value = -1
        if ball_x==bat_x+bat_width+3 and ball_y in range(bat_y,bat_y+bat_height):
            pygame.mixer.music.play()
            ball_x_incr = -1
            #ball_x = screen_width
        if ball_x==0:
            time.sleep(1)
            c+=1
            ball_x = comp_bat_x
            comp_bat_y = random.randint(0,screen_height-bat_height)
            ball_y = comp_bat_y+int((bat_height/2))
        if ball_x==screen_width:
            time.sleep(1)
            p+=1
            ball_x = comp_bat_x
            comp_bat_y = random.randint(0,screen_height-bat_height)
            ball_y = comp_bat_y+int((bat_height/2))
        if ball_x==comp_bat_x and ball_y in range(comp_bat_y,comp_bat_y+bat_height):
            ball_x_incr = 1
            pygame.mixer.music.play()
            
        if ball_x > int(screen_width/2) and ball_x_incr == -1 and value == 1: #ball_y < comp_bat_y:
                comp_bat_y_incr=1
                if ball_y < 50:
                    comp_bat_y_incr=0
        if ball_x > int(screen_width/2) and ball_x_incr == -1 and value == 1 and ball_y > (comp_bat_y+(bat_height/2)):
            comp_bat_y_incr=-1
        if ball_x > int(screen_width/2) and ball_x_incr == -1 and value==-1:#ball_y > comp_bat_y:
                comp_bat_y_incr = -1
                if ball_y > 250:
                    comp_bat_y_incr=0
        if ball_x > int(screen_width/2) and ball_x_incr == -1 and value==-1 and ball_y < (comp_bat_y+(bat_height/2)):
            comp_bat_y_incr = 1
        if ball_x == comp_bat_x :
            comp_bat_y_incr =0
            
        if p==6:
            c=0
            p=0
            lev+=1
            n+=50
        if c==6:
            pygame.mixer.music.pause()
            c=0
            p=0
            lev+=0
            n+=0
            gameover()

        clock.tick(n)
        screen.fill(green)
        player_score(p)
        computer_score(c)
        level = fontb.render('Level '+str(lev),True,white)
        screen.blit(level,(screen_height-220,0))
        bat(bat_color,bat_x,bat_y,bat_width,bat_height)
        bat(comp_bat_color,comp_bat_x,comp_bat_y,bat_width,bat_height)
        ball(ball_x,ball_y,ball_r)
        pygame.display.update()

game()
