
import pygame
from pygame.locals import *
import time
import random


size=40
background_colour=(99,167,68)


class Apple:
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.image=pygame.image.load("resources/apple.jpg").convert()
        self.x=random.randint(0,47)*size
        self.y=random.randint(0,26)*size
        pygame.display.update()
    
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        

        
    def move(self):
        self.x=random.randint(0,47)*size
        self.y=random.randint(0,26)*size

class Snake:
    def __init__(self,parent_screen):
        self.length=1
        self.parent_screen = parent_screen
        self.block=pygame.image.load("resources/block.jpg").convert()
        self.x=[(random.randint(0,38))*40]
        self.y=[(random.randint(0,18)*40)]
        self.direction=''
    


    
    def move_left(self):
        self.direction = 'left'

  
  
    def move_right(self):
        self.direction = 'right'
   
   
    def move_down(self):
        self.direction ='down'
     
    
    def move_up(self):
        self.direction = 'up'


    def walk(self):
        
        for i in range(((self.length)-1),0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
     
        
        
        if self.direction == 'up':
            self.y[0] -=size
        
        if self.direction == 'down':
            self.y[0] +=size
        
        if self.direction == 'left':
            self.x[0] -=size
        
        if self.direction == 'right':
            self.x[0] +=size

        self.draw()

    def draw(self):
        self.parent_screen.fill(background_colour)
        
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.update()
       
  
    def increase_length(self):
        self.length+=1
        self.x.append(1)
        self.y.append(1)  
    

class Game:
    def __init__(self):
        pygame.init()
    
        self.surface=pygame.display.set_mode((1920,1080))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()


    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def collison(self,x1,y1,x2,y2):
        if x1+1 >= x2 and x1<=x2 :
             if y1+1 >= y2 and y1<=y2 :
                return True
        return False
    

                

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.update()
        
        
        if self.collison(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()
        
        if  (self.snake.x[0]<0) :
            raise "Game over"
        
        if  (self.snake.x[0]>1920) :
            raise "Game over"
        
        if  (self.snake.y[0]<0) :
            raise "Game over"
        
        if  (self.snake.y[0]>1080) :
            raise "Game over"

        for i in range(2,self.snake.length):
            if  self.collison(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                raise "Game over"
            
    
    
    def display_score(self):
        font=pygame.font.SysFont('comic sans',40)
        score=font.render(f"Score:{self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(835,5))
        pygame.display.update()
        
    
    def show_game_over(self):

        self.image=pygame.image.load("resources/background.jpg").convert()
        font=pygame.font.SysFont('arial',50)
        font1=pygame.font.SysFont('arial',90)
        
        message=font1.render("GAME OVER",True,(255,50,30))
        self.surface.blit(message,(750,100))
        
        message2=font.render(f"Your Score is : {self.snake.length}",True,(255,255,255))
        self.surface.blit(message2,(10,500))
        
        message3=font.render("If you want to try again press the enter button . If you want to quit press the escape button",True,(255,255,255))
        self.surface.blit(message3,(10,600))
        pause = True

        self.reset()
        pygame.display.update()
    


       

    def run(self):
        running=True 
        pause=False        
        while running:
            
            
            
            for event in pygame.event.get():
        
                if event.type ==KEYDOWN:

                    if event.key==K_RETURN:
                        pause=False   
                
                    if event.key==K_ESCAPE:
                        running=False
                    
                    if not pause:
                        if event.key==K_UP:
                            self.snake.move_up()
    
                    
                        if event.key==K_DOWN:
                            self.snake.move_down()
                       
                    
                        if event.key==K_LEFT:
                            self.snake.move_left()
               
        
                    
                        if event.key==K_RIGHT:
                            self.snake.move_right()
                
                elif event.type == QUIT:
                    running=False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            
            time.sleep(0.1)
       
            
            
    

if __name__=="__main__":
    game=Game()
    game.run()

    