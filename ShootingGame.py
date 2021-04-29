import pygame
import sys
import random
import os
from time import sleep

BLACK = (0, 0, 0)
screen_width = 480
screen_height = 640
# rock_image= ["C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock01.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock02.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock03.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock04.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock05.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock06.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock07.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock08.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock09.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock10.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock11.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock12.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock13.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock14.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock15.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock16.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock17.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock18.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock19.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock20.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock21.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock22.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock23.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock24.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock25.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock26.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock27.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock28.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock29.png", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\rock30.png"]
# explosionSound = ["C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\explosion01.wav", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\explosion02.wav", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\explosion03.wav", "C:\\Users\\Jyosun\\Desktop\\PYTHON\\ShootingGame\\images\\explosion04.wav"]

def drawObject(obj, x, y):
    global screen
    screen.blit(obj, (x, y))
    
def writeScore(count):
    global screen
    font = pygame.font.Font(None, 30)
    text = font.render("Score:" + str(count), True, (255, 255, 255))
    screen.blit(text, (10, 0))
    
def writePassed(count):
    global screen
    font = pygame.font.Font(None, 30)
    text = font.render("LossScore:" + str(count), True, (255, 0, 0))
    screen.blit(text, (350, 0))
    
def writeMessage(text):
    global screen, gameOverSound
    textFont = pygame.font.Font(None, 60)
    text = textFont.render(text, True, (255, 0, 0))
    text_pos = text.get_rect()
    text_pos.center = (screen_width / 2, screen_height / 2)
    screen.blit(text, text_pos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameOverSound.play()
    sleep(2)
    pygame.mixer.music.play(-1)
    runGame()
    
def crash():
    global screen
    writeMessage('Destroyed!')
    
def gameOver():
    global screen
    writeMessage("Game Over!")

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("요순이가 만든 슈팅게임")

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background.png"))
fighter = pygame.image.load(os.path.join(image_path, "fighter.png"))
missile = pygame.image.load(os.path.join(image_path, "missile.png"))
explosion = pygame.image.load(os.path.join(image_path, "explosion.png"))
rock_image = pygame.image.load(os.path.join(image_path, "rock01.png"))
pygame.mixer.music.load(os.path.join(image_path, "music.wav"))
pygame.mixer.music.play(-1)
explosionSound = pygame.mixer.Sound(os.path.join(image_path, "explosion01.wav"))
missileSound = pygame.mixer.Sound(os.path.join(image_path, "missile.wav"))
gameOverSound = pygame.mixer.Sound(os.path.join(image_path, "gameover.wav"))
clock = pygame.time.Clock()
    
def runGame():
    global screen, clock, background, fighter, missile, explosion, missileSound
    
    fighter_size = fighter.get_rect().size
    fighter_width = fighter_size[0]
    fighter_height = fighter_size[1]
    fighter_speed = 7
    
    x = screen_width * 0.45
    y = screen_height * 0.9
    fighter_x = 0
    
    missile_xy = []
    
    rock = rock_image
    rock_size = rock.get_rect().size
    rock_width = rock_size[0]
    rock_height = rock_size[1]
    destroySound = pygame.mixer.Sound(explosionSound)
    
    rock_x = random.randrange(0, screen_width - rock_width)
    rock_y = 0
    rock_speed = 2
    
    isShot = False
    shotCount = 0
    rockPassed = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    fighter_x -= fighter_speed
                    
                elif event.key == pygame.K_RIGHT:
                    fighter_x += fighter_speed
                    
                elif event.key == pygame.K_SPACE:
                    missileSound.play()
                    missile_x = x + fighter_width / 2
                    missile_y = y - fighter_height
                    missile_xy.append([missile_x, missile_y]) 
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter_x = 0
                
        drawObject(background, 0, 0)
        
        x += fighter_x
        if x < 0:
            x=0
        elif x > screen_width - fighter_width:
            x = screen_width - fighter_width
        
        rock_y += rock_speed
            
        if y < rock_y + rock_height:
            if(rock_x > x and rock_x < x + fighter_width) or \
                (rock_x + rock_width > x and rock_x + rock_width < x + fighter_width):
                crash()
        
        drawObject(fighter, x, y)
        
        if len(missile_xy) != 0:
            for i, bxy in enumerate(missile_xy):
                bxy[1] -= 10
                missile_xy[i][1] = bxy[1]
                
                if bxy[1] < rock_y:
                    if bxy[0] > rock_x and bxy[0] < rock_x + rock_width:
                        missile_xy.remove(bxy)
                        isShot = True
                        shotCount += 1
                
                if bxy[1] <= 0:
                    try:
                        missile_xy.remove(bxy)
                    except:
                        pass
                    
        if len(missile_xy) != 0:
            for bx, by in missile_xy:
                drawObject(missile, bx, by)
                
        writeScore(shotCount)
        
        if rock_y > screen_height:
            rock = rock_image
            rock_size = rock.get_rect().size
            rock_width = rock_size[0]
            rock_height = rock_size[1]
            rock_x = random.randrange(0, screen_width - rock_width)
            rock_y = 0
            rockPassed += 1
            
        if rockPassed == 3:
            gameOver()
        
        writePassed(rockPassed)
            
        if isShot:
            drawObject(explosion, rock_x, rock_y)
            destroySound.play()
            rock = rock_image
            rock_size = rock.get_rect().size
            rock_width = rock_size[0]
            rock_height = rock_size[1]
            rock_x = random.randrange(0, screen_width - rock_width)
            rock_y = 0
            destroySound = pygame.mixer.Sound(explosionSound)
            isShot = False
            
            rock_speed += 0.1
            if rock_speed >=10:
                rock_speed = 10
            
        drawObject(rock, rock_x, rock_y)
        
        pygame.display.update()
        
        clock.tick(60)
    
    pygame.quit()
    
runGame()
