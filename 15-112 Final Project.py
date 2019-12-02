import pygame
import pygame.font
import time
import math
from pygame.locals import *
pygame.init()
class color():
    def __init__(self):
        self.win = pygame.display.set_mode((655, 383))
        pygame.display.set_caption("First Game")
        bg = pygame.image.load('mainscreen.jpg')
        self.win.blit(bg,(0,0))
        largeText = pygame.font.Font('Kardust TS Condensed Bold Italic.ttf',40)
        TextSurf, TextRect = self.text_objects("Choose Color and press OK twice", largeText)
        TextRect.center = ((655/2),(50))
        self.win.blit(TextSurf, TextRect)
        self.c = [0,0,0]



    def text_objects(self,text, font):
        black = [0,0,0]
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
    
    def colours(self,win):
        self.mouse = pygame.mouse.get_pos()
        if 36+66 > self.mouse[0] > 36 and 148+30 > self.mouse[1] > 148:
            pygame.draw.rect(self.win,[255,0,0],(36,148,66,30))
        else:
            pygame.draw.rect(self.win, [180,0,0],(36,148,66,30))

        if 138+66 > self.mouse[0] > 138 and 148+30 > self.mouse[1] > 148:
            pygame.draw.rect(self.win, [0,255,0],(138,148,66,30))
        else:
            pygame.draw.rect(self.win, [0,180,0],(138,148,66,30))

        if 240+66 > self.mouse[0] > 240 and 148+30 > self.mouse[1] > 148:
            pygame.draw.rect(self.win, [0,0,255],(240,148,66,30))
        else:
            pygame.draw.rect(self.win, [0,0,180],(240,148,66,30))

        if 342+66 > self.mouse[0] > 342 and 148+30 > self.mouse[1] > 148:
            pygame.draw.rect(self.win, [255,255,255],(342,148,66,30))
        else:
            pygame.draw.rect(self.win, [200,200,200],(342,148,66,30))

        if 444+66 > self.mouse[0] > 444 and 148+30 > self.mouse[1] > 148:
            pygame.draw.rect(self.win, [255,255,255],(444,148,66,30))
        else:
            pygame.draw.rect(self.win, [200,200,200],(444,148,66,30))
        
        

        button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("RED", button1)
        textRect.center = ( (36+(66/2)), (148+(30/2)) )
        self.win.blit(textSurf, textRect)

        button2 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("GREEN", button2)
        textRect.center = ( (138+(66/2)), (148+(30/2)) )
        self.win.blit(textSurf, textRect)

        button3 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("BLUE", button3)
        textRect.center = ( (240+(66/2)), (148+(30/2)) )
        self.win.blit(textSurf, textRect)

        button4 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("WHITE", button3)
        textRect.center = ( (342+(66/2)), (148+(30/2)) )
        self.win.blit(textSurf, textRect)

        button4 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("OK", button3)
        textRect.center = ( (444+(66/2)), (148+(30/2)) )
        self.win.blit(textSurf, textRect)

        msg = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Press q to go back", msg)
        textRect.center = ( (70+(134/2)), (340+(40/2)) )
        self.win.blit(textSurf, textRect)

    def game_intro(self):
        intro = True
        clock = pygame.time.Clock()

        while intro:
            clock.tick(100)
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.colours(self.win)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    sp = SinglePlayer()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    if 36+66 > self.mouse[0] > 36 and 148+30 > self.mouse[1] > 148:
                        self.c  = [255,0,0]
                    if 138+66 > self.mouse[0] > 138 and 148+30 > self.mouse[1] > 148:
                        self.c = [0,255,0]
                    if 240+66 > self.mouse[0] > 240 and 148+30 > self.mouse[1] > 148:
                        self.c = [0,0,255]

                    if 342+66 > self.mouse[0] > 342 and 148+30 > self.mouse[1] > 148:
                        self.c = [255,255,255]
                    if (444+66 > self.mouse[0] > 444 and 148+30 > self.mouse[1] > 148) and self.c != [0,0,0]:
                        return self.c
                    
                    
                    
            pygame.display.update()
        
        
        

