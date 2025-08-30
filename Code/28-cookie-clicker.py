import pygame
import os,sys
pygame.init()
#constannts
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
BROWN = (205,133,163)
GREEN = (50,205,50)
WHITE  = (255,255,255)
START_TITLE_Y = 90
START_INSTRUCTION1_Y = 150
START_INSTRUCTION2_Y = 120
PLAY_BUTTON_Y = 500
DARK_GREY = (64,64,64)
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 200
COOKIE_X = 300
COOKIE_Y = 400
count = 0

background_image = pygame.image.load(os.path.join("assets","BG.png"))
background_image = pygame.transform.scale(background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
Cookie_image = pygame.image.load(os.path.join("assets","COOKIE.png"))
Cookie_image = pygame.transform.scale(Cookie_image,(300,300))
cookie_rect = Cookie_image.get_rect()
cookie_rect.center = (COOKIE_X,COOKIE_Y)
background_sound = pygame.mixer.music.load(os.path.join("assets","bg_score.mp3"))
cookie_click_sound = pygame.mixer.Sound(os.path.join("assets","snap.wav"))

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
def create_button(text,x,y,height,width,colour):
  button_rect = pygame.Rect(x,y,width,height)
  button_rect.center = (x,y)

  pygame.draw.rect(screen,colour,button_rect)
  pygame.draw.rect(screen,DARK_GREY,button_rect,2)
  text_surface = medium_font.render(text,False,DARK_GREY)  
  text_rect = text_surface.get_rect(center = button_rect.center) 
  screen.blit(text_surface,text_rect)
  return button_rect


title_font = pygame.font.Font(None,48)
small_font = pygame.font.Font(None,24)
medium_font = pygame.font.Font(None,36)

def draw_start_screen():
  global start_button_rect
  #cookie clicker
  #click the cookie to earn cookie
  #erach 100 cookies to win
  #draw a start button
  draw_text("cookie clicker",title_font,BROWN,SCREEN_WIDTH//2,START_TITLE_Y)
  draw_text("click the cookie to earn cookie",medium_font,BROWN,SCREEN_WIDTH//2,START_INSTRUCTION1_Y)
  draw_text("reach 100 cookie to win",medium_font,BROWN,SCREEN_WIDTH//2,START_INSTRUCTION2_Y)
  pygame.mixer.music.play()

  start_button_rect = create_button("Play",SCREEN_WIDTH/2,SCREEN_HEIGHT/2,BUTTON_HEIGHT,BUTTON_WIDTH,GREEN)

  
def handle_start_screen_click(mousepos):
  global GAME_STATE
  if start_button_rect and start_button_rect.collidepoint(mousepos):
    GAME_STATE = STATE_PLAYING
def handle_playing_screen_click(mouse_pos):
  global count
  global GAME_STATE
  if cookie_rect and cookie_rect.collidepoint(mouse_pos):
    cookie_click_sound.play()
    count+=1
    if count==100:
      GAME_STATE = STATE_WIN

def handle_mouse_click(mousepos):
  if GAME_STATE == STATE_START:
    handle_start_screen_click(mousepos)
  elif GAME_STATE == STATE_PLAYING:
    handle_playing_screen_click(mousepos)
    




def draw_playing_screen():
  draw_text("Cookie clicker",title_font,BROWN,SCREEN_WIDTH//2,START_TITLE_Y)
  draw_text("Click to earn cookies",medium_font,BROWN,SCREEN_WIDTH//2,START_INSTRUCTION1_Y)
  draw_text("Reach 100 cookies to win. ",medium_font,BROWN,SCREEN_WIDTH//2,START_INSTRUCTION2_Y)
  draw_text(f'you need {100-count} clicks to win',medium_font,BROWN,SCREEN_WIDTH//2,COOKIE_Y+200)
  screen.blit(Cookie_image,cookie_rect)

def draw_win_screen():
  draw_text("You Won!",title_font,BROWN,SCREEN_WIDTH//2,START_TITLE_Y)
  draw_text("You reached the end!",title_font,BROWN,SCREEN_WIDTH//2,START_INSTRUCTION1_Y)
  pygame.mixer.music.stop()


#load the cookie image

running = True
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Cookie Clicker")
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running  = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        handle_mouse_click(event.pos)
  screen.blit(background_image, (0,0))
  if GAME_STATE == STATE_START:
    draw_start_screen()
  elif GAME_STATE == STATE_PLAYING:
    draw_playing_screen()
  elif GAME_STATE == STATE_WIN:
    draw_win_screen()

  pygame.display.flip()


pygame.quit()
sys.exit()