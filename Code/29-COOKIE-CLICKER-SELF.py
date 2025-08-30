import pygame
import os,sys
pygame.init()

#constannts
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
BROWN = (205,133,163)
GREEN = (0,255,0)
WHITE  = (255,255,255)
START_TITLE_Y = 90
START_INSTRUCTION1_Y = 150
START_INSTRUCTION2_Y = 120
PLAY_BUTTON_Y = 500
PLAY_BUTTON_RECT_Y = 500
PLAY_BUTTON_WIDTH = 200
PLAY_BUTTON_HEIGHT = 90
PLAY_BUTTON_RECT = pygame.Rect(SCREEN_WIDTH//2,PLAY_BUTTON_RECT_Y,PLAY_BUTTON_WIDTH,PLAY_BUTTON_HEIGHT)
PLAY_BUTTON_RECT.center = (SCREEN_WIDTH // 2, PLAY_BUTTON_Y)

#game states

STATE_START = "start"
STATE_PLAYING = "running"
STATE_WIN = "win"
STATE_REPLAY = "replay"
GAME_STATE = STATE_START
def draw_text(text,font,colour,x,y):
  text_surface = font.render(text,True,colour)
  text_rect = text_surface.get_rect(center=(x,y))
  return screen.blit(text_surface,text_rect)

title_font = pygame.font.Font(None,48)
small_font = pygame.font.Font(None,24)
medium_font = pygame.font.Font(None,36)

def draw_start_screen():
  #cookie clicker
  #click the cookie to earn cookie
  #erach 100 cookies to win
  #draw a start button
  draw_text("cookie clicker",title_font,BROWN,SCREEN_WIDTH//2,START_TITLE_Y)
  draw_text("click the cookie to earn cookie",medium_font,BROWN,SCREEN_WIDTH//2,START_INSTRUCTION1_Y)
  draw_text("reach 100 cookie to win",medium_font,BROWN,SCREEN_WIDTH//2,START_INSTRUCTION2_Y)
  draw_text("PLAY",title_font,GREEN,SCREEN_WIDTH//2,PLAY_BUTTON_Y)
def draw_playing_screen():
  pass
def draw_win_screen():
  pass

#load the cookie image
background_image = pygame.image.load(os.path.join("assets","BG.png"))
background_image = pygame.transform.scale(background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
cookie_image = pygame.image.load
running = True

pygame.display.set_caption("Cookie Clicker")
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running  = False
    elif event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_ESCAPE:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if PLAY_BUTTON_RECT.collidepoint(event.pos):
        GAME_STATE = STATE_PLAYING

  if GAME_STATE == STATE_START:
    screen.blit(background_image, (0,0))
    pygame.draw.rect(screen, WHITE, PLAY_BUTTON_RECT)
    draw_start_screen()
  elif GAME_STATE == STATE_PLAYING:
    screen.blit(background_image, (0,0))
 

  pygame.display.flip()


pygame.quit()
sys.exit()