class course1():
    def __init__(self,color):
        win = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("First Game")
        bg = pygame.image.load('Course2.png')
        win.blit(bg,(0,0))
        self.color = color
        self.ball = ball(118,453,5,(self.color),win)
        self.count = 0
        self.game_loop(win,self.ball)
        
    def hole(self,surf):
        self.Hole = pygame.draw.circle(surf, (0,0,0), (443,99), 12)
        self.holex = 443
        self.holey = 99
        self.holerad = 12
        
    def text_objects(self,text, font):
        black = [0,0,0]
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
        
    def game_loop(self,surf,ball):
        self.bg = pygame.image.load('Course2.png')
        self.surf = surf
        run = True
        shoot = False
        stop = False
        top = False
        time = 0
        power = 0
        angle = 0
        clock = pygame.time.Clock()
        line = [(),()]
        i = 1
        while run:
            clock.tick(100)
            if  shoot:
                power -= 0.05
                # IF BALL SLOWS DOWN AND STOPS
                if int(power) == initialpower//2:
                    stop = True
                    self.ball.x = self.ball.x
                    self.ball.y = self.ball.y
                    power = 0
                    
                    self.game_loop(surf,ball)
                    self.count+=1
                # IF BALL GOES IN THE HOLE
                dist = math.sqrt((self.holex - self.ball.x)**2 +(self.holey - self.ball.y)**2)
                if dist <= self.ball.radius + self.holerad:
                    shoot = False
                    stop = False
                    print(self.count)
                    num = 'No of shots: ' + str(self.count)
                    pygame.draw.rect(self.surf,[255,255,255],(150,250,200,50))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                    textSurf, textRect = self.text_objects(num, button1)
                    textRect.center = ( (150+(200/2)), (250+(30/2)) )
                    self.surf.blit(textSurf, textRect)


                    pygame.draw.rect(self.surf,[255,255,255],(150,300,200,50))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                    textSurf, textRect = self.text_objects('Press r to Restart', button1)
                    textRect.center = ( (150+(200/2)), (300+(30/2)) )
                    self.surf.blit(textSurf, textRect)

                    pygame.draw.rect(self.surf,[255,255,255],(150,350,200,30))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                    textSurf, textRect = self.text_objects('Press q to quit', button1)
                    textRect.center = ( (150+(200/2)), (350+(30/2)) )
                    self.surf.blit(textSurf, textRect)

                    
                    #for event in pygame.event.get():
                    while event.type != pygame.QUIT:
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_r]:
                                c1 = course1(self.color)
                            if keys[pygame.K_q]:
                                sg = SinglePlayer()
                # IF THE BALL COLLIDES AGAINST THE WALLS
                if stop == False:
                    time += 0.05
                    po = self.ball.ballPath(self.ball,x, y, power, angle, time,i)
                    self.ball.x = po[0] 
                    self.ball.y = po[1]
                    if self.ball.y < 210 and (self.ball.x >=236 and self.ball.x < 499):
                        top = True
                    else:
                        top = False
    
                    #IF BALL COLLIDES WITH THE LEFT WALL
                    if self.ball.x<0+self.ball.radius:
                        self.ball.x = -self.ball.x 
                    #IF BALL COLLIDES WITH THE TOP WALL       
                    if self.ball.y<0+self.ball.radius:
                        self.ball.y = -self.ball.y
                    #IF BALL COLLIDES WITH THE TOP RIGHT WALL
                    if self.ball.x > 499 - self.ball.radius and top == True:
                         self.ball.x = 2*(499 - self.ball.radius) - self.ball.x
                    #IF BALL COLLIDES WITH THE BOTTOM BOTTOM WALL
                    if self.ball.y>499 - self.ball.radius:
                        self.ball.y = 2*(499 - self.ball.radius) - self.ball.y
                    #IF BALL COLLIDES WITH THE BOTTOM RIGHT WALL
                    if self.ball.y > 210 and top == False:
                        if (self.ball.x >= 236 - self.ball.radius):
                            self.ball.x = 2*(236 - self.ball.radius) - self.ball.x
                    #IF BALL COLLIDES WITH THE TOP BOTTOM WALL
                    if (self.ball.x >= 236 - self.ball.radius and self.ball.x < 499):
                        if self.ball.y >= 210 - self.ball.radius:
                            self.ball.y = 2*(210 - self.ball.radius) - self.ball.y
                        #self.ball.y = -self.ball.y




            line = [(self.ball.x, self.ball.y), pygame.mouse.get_pos()]
            self.ball.redrawWindow(self.surf,self.ball,line)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                        
                    if not shoot:
                        x = self.ball.x
                        y = self.ball.y
                        pos =pygame.mouse.get_pos()
                        #print(pos)
                        shoot = True
                        power = math.sqrt((line[1][1]-line[0][1])**2 +(line[1][0]-line[0][1])**2)/8
                        initialpower = power
                        angle = self.ball.findAngle(pos,self.ball)
                        self.count += 1
                            
                    
            
            self.surf.blit(self.bg,(0,0))
            self.hole(self.surf)
            pygame.display.update()


