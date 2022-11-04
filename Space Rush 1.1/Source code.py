from cmath import rect
from pygame import mixer
import json
import pygame
import random
import time

# intialize the pygame
pygame.init()

# intialize the mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

# title and stuff
pygame.display.set_caption('Space Rush by @itsswaggy')
icon = pygame.image.load('Spaceship.png')
pygame.display.set_icon(icon)

# create window
screen = pygame.display.set_mode((800, 600))

# load the sounds
laser_fx = pygame.mixer.Sound("lazer.wav")
laser_fx.set_volume(0.55)

ex = pygame.mixer.Sound("explosion.wav")
ex.set_volume(0.60)

# background music
bgmusic = pygame.mixer.Sound("bgmusic.wav")
bgmusic.play(-1)
bgmusic.set_volume(0.75)

# score and stuff
shine = 0
score = -1
highscore = 0
font = pygame.font.Font('Bubblegum.ttf', 22)
font1 = pygame.font.Font('Bubblegum.ttf', 16)
font2 = pygame.font.Font('Bubblegum.ttf', 48)

def show_score():
    score_value = font.render('Score: ' + str(score), True, (255,255,255))
    screen.blit(score_value, (345, 20))

def high_score():
    highscore_value = font.render('Highscore: ' + str(highscore), True, (255,255,255))
    screen.blit(highscore_value, (323, 40))

def esc_to():
    esc_to_ = font1.render('ESC to pause', True, (255,255,255))
    screen.blit(esc_to_, (688, 10))

with open('virus.txt') as highscore_file:
    highscore = json.load(highscore_file)

# press q to quit
def q_to_quit():
    q_to = font1.render('Press Q to quit.', True, (255,255,255))
    screen.blit(q_to, (10, 10))

# baground
bg = pygame.image.load('bg.png')

# spaceship
playerImg = pygame.image.load('Spaceship.png')
hitbox = playerImg.get_rect()
vel = 2
hitbox.y = 268

# small asteroid
asteroid_smallImg = pygame.image.load('asteroid.png')
hitbox_ = asteroid_smallImg.get_rect()
vel_ = 1

# check if the player can restart
check = False
# check if main menu = true
mainmenu = False
# check if pausescreen = true
pausescreen = False

# aliens
alienImg = pygame.image.load('Invader.png')
hitbox___ = alienImg.get_rect()
vel___ = 1
hitbox___.x = 530

alien_Img = pygame.image.load('Invader.png')
alien_hitbox = alien_Img.get_rect()
speed___ = 2
alien_hitbox.x = 630

# big asteroid
big_asteroidImg = pygame.image.load('Big_asteroid.png')
hitbox__ = big_asteroidImg.get_rect()
vel__ = 0.5
hitbox__.y = -150

# bullets
bulletImg = pygame.image.load('laser.png')
bullet_hitbox = bulletImg.get_rect()
speed_ = 2.1
bullet_hitbox.x = -50
bullet_hitbox.y = 0

bullet_Img = pygame.image.load('laser.png')
bullet__hitbox = bullet_Img.get_rect()
speed__ = 2.1
bullet__hitbox.x = -50
bullet__hitbox.y = 0

player_bullet = pygame.image.load('laser.png')
pbullet_hitbox = player_bullet.get_rect()
pbullet_speed = 2.5
pbullet_hitbox.x = 2000

# point
pointImg = pygame.image.load('asteroid.png')
point = pointImg.get_rect()
point_speed = 4
point.y

# blue scoreboard
bluebg = pygame.image.load('spacebg.png')

