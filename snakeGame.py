import pygame
import time
import random
import tkinter as tk
from tkinter import messagebox

pygame.init()

screen_width = 800
screen_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

block_size = 20
snake_speed = 10

font = pygame.font.SysFont(None, 40)

def snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(gameDisplay, green, [segment[0], segment[1], block_size, block_size])

def pesan_layar(psn, color):
    teks_layar = font.render(psn, True, color)
    gameDisplay.blit(teks_layar, [(screen_width - teks_layar.get_width()) / 2, (screen_height - teks_layar.get_height()) / 2])

def tampilkan_skor(skor):
    teks_skor = font.render("Skor: " + str(skor), True, black)
    gameDisplay.blit(teks_skor, [10, 10])

def tampilkan_popup():
    root = tk.Tk()
    root.withdraw()
    result = messagebox.askquestion("Keluar", "Apakah Anda yakin ingin keluar dari permainan?")
    root.destroy()
    return result

def gameLoop():
    gameExit = False
    gameOver = False 

    lead_x = screen_width / 2
    lead_y = screen_height / 2

    lead_x_change = 0 
    lead_y_change = 0 

    snake_list = []
    snake_length = 1 

    randAppleX = round(random.randrange(0, screen_width - block_size ) / 20.0) * 20.0
    randAppleY = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0 
    
    score = 0

    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            pesan_layar("Game Over", red)
            tampilkan_skor(score)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        choice = tampilkan_popup()
                        if choice == "yes":
                            gameExit = True
                            gameOver = False
                        else:
                            gameOver = False
                            score = 0
                            gameLoop()
                    elif event.key == pygame.K_c:
                        gameOver = False
                        score = 0
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for eachSegment in snake_list[:-1]:
            if eachSegment == snake_head:
                gameOver = True

        snake(snake_list)
        tampilkan_skor(score)

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
            randAppleY = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0
            snake_length += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameDisplay = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

gameLoop()