class course2():
    def __init__(self,color):
        win = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("First Game")
        bg = pygame.image.load('Course3.png')
        win.blit(bg,(0,0))
        self.color = color
        self.ball = ball(68,465,5,(self.color),win)
        self.count = 0
        self.game_loop(win,self.ball)
        
    def hole(self,surf):
        self.Hole = pygame.draw.circle(surf, (0,0,0), (424,460), 12)
        self.holex = 424
        self.holey = 460
        self.holerad = 12
        
    def text_objects(self,text, font):
        black = [0,0,0]
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
    
    def game_loop(self,surf,ball):
        self.bg = pygame.image.load('Course3.png')
        self.surf = surf
        run = True
        shoot = False
        stop = False
        top = False
        bottom1 = False
        bottom2 = False
        time = 0
        power = 0
        angle = 0
        clock = pygame.time.Clock()
        line = [(),()]
        i = 1
        while run:
            clock.tick(100)
            if  shoot:
                power -= 0.05
                # IF BALL SLOWS DOWN AND STOPS
                if int(power) == initialpower//2:
                    stop = True
                    self.ball.x = self.ball.x
                    self.ball.y = self.ball.y
                    power = 0
                    
                    
                    self.game_loop(surf,ball)
                    self.count+=1
                # IF BALL GOES IN THE HOLE
                dist = math.sqrt((self.holex - self.ball.x)**2 +(self.holey - self.ball.y)**2)
                if dist <= self.ball.radius + self.holerad:
                    shoot = False
                    stop = False
                    print(self.count)
                    num = 'No of shots: ' + str(self.count)
                    pygame.draw.rect(self.surf,[255,255,255],(150,250,200,50))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                    textSurf, textRect = self.text_objects(num, button1)
                    textRect.center = ( (150+(200/2)), (250+(30/2)) )
                    self.surf.blit(textSurf, textRect)


                    pygame.draw.rect(self.surf,[255,255,255],(150,300,200,50))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                    textSurf, textRect = self.text_objects('Press r to Restart', button1)
                    textRect.center = ( (150+(200/2)), (300+(30/2)) )
                    self.surf.blit(textSurf, textRect)

                    pygame.draw.rect(self.surf,[255,255,255],(150,350,200,30))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                    textSurf, textRect = self.text_objects('Press q to quit', button1)
                    textRect.center = ( (150+(200/2)), (350+(30/2)) )
                    self.surf.blit(textSurf, textRect)
                    
                    #for event in pygame.event.get():
                    while event.type != pygame.QUIT:
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_r]:
                                c2 = course2(self.color)
                            if keys[pygame.K_q]:
                                sg = SinglePlayer()
                
                # IF THE BALL COLLIDES AGAINST THE WALLS
                if stop == False:
                    time += 0.05
                    po = self.ball.ballPath(self.ball,x, y, power, angle, time,i)
                    self.ball.x = po[0] 
                    self.ball.y = po[1]


                    if (self.ball.y>= 151 + self.ball.radius and self.ball.y <= 499 - self.ball.radius) and (self.ball.x >= 0 + self.ball.radius):
                        bottom1 = True
                    if (self.ball.y>= 0 + self.ball.radius and self.ball.y < 151) and (self.ball.x >= 0 + self.ball.radius and self.ball.x <= 499 - self.ball.radius):
                        top = True
                    if (self.ball.y>= 151 + self.ball.radius and self.ball.y <= 499 - self.ball.radius) and (self.ball.x <= 499 - self.ball.radius):
                        bottom2 = True
                        
                    #IF BALL COLLIDES WITH THE BOTTOM BOTTOM
                    if (self.ball.x >= 0 + self.ball.radius and self.ball.x <= 146 - self.ball.radius) and self.ball.y >= 151:
                        if self.ball.y > 499 - self.ball.radius:
                            self.ball.y = 2*(499 - self.ball.radius) - self.ball.y
                            
                    #IF BALL COLLIDES WITH LEFT WALL
                    if self.ball.x < 0 + self.ball.radius:
                        #self.ball.x = 2*(0 - self.ball.radius) - self.ball.x
                        self.ball.x = -self.ball.x
                    #IF BALL COLLIDES WITH TOP WALL
                    if self.ball.y < 0 + self.ball.radius:
                        self.ball.y = -self.ball.y
                        

                    #IF BALL COLLIDES WITH THE SECOND RIGHT WALL
                    if self.ball.x >= 499 - self.ball.radius:
                        self.ball.x = 2*(499 - self.ball.radius) - self.ball.x
                        
                        
                    if self.ball.y > 499 - self.ball.radius:
                        self.ball.y = 2*(499 - self.ball.radius) - self.ball.y
                        
                        
                    #IF BALL COLLIDES WITH THE FIRST RIGHT BOTTOM WALL
                    if (self.ball.y >= 151 + self.ball.radius and self.ball.y < 499 - self.ball.radius) and self.ball.x >= 0 and bottom2 == False:
                        if self.ball.x > 146 - self.ball.radius:
                            self.ball.x = 2*(146 - self.ball.radius) - self.ball.x
                            
                            
                    if self.ball.y < 0 + self.ball.radius :
                        self.ball.y = -self.ball.y
                    #IF BALL COLLIDES WITH THE TOP BOTTOM WALL
                    if (self.ball.x>= 146 + self.ball.radius and self.ball.x <=358 - self.ball.radius) and self.ball.y>0:
                        if self.ball.y >= 151 - self.ball.radius:
                            self.ball.y = 2*(151 - self.ball.radius) - self.ball.y
                            
                            
                    if self.ball.y < 0 + self.ball.radius :
                       self.ball.y = -self.ball.y

