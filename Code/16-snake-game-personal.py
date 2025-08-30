import pygame,sys,random
#game constants

WIDTH,HEIGHT = 800,600
WHITE = (255,255,255)
GRID_SIZE = 20
SNAKE_SPEED = 20
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
snake_x = WIDTH/2
snake_y = HEIGHT/2
remove = True
apple_position_x = random.randint(8,800)
apple_position_y  = random.randint(8,600)
score = 0
game_state = "running"


# create a text surface object,
# on which text is drawn on it.

direction = (0,0)
FPS = 10
snake = [(WIDTH/2,HEIGHT/2),(WIDTH/2 +GRID_SIZE, HEIGHT/2)]
clock = pygame.time.Clock()


pygame.init()
font = pygame.font.Font('ADLaMDisplay-Regular.ttf', 32)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snaka game")


#Game loop
while True:
  screen.fill(WHITE)
  apple = pygame.draw.rect(screen,RED,(apple_position_x,apple_position_y,GRID_SIZE,GRID_SIZE))
  #event loop
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_s:
        direction = (0,1)
      elif event.key == pygame.K_w:
        direction = (0,-1)
      elif event.key  == pygame.K_a:
        direction =  (-1,0)
      elif event.key == pygame.K_d:
        direction = (1,0)
  #clock tick
 
  #controls here
  #extract the head element
  head_x,head_y = snake[0]
  #find position of the new head 
  head_x = head_x+direction[0]*GRID_SIZE
  head_y = head_y+direction[1]*GRID_SIZE

  #create a new head
  new_head = (head_x,head_y)
  new_head_rect = pygame.Rect(new_head[0], new_head[1], GRID_SIZE, GRID_SIZE)
  #add the head 
  snake.insert(0,new_head)
  if remove:
   
    snake.pop()
  


  

  
  if new_head_rect.colliderect(apple):
    apple_position_x = random.randint(8,800)
    remove = False
    score+=1
    apple_position_y  = random.randint(8,600)
  else:
    remove = True
  if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
    remove = False
    game_over = font.render(f"Score: {score}, GAME OVER", True,BLACK)
    screen.blit(game_over,(GRID_SIZE,GRID_SIZE))
  
  

  
  clock.tick(FPS)
  #rendering here
  for part in snake:
    pygame.draw.rect(screen,BLUE,(part[0],part[1],GRID_SIZE,GRID_SIZE))
  text = font.render(f"Score: {score}", True,BLACK)
  screen.blit(text,(GRID_SIZE,GRID_SIZE))
  

  pygame.display.flip()
  