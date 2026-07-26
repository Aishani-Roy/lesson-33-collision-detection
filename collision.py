import pygame
import random
SW=500
SH=400
MS=5
FS=72
pygame.init()
bg=pygame.transform.scale(pygame.image.load('bg.jpg'),(SW,SH))
font=pygame.font.SysFont("Times New Roman",FS)
class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.Color('dodgerblue'))  # Background color of sprite
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change,SW-self.rect.width,),0)
        self.rect.y=max(min(self.rect.y+y_change,SH-self.rect.height,),0)
all_sprites = pygame.sprite.Group()
sp1 = Sprite(pygame.Color("black"), 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites.add(sp1)

sp2 = Sprite(pygame.Color("red"), 20, 30)
sp2.rect.x = random.randint(0, 480)
sp2.rect.y = random.randint(0, 370)
all_sprites.add(sp2)

screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Collision Sprites")  
running=True
won=False 
clock=pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if not won:
        keys=pygame.key.get_pressed()
        x_change=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*MS
        y_change=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*MS 
        sp1.move(x_change,y_change) 
        if sp1.rect.colliderect(sp2.rect):
            all_sprites.remove(sp2)
            won=True
    screen.blit(bg,(0,0))
    all_sprites.draw(screen)

    if won:
        win_text=font.render("you win!",True,pygame.Color("purple"))
        screen.blit(win_text,((SW-win_text.get_width())//2,(SH-win_text.get_height())//2)) 
    pygame.display.flip()
    clock.tick(120) 
pygame.quit()              