##                    if (self.ball.x>= 146 + self.ball.radius and self.ball.x <=358 - self.ball.radius) and self.ball.y>0:
##                        if self.ball.y >= 151 - self.ball.radius:
##                            self.ball.y = -self.ball.y
##                            self.ball.y = 2*(151 - self.ball.radius) - self.ball.y
                            
                    #IF BALL COLLIDES WITH THE SECOND RIGHT WALL
                    if self.ball.x >= 499 - self.ball.radius:
                        self.ball.x = 2*(499 - self.ball.radius) - self.ball.x
                        
                        
                    #IF BALL COLLIDES WITH THE SECOND BOTTOM BOTTOM WALL
                    if (self.ball.x >= 358 + self.ball.radius and self.ball.x <= 499 - self.ball.radius) and y > 151 + self.ball.radius and bottom2 == True:
                        if self.ball.y > 499 - self.ball.radius:
                            self.ball.y = 2*(499 - self.ball.radius) - self.ball.y
                            
                    #IF BALL COLLIDES WITH THE SECOND BOTTOM LEFT WALL
                    if (self.ball.y >= 151 and self.ball.y <= 499) and bottom2 == True:
                        if self.ball.x == 358 + self.ball.radius:
                            #self.ball.x = 2*(358 - self.ball.radius) - self.ball.x
                            self.ball.x = 358 - self.ball.x
                            



            line = [(self.ball.x, self.ball.y), pygame.mouse.get_pos()]
            self.ball.redrawWindow(self.surf,self.ball,line)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    c2 = course2(self.color)
                
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                        
                    if not shoot:
                        x = self.ball.x
                        y = self.ball.y
                        pos =pygame.mouse.get_pos()
                        #print(pos)
                        shoot = True
                        power = math.sqrt((line[1][1]-line[0][1])**2 +(line[1][0]-line[0][1])**2)/8
                        initialpower = power
                        angle = self.ball.findAngle(pos,self.ball)
                        self.count += 1
                            
                    
            
            self.surf.blit(self.bg,(0,0))
            self.hole(self.surf)
            pygame.display.update()



class course1_tt():
    def __init__(self,color):
        win = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("First Game")
        bg = pygame.image.load('Course2.png')
        win.blit(bg,(0,0))
        self.color = color
        self.ball = ball(118,453,5,(self.color),win)
        self.count = 0
        self.ellapsed = 0
        self.game_loop(win,self.ball,self.ellapsed)
        
    def hole(self,surf):
        self.Hole = pygame.draw.circle(surf, (0,0,0), (443,99), 12)
        self.holex = 443
        self.holey = 99
        self.holerad = 12
        
    def text_objects(self,text, font):
        black = [0,0,0]
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
        
    def game_loop(self,surf,ball,ellapsed):
        self.bg = pygame.image.load('Course2.png')
        self.surf = surf
        run = True
        shoot = False
        stop = False
        top = False
        time = 0
        power = 0
        angle = 0
        self.ellapsed = ellapsed
        clock = pygame.time.Clock()
        line = [(),()]
        i = 1
        start_ticks=pygame.time.get_ticks()
        while run:
            clock.tick(1000)
            seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
            num = 'Time: ' + str(int(seconds)+ int(self.ellapsed))
            button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
            textSurf, textRect = self.text_objects(num, button1)
            textRect.center = ( (250+(200/2)), (400+(30/2)) )
            self.surf.blit(textSurf, textRect)
            seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
            if stop == True or seconds + self.ellapsed > 20: # if more than 10 seconds close the game
                #run = False
                shoot = False
                stop == True
                num = 'Time is over. Your Time: ' + str(int(seconds)) + ' seconds'
                pygame.draw.rect(self.surf,[255,255,255],(150,250,200,50))
                button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",12)
                textSurf, textRect = self.text_objects(num, button1)
                textRect.center = ( (150+(200/2)), (250+(30/2)) )
                self.surf.blit(textSurf, textRect)


                pygame.draw.rect(self.surf,[255,255,255],(150,300,200,50))
                button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                textSurf, textRect = self.text_objects('Press r to Restart', button1)
                textRect.center = ( (150+(200/2)), (300+(30/2)) )
                self.surf.blit(textSurf, textRect)

                pygame.draw.rect(self.surf,[255,255,255],(150,350,200,30))
                button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                textSurf, textRect = self.text_objects('Press q to quit', button1)
                textRect.center = ( (150+(200/2)), (350+(30/2)) )
                self.surf.blit(textSurf, textRect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_r]:
                        c1 = course1_tt(self.color)
                    if keys[pygame.K_q]:
                        tt = TimeTrails()
                #pygame.display.update()
                
                break
            
            
            
            if  shoot:
                power -= 0.05
                # IF BALL SLOWS DOWN AND STOPS
                if int(power) == initialpower//2:
                    stop = True
                    self.ball.x = self.ball.x
                    self.ball.y = self.ball.y
                    power = 0
                    self.ellapsed = self.ellapsed + seconds
                    self.game_loop(surf,ball,self.ellapsed)
                    self.count+=1
                # IF BALL GOES IN THE HOLE
                dist = math.sqrt((self.holex - self.ball.x)**2 +(self.holey - self.ball.y)**2)
                if dist <= self.ball.radius + self.holerad:
                    shoot = False
                    stop = False
                    self.ellapsed = self.ellapsed + seconds
                    num = 'Time Ellapsed: ' + str(int(self.ellapsed)) + ' seconds.'
                    pygame.draw.rect(self.surf,[255,255,255],(150,250,200,50))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",15)
                    textSurf, textRect = self.text_objects(num, button1)
                    textRect.center = ( (150+(200/2)), (250+(30/2)) )
                    self.surf.blit(textSurf, textRect)


                    pygame.draw.rect(self.surf,[255,255,255],(150,300,200,50))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                    textSurf, textRect = self.text_objects('Press r to Restart', button1)
                    textRect.center = ( (150+(200/2)), (300+(30/2)) )
                    self.surf.blit(textSurf, textRect)

                    pygame.draw.rect(self.surf,[255,255,255],(150,350,200,30))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                    textSurf, textRect = self.text_objects('Press q to quit', button1)
                    textRect.center = ( (150+(200/2)), (350+(30/2)) )
                    self.surf.blit(textSurf, textRect)

                    
                    #for event in pygame.event.get():
                    while event.type != pygame.QUIT:
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_r]:
                                c1 = course1_tt(self.color)
                            if keys[pygame.K_q]:
                                tt = TimeTrails()
                # IF THE BALL COLLIDES AGAINST THE WALLS
                if stop == False:
                    time += 0.05
                    po = self.ball.ballPath(self.ball,x, y, power, angle, time,i)
                    self.ball.x = po[0] 
                    self.ball.y = po[1]
                    if self.ball.y < 210 and (self.ball.x >=236 and self.ball.x < 499):
                        top = True
                    else:
                        top = False
    
                    #IF BALL COLLIDES WITH THE LEFT WALL
                    if self.ball.x<0+self.ball.radius:
                        self.ball.x = -self.ball.x 
                    #IF BALL COLLIDES WITH THE TOP WALL       
                    if self.ball.y<0+self.ball.radius:
                        self.ball.y = -self.ball.y
                    #IF BALL COLLIDES WITH THE TOP RIGHT WALL
                    if self.ball.x > 499 - self.ball.radius and top == True:
                         self.ball.x = 2*(499 - self.ball.radius) - self.ball.x
                    #IF BALL COLLIDES WITH THE BOTTOM BOTTOM WALL
                    if self.ball.y>499 - self.ball.radius:
                        self.ball.y = 2*(499 - self.ball.radius) - self.ball.y
                    #IF BALL COLLIDES WITH THE BOTTOM RIGHT WALL
                    if self.ball.y > 210 and top == False:
                        if (self.ball.x >= 236 - self.ball.radius):
                            self.ball.x = 2*(236 - self.ball.radius) - self.ball.x
                    #IF BALL COLLIDES WITH THE TOP BOTTOM WALL
                    if (self.ball.x >= 236 - self.ball.radius and self.ball.x < 499):
                        if self.ball.y >= 210 - self.ball.radius:
                            self.ball.y = 2*(210 - self.ball.radius) - self.ball.y
                        #self.ball.y = -self.ball.y




            line = [(self.ball.x, self.ball.y), pygame.mouse.get_pos()]
            self.ball.redrawWindow(self.surf,self.ball,line)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                        
                    if not shoot:
                        x = self.ball.x
                        y = self.ball.y
                        pos =pygame.mouse.get_pos()
                        #print(pos)
                        shoot = True
                        power = math.sqrt((line[1][1]-line[0][1])**2 +(line[1][0]-line[0][1])**2)/8
                        initialpower = power
                        angle = self.ball.findAngle(pos,self.ball)
                        self.count += 1
                            
                    
            
            self.surf.blit(self.bg,(0,0))
            self.hole(self.surf)
            pygame.display.update()