running = True
while running:

        # RGB
        screen.fill((149, 27, 218))
        # bagground
        screen.blit(bg, (0,0))

        # define quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('virus.txt', 'w') as highscore_file:
                    json.dump(highscore,highscore_file)

                running = False

        # keyboard input
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_RIGHT]:
            hitbox.x += vel
        if userInput[pygame.K_LEFT]:
            hitbox.x -= vel
        if userInput[pygame.K_UP]:
            hitbox.y -= vel
        if userInput[pygame.K_DOWN]:
            hitbox.y += vel
        if userInput[pygame.K_d]:
            hitbox.x += vel
        if userInput[pygame.K_a]:
            hitbox.x -= vel
        if userInput[pygame.K_w]:
            hitbox.y -= vel
        if userInput[pygame.K_s]:
            hitbox.y += vel
        if userInput[pygame.K_SPACE] and pbullet_hitbox.x == 2000:
            pbullet_hitbox.x = hitbox.x
            pbullet_hitbox.y = hitbox.y
            laser_fx.play()
        if userInput[pygame.K_ESCAPE] and check == True:
            hitbox.x = 0
            hitbox.y = 268
            hitbox__.x = 0
            hitbox__.y = -150
            bullet_hitbox.x = -70
            bullet__hitbox.x = -70
            hitbox_.x = 736
            hitbox_.y = 150
            score = 1
            speed_ = 2.1
            speed__ = 2.1
            speed___ = 2
            vel = 2
            vel_ = 1
            vel__ = 0.5
            vel___ = 1
            point_speed = 4
            pbullet_speed = 2.5
            shine = 1
            check = False
        if userInput[pygame.K_g] and score == 0 and mainmenu == True:
            hitbox.x = 0
            hitbox.y = 268
            hitbox__.x = 0
            hitbox__.y = -150
            bullet_hitbox.x = -70
            bullet__hitbox.x = -70
            hitbox_.x = 736
            hitbox_.y = 150
            score += 1
            speed_ = 2.1
            speed__ = 2.1
            speed___ = 2
            vel = 2
            vel_ = 1
            vel__ = 0.5
            vel___ = 1
            point_speed = 4
            pbullet_speed = 2.5
            mainmenu = False
        if userInput[pygame.K_ESCAPE] and score >= 3 and mainmenu == False and check == False:
            pausescreen = True
        if userInput[pygame.K_e] and pausescreen == True and mainmenu == False and check == False:
            pausescreen = False
            score += 1
            speed_ = 2.1
            speed__ = 2.1
            speed___ = 2
            vel = 2
            vel_ = 1
            vel__ = 0.5
            vel___ = 1
            point_speed = 4
            pbullet_speed = 2.5
        if userInput[pygame.K_q]:
            with open('highscore.txt', 'w') as highscore_file:
                json.dump(highscore,highscore_file)
            pygame.quit()

        # movement
        if hitbox_.x >= 0:
            hitbox_.x -= vel_
        
        if hitbox__.x >= 0:
            hitbox__.x -= vel__

        if score == 10:
            hitbox__.y = 112

        if hitbox___.y <= 600:
            hitbox___.y += vel___

        if alien_hitbox.y <= 600:
            alien_hitbox.y += vel___

        if score > 9:
            vel = 2

        if bullet_hitbox.x > -70:
            bullet_hitbox.x -= speed_

        if bullet__hitbox.x > -70:
            bullet__hitbox.x -= speed__
        
        if pbullet_hitbox.x < 2000:
            pbullet_hitbox.x += pbullet_speed

        # point clock
        if point.x > 0:
            point.x -= point_speed
        
        if point.x <= 5:
            point.x = 736
            shine += 1
            score += 1

        if score > highscore:
            highscore += 1

        # player bounderies
        if hitbox.y <= 0:
            hitbox.y = 0
        elif hitbox.y >= 536:
            hitbox.y = 536
            
        if hitbox.x <= 0:
            hitbox.x = 0
        elif hitbox.x >= 736:
            hitbox.x = 736

        # if the asteroid hits the left side, tp back
        if hitbox_.x <= 1:
            hitbox_.x = 736
            hitbox_.y = random.randint(1,536)
            vel_ += 0.03
        
        if score > 9 and hitbox__.x <= 0:
            hitbox__.x = 672
            hitbox__.y = random.randint(1,472)
            vel__ += 0.09
        
        if bullet_hitbox.x < 0 and shine > 20 and hitbox___.y == 268:
            bullet_hitbox.y = 268
            bullet_hitbox.x = 530
            laser_fx.play()
        
        if bullet_hitbox.x < 0 and shine > 20 and hitbox___.y == 532:
            bullet_hitbox.y = 532
            bullet_hitbox.x = 530
            laser_fx.play()
        
        if bullet_hitbox.x < 0 and shine > 20 and hitbox___.y == 30:
            bullet_hitbox.y = 30
            bullet_hitbox.x = 530
            laser_fx.play()

        if bullet__hitbox.x < 0 and shine > 35 and alien_hitbox.y == 400:
            bullet__hitbox.y = 400
            bullet__hitbox.x = 630
            laser_fx.play()
        
        if bullet__hitbox.x < 0 and shine > 35 and alien_hitbox.y == 132:
            bullet__hitbox.y = 132
            bullet__hitbox.x = 630
            laser_fx.play()

        if hitbox___.y >= 572:
            vel___ *= -1
        
        if hitbox___.y <= 0:
            vel___ *= -1
        
        if alien_hitbox.y >= 572:
            speed___ *= -1
        
        if alien_hitbox.y <= 0:
            speed___ *= -1

        screen.blit(playerImg, hitbox)
        screen.blit(asteroid_smallImg, hitbox_)
        screen.blit(big_asteroidImg, hitbox__)
        screen.blit(bulletImg, bullet_hitbox)
        screen.blit(bullet_Img, bullet__hitbox)
        screen.blit(player_bullet, pbullet_hitbox)
            
        if shine >= 20:
            screen.blit(alienImg, hitbox___)

        if shine >= 35:
            screen.blit(alien_Img, alien_hitbox)

        # define if the hitboxes hit eachother
        if hitbox.colliderect(hitbox_):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True

            screen.blit(bluebg, (0,0))

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 270))

            restart()

        if hitbox.colliderect(hitbox__):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True

            screen.blit(bluebg, (0,0))

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 270))

            restart()

        if shine > 20 and hitbox.colliderect(hitbox___):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True

            screen.blit(bluebg, (0,0))

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 270))

            restart()

        if shine > 35 and hitbox.colliderect(alien_hitbox):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True

            screen.blit(bluebg, (0,0))

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 320))

            restart()

        if hitbox.colliderect(bullet_hitbox):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True

            screen.blit(bluebg, (0,0))

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 270))

            restart()

        if hitbox.colliderect(bullet__hitbox):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True

            screen.blit(bluebg, (0,0))

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 270))

            restart()

        if score == 0:
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            mainmenu = True

            screen.blit(bluebg, (0,0))

            def main_menu():
                main_pen = font2.render('Press G to start', True, (255,255,255))
                screen.blit(main_pen, (190, 270))

            main_menu()

        if pausescreen == True:
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0

            screen.blit(bluebg, (0,0))

            def pause():
                esc_to = font2.render('Press E to resume', True, (255,255,255))
                screen.blit(esc_to, (145, 270))
            
            pause()
        
        if pbullet_hitbox.colliderect(hitbox_):
            hitbox_.y = -150
            ex.play()
        
        if pbullet_hitbox.colliderect(hitbox__):
            hitbox__.y = -150
            ex.play()
        
        if shine >= 35 and pbullet_hitbox.colliderect(alien_hitbox):
            shine -= 5

        if shine >= 20 and pbullet_hitbox.colliderect(hitbox___):
            shine -= 5

        # update the window
        esc_to()
        high_score()
        q_to_quit()
        show_score()
        pygame.time.delay(3)
        pygame.display.update()    

