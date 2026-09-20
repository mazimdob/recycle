import pygame
import time
import random

pygame.init()
pygame.display.set_caption("recycle game ")

screen_Width=900
screen_Height=700
screen=pygame.display.set_mode((screen_Width,screen_Height))

def changebackround():
    image=pygame.image.load("bground.png")
    image=pygame.transform.scale(image,(screen_Width,screen_Height))
    screen.blit(image,(0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class non_recycle(pygame.sprite.Sprite):
    def __init__(self ):
        super().__init__()
        self.image=pygame.image.load("plastic.png")
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

class recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image(30,30))
        self.rect=self.image.get_rect()
allsprites=pygame.sprite.Group()
item_list=pygame.sprite.Group()
plastic_list=pygame.sprite.Group()

bin=Bin()
allsprites.add(bin)

for i in range(20):
    plastic=non_recycle()
    plastic.rect.x=random.randrange(screen_Width)
    plastic.rect.y=random.randrange(screen_Height)
    plastic_list.add(plastic)
    allsprites.add(plastic)
images=["item1.png","item2.png","item3.png"]
for i in range(50):
    item=recyclable(random.choice(images))
    item.rect.x=random.randrange(screen_Width)
    item.rect.y=random.randrange(screen_Height)
    item_list.add(item)
    allsprites.add(item)

WHITE=(255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)
GREEN=(0,255,0)
playing=True
score=0

clock=pygame.time.Clock()
start_time=time.time()

myfont=pygame.font.SysFont("Times New Roman",22)
text=myfont.render("score="+str(0),True,BLACK)

while playing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    timeElapsed=time.time()-start_time
    if timeElapsed>=60:
        if score>=20:
            screen.fill(GREEN)
            myfont=pygame.font.SysFont("comic",50)
            text1=myfont.render("binloot successful",True,BLACK)
        else:
            screen.fill(RED)
            myfont=pygame.font.SysFont("comic",50)
            text1=myfont.render("binloot unsuccessful",True,BLACK)

        screen.blit(text1,(250,40))            
    else:
        changebackround()
        countdown=myfont.render("Time Left:"+str(60-int(timeElapsed)),True,BLACK)
        screen.blit(countdown,(20,10))

        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y>0:
                bin.rect.y-=5

        if keys[pygame.K_DOWN]:
            if bin.rect.y<630:
                bin.rect.y+=5

        if keys [pygame.K_RIGHT]:
            if bin.rect.x<850:
                bin.rect.x+=5

        if keys [pygame.K_LEFT]:
            if bin.rect.x>0:
                bin.rect.x-=5