class course2_tt():
    def __init__(self,color):
        win = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("First Game")
        self.bg = pygame.image.load('Course3.png')
        win.blit(self.bg,(0,0))
        self.color = color
        self.ball = ball(68,465,5,(self.color),win)
        self.count = 0
        self.ellapsed = 0
        self.game_loop(win,self.ball,self.ellapsed)
        
    def hole(self,surf):
        self.Hole = pygame.draw.circle(surf, (0,0,0), (424,460), 12)
        self.holex = 424
        self.holey = 460
        self.holerad = 12
        
    def text_objects(self,text, font):
        black = [0,0,0]
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
    
    def game_loop(self,surf,ball,ellapsed):
        self.bg = pygame.image.load('Course3.png')
        self.surf = surf
        run = True
        shoot = False
        stop = False
        top = False
        bottom1 = False
        bottom2 = False
        time = 0
        power = 0
        angle = 0
        self.ellapsed = ellapsed
        clock = pygame.time.Clock()
        line = [(),()]
        i = 1
        start_ticks=pygame.time.get_ticks()
        while run:
            clock.tick(1000)
            seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
            num = 'Time: ' + str(int(seconds)+ int(self.ellapsed))
            button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
            textSurf, textRect = self.text_objects(num, button1)
            textRect.center = ( (150+(200/2)), (250+(30/2)) )
            self.surf.blit(textSurf, textRect)
            if stop == True or seconds + self.ellapsed > 20: # if more than 10 seconds close the game
                #run = False
                shoot = False
                num = 'Time is over. Your Time: ' + str(int(seconds))
                pygame.draw.rect(self.surf,[255,255,255],(150,250,200,50))
                button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",15)
                textSurf, textRect = self.text_objects(num, button1)
                textRect.center = ( (150+(200/2)), (250+(30/2)) )
                self.surf.blit(textSurf, textRect)


                pygame.draw.rect(self.surf,[255,255,255],(150,300,200,50))
                button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                textSurf, textRect = self.text_objects('Press r to Restart', button1)
                textRect.center = ( (150+(200/2)), (300+(30/2)) )
                self.surf.blit(textSurf, textRect)

                pygame.draw.rect(self.surf,[255,255,255],(150,350,200,30))
                button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                textSurf, textRect = self.text_objects('Press q to quit', button1)
                textRect.center = ( (150+(200/2)), (350+(30/2)) )
                self.surf.blit(textSurf, textRect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_r]:
                        c2 = course2_tt(self.color)
                    if keys[pygame.K_q]:
                        tt = TimeTrails()
                
                
                break
            
            if  shoot:
                power -= 0.05
                # IF BALL SLOWS DOWN AND STOPS
                if int(power) == initialpower//2:
                    stop = True
                    self.ball.x = self.ball.x
                    self.ball.y = self.ball.y
                    power = 0
                    self.ellapsed = self.ellapsed + seconds
                    self.game_loop(surf,ball,self.ellapsed)
                    self.count+=1
                # IF BALL GOES IN THE HOLE
                dist = math.sqrt((self.holex - self.ball.x)**2 +(self.holey - self.ball.y)**2)
                if dist <= self.ball.radius + self.holerad:
                    shoot = True
                    stop = False
                    self.ellapsed = self.ellapsed + seconds
                    num = 'Time Ellapsed: ' + str(int(self.ellapsed)) + ' seconds'
                    pygame.draw.rect(self.surf,[255,255,255],(150,250,200,50))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",15)
                    textSurf, textRect = self.text_objects(num, button1)
                    textRect.center = ( (150+(200/2)), (250+(30/2)) )
                    self.surf.blit(textSurf, textRect)


                    pygame.draw.rect(self.surf,[255,255,255],(150,300,200,50))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                    textSurf, textRect = self.text_objects('Press r to Restart', button1)
                    textRect.center = ( (150+(200/2)), (300+(30/2)) )
                    self.surf.blit(textSurf, textRect)

                    pygame.draw.rect(self.surf,[255,255,255],(150,350,200,30))
                    button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
                    textSurf, textRect = self.text_objects('Press q to quit', button1)
                    textRect.center = ( (150+(200/2)), (350+(30/2)) )
                    self.surf.blit(textSurf, textRect)
                    
                    #for event in pygame.event.get():
                    while event.type != pygame.QUIT:
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_r]:
                                c2 = course2_tt(self.color)
                            if keys[pygame.K_q]:
                                tt = TimeTrails()
                
                # IF THE BALL COLLIDES AGAINST THE WALLS
                if stop == False:
                    time += 0.05
                    po = self.ball.ballPath(self.ball,x, y, power, angle, time,i)
                    self.ball.x = po[0] 
                    self.ball.y = po[1]


                    if (self.ball.y>= 151 + self.ball.radius and self.ball.y <= 499 - self.ball.radius) and (self.ball.x >= 0 + self.ball.radius):
                        bottom1 = True
                    if (self.ball.y>= 0 + self.ball.radius and self.ball.y < 151) and (self.ball.x >= 0 + self.ball.radius and self.ball.x <= 499 - self.ball.radius):
                        top = True
                    if (self.ball.y>= 151 + self.ball.radius and self.ball.y <= 499 - self.ball.radius) and (self.ball.x <= 499 - self.ball.radius):
                        bottom2 = True
                        
                    #IF BALL COLLIDES WITH THE BOTTOM BOTTOM
                    if (self.ball.x >= 0 + self.ball.radius and self.ball.x <= 146 - self.ball.radius) and self.ball.y >= 151:
                        if self.ball.y > 499 - self.ball.radius:
                            self.ball.y = 2*(499 - self.ball.radius) - self.ball.y
                            
                            
                    #IF BALL COLLIDES WITH LEFT WALL
                    if self.ball.x < 0 + self.ball.radius:
                        #self.ball.x = 2*(0 - self.ball.radius) - self.ball.x
                        self.ball.x = -self.ball.x
                    #IF BALL COLLIDES WITH TOP WALL
                    if self.ball.y < 0 + self.ball.radius:
                        
                        self.ball.y = -self.ball.y
                        
                        #self.ball.y = 2*(self.ball.radius + self.ball.radius) + self.ball.y
                        #print(self.ball.y)

                    #IF BALL COLLIDES WITH THE SECOND RIGHT WALL
                    if self.ball.x >= 499 - self.ball.radius:
                        self.ball.x = 2*(499 - self.ball.radius) - self.ball.x
                        
                        
                    if self.ball.y > 499 - self.ball.radius:
                        self.ball.y = 2*(499 - self.ball.radius) - self.ball.y
                        
                        
                    #IF BALL COLLIDES WITH THE FIRST RIGHT BOTTOM WALL
                    if (self.ball.y >= 151 + self.ball.radius and self.ball.y < 499 - self.ball.radius) and self.ball.x >= 0 and bottom2 == False:
                        if self.ball.x > 146 - self.ball.radius:
                            self.ball.x = 2*(146 - self.ball.radius) - self.ball.x
                            
                            
                    if self.ball.y < 0 + self.ball.radius :
                        self.ball.y = -self.ball.y
                    #IF BALL COLLIDES WITH THE TOP BOTTOM WALL
                    if (self.ball.x>= 146 + self.ball.radius and self.ball.x <=358 - self.ball.radius) and self.ball.y>0:
                        if self.ball.y >= 151 - self.ball.radius:
                            self.ball.y = 2*(151 - self.ball.radius) - self.ball.y
                            
                            
                    if self.ball.y < 0 + self.ball.radius :
                       self.ball.y = -self.ball.y

