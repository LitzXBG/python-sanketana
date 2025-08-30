import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")
while True:
    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  pygame.draw.rect(screen,"#000091",[100,100,100,200],0)
  pygame.draw.rect(screen,"#FFFFFF",[200,100,100,200],0)
  pygame.draw.rect(screen,"#E1000F",[300,100,100,200],0)

  pygame.display.flip()
  #make flag of france