##                    if (self.ball.x>= 146 + self.ball.radius and self.ball.x <=358 - self.ball.radius) and self.ball.y>0:
##                        if self.ball.y >= 151 - self.ball.radius:
##                            self.ball.y = -self.ball.y
##                            self.ball.y = 2*(151 - self.ball.radius) - self.ball.y
                            
                    #IF BALL COLLIDES WITH THE SECOND RIGHT WALL
                    if self.ball.x >= 499 - self.ball.radius:
                        self.ball.x = 2*(499 - self.ball.radius) - self.ball.x
                        
                        
                    #IF BALL COLLIDES WITH THE SECOND BOTTOM BOTTOM WALL
                    if (self.ball.x >= 358 + self.ball.radius and self.ball.x <= 499 - self.ball.radius) and y > 151 + self.ball.radius and bottom2 == True:
                        if self.ball.y > 499 - self.ball.radius:
                            self.ball.y = 2*(499 - self.ball.radius) - self.ball.y
                            
                    #IF BALL COLLIDES WITH THE SECOND BOTTOM LEFT WALL
                    if (self.ball.y >= 151 and self.ball.y <= 499) and bottom2 == True:
                        if self.ball.x == 358 + self.ball.radius:
                            #self.ball.x = 2*(358 - self.ball.radius) - self.ball.x
                            self.ball.x = 358 - self.ball.x



            line = [(self.ball.x, self.ball.y), pygame.mouse.get_pos()]
            self.ball.redrawWindow(self.surf,self.ball,line)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    c2 = course2_tt(self.color)
                #pygame.display.update()
                
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                        
                    if not shoot:
                        x = self.ball.x
                        y = self.ball.y
                        pos =pygame.mouse.get_pos()
                        #print(pos)
                        shoot = True
                        power = math.sqrt((line[1][1]-line[0][1])**2 +(line[1][0]-line[0][1])**2)/8
                        initialpower = power
                        angle = self.ball.findAngle(pos,self.ball)
                        self.count += 1
                            
                    
            
            self.surf.blit(self.bg,(0,0))
            self.hole(self.surf)
            pygame.display.update()







        
class ball(object):
    def __init__(self,x,y,radius,color,surf):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.surf = surf
        #self.game_intro(self.surf)
        

    def draw(self,surf,color):
        pygame.draw.circle(self.surf, (color), (int(self.x),int(self.y)), self.radius)


    @staticmethod
    def ballPath(self,startx, starty, power, ang, time,i):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power
        if power > 0:
            distX = (velx) * time
            distY = (vely) * time
            newx = round(distX + startx)
            newy = round(starty - distY)
        else:
            newx = self.x
            newy = self.y
            


        return (newx, newy)


    def redrawWindow(self,surf,obj,line):
        obj.draw(self.surf,self.color)
        pygame.draw.line(self.surf, (255,255,255),line[0], line[1])
        pygame.display.update()

    def findAngle(self,pos,obj):
        sX = obj.x
        sY = obj.y
        try:
            angle = math.atan((sY - pos[1]) / (sX - pos[0]))
        except:
            angle = math.pi / 2

        if pos[1] < sY and pos[0] > sX:
            angle = abs(angle)
        elif pos[1] < sY and pos[0] < sX:
            angle = math.pi - angle
        elif pos[1] > sY and pos[0] < sX:
            angle = math.pi + abs(angle)
        elif pos[1] > sY and pos[0] > sX:
            angle = (math.pi * 2) - angle

        return angle


class mainScreen():
    
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((655, 383))
        self.bg = pygame.image.load('mainscreen.jpg')
        self.win.blit(self.bg,(0,0))
        pygame.display.set_caption("First Game")
        largeText = pygame.font.Font('Kardust TS Condensed Bold Italic.ttf',72)
        TextSurf, TextRect = self.text_objects("Mini Golf", largeText)
        TextRect.center = ((655/2),(70))
        self.win.blit(TextSurf, TextRect)
        
        
        
    def text_objects(self,text, font):
        black = [0,0,0]
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def buttons(self):
        self.mouse = pygame.mouse.get_pos()
        if 485+150 > self.mouse[0] > 485 and 200+30 > self.mouse[1] > 200:
            pygame.draw.rect(self.win,[200,200,200],(485,200,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,200,150,30))

        if 485+150 > self.mouse[0] > 485 and 250+30 > self.mouse[1] > 250:
            pygame.draw.rect(self.win, [200,200,200],(485,250,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,250,150,30))

        if 485+150 > self.mouse[0] > 485 and 300+30 > self.mouse[1] > 300:
            pygame.draw.rect(self.win, [200,200,200],(485,300,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,300,150,30))

        button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Single Player", button1)
        textRect.center = ( (485+(150/2)), (200+(30/2)) )
        self.win.blit(textSurf, textRect)

        button2 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Time Trails", button2)
        textRect.center = ( (485+(150/2)), (250+(30/2)) )
        self.win.blit(textSurf, textRect)

        button3 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Instructions", button3)
        textRect.center = ( (485+(150/2)), (300+(30/2)) )
        self.win.blit(textSurf, textRect)

    def game_intro(self):
        intro = True
        

        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.buttons()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    if 485+150 > self.mouse[0] > 485 and 200+30 > self.mouse[1] > 200:
                        sg = SinglePlayer()
                    if 485+150 > self.mouse[0] > 485 and 300+30 > self.mouse[1] > 300:
                        inst = instructions()
                    if 485+150 > self.mouse[0] > 485 and 250+30 > self.mouse[1] > 250:
                        tt = TimeTrails()
                        
            pygame.display.update()
            self.clock.tick(15)
            
class instructions():
    def __init__(self):
        self.win = pygame.display.set_mode((655,383))
        self.bg = pygame.image.load('instructions.jpg')
        self.win.blit(self.bg,(0,0))
        pygame.display.set_caption("Instructions")
        self.clock = pygame.time.Clock()
        self.game_intro()

    def game_intro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    m = mainScreen()
                    m.game_intro()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    ms = mainScreen()
                    ms.game_intro()
                    
            pygame.display.update()
            self.clock.tick(15)

class TimeTrails():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((655, 383))
        self.bg = pygame.image.load('mainscreen.jpg')
        self.win.blit(self.bg,(0,0))
        pygame.display.set_caption("TimeTrails")
        largeText = pygame.font.Font('Kardust TS Condensed Bold Italic.ttf',72)
        TextSurf, TextRect = self.text_objects("Time Trails", largeText)
        TextRect.center = ((655/2),(70))
        self.win.blit(TextSurf, TextRect)
        self.game_intro()

    def text_objects(self,text, font):
        black = [0,0,0]
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def levels(self):
        self.mouse = pygame.mouse.get_pos()
        if 485+150 > self.mouse[0] > 485 and 200+30 > self.mouse[1] > 200:
            pygame.draw.rect(self.win,[200,200,200],(485,200,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,200,150,30))

        if 485+150 > self.mouse[0] > 485 and 250+30 > self.mouse[1] > 250:
            pygame.draw.rect(self.win, [200,200,200],(485,250,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,250,150,30))


            
        button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Level 1", button1)
        textRect.center = ( (485+(150/2)), (200+(30/2)) )
        self.win.blit(textSurf, textRect)

        button2 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Level 2", button2)
        textRect.center = ( (485+(150/2)), (250+(30/2)) )
        self.win.blit(textSurf, textRect)

        msg = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Press q to go back", msg)
        textRect.center = ( (70+(134/2)), (340+(40/2)) )
        self.win.blit(textSurf, textRect)

    def game_intro(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    m = mainScreen()
                    m.game_intro()
                self.levels()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    ms = mainScreen()
                    ms.game_intro()
                    
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    if 485+150 > self.mouse[0] > 485 and 200+30 > self.mouse[1] > 200:
                        clr = color()
                        print(clr.game_intro())
                        c1 = course1_tt(clr.game_intro())
                    if 485+150 > self.mouse[0] > 485 and 250+30 > self.mouse[1] > 250:
                        clr = color()
                        print(clr.game_intro())
                        c2 = course2_tt(clr.game_intro())
            pygame.display.update()
            self.clock.tick(15)
        
        
class SinglePlayer():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((655, 383))
        self.bg = pygame.image.load('mainscreen.jpg')
        self.win.blit(self.bg,(0,0))
        pygame.display.set_caption("Single Player")
        largeText = pygame.font.Font('Kardust TS Condensed Bold Italic.ttf',72)
        TextSurf, TextRect = self.text_objects("Single Player", largeText)
        TextRect.center = ((655/2),(70))
        self.win.blit(TextSurf, TextRect)
        self.game_intro()
        
    
        

    def text_objects(self,text, font):
        black = [0,0,0]
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
    def levels(self):
        self.mouse = pygame.mouse.get_pos()
        if 485+150 > self.mouse[0] > 485 and 200+30 > self.mouse[1] > 200:
            pygame.draw.rect(self.win,[200,200,200],(485,200,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,200,150,30))

        if 485+150 > self.mouse[0] > 485 and 250+30 > self.mouse[1] > 250:
            pygame.draw.rect(self.win, [200,200,200],(485,250,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,250,150,30))



        button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Level 1", button1)
        textRect.center = ( (485+(150/2)), (200+(30/2)) )
        self.win.blit(textSurf, textRect)

        button2 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Level 2", button2)
        textRect.center = ( (485+(150/2)), (250+(30/2)) )
        self.win.blit(textSurf, textRect)



        msg = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Press q to go back", msg)
        textRect.center = ( (70+(134/2)), (340+(40/2)) )
        self.win.blit(textSurf, textRect)

    def game_intro(self):
        intro = True
    

        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    #pygame.quit()
                    #quit()
                    m = mainScreen()
                    m.game_intro()
                self.levels()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    ms = mainScreen()
                    ms.game_intro()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    if 485+150 > self.mouse[0] > 485 and 200+30 > self.mouse[1] > 200:
                        clr = color()
                        print(clr.game_intro())
                        c1 = course1(clr.game_intro())
                    if 485+150 > self.mouse[0] > 485 and 250+30 > self.mouse[1] > 250:
                        clr = color()
                        print(clr.game_intro())
                        c2 = course2(clr.game_intro())
            pygame.display.update()
            self.clock.tick(15)
        

sc = mainScreen()
sc.game_intro()





    
