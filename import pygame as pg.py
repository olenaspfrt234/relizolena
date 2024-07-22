import pygame as pg
from random import*

width=700
height=600



white=(255,255,255)
black=(0,0,0)
frog_l=[
    pg.image.load("Idle (32x32)_1.png"),
    pg.image.load("Idle (32x32)_2.png"),
    pg.image.load("Idle (32x32)_3.png"),
    pg.image.load("Idle (32x32)_4.png"),
    pg.image.load("Idle (32x32)_5.png"),
    pg.image.load("Idle (32x32)_6.png"),
    pg.image.load("Idle (32x32)_7.png"),
    pg.image.load("Idle (32x32)_8.png"),
    pg.image.load("Idle (32x32)_9.png"),
    pg.image.load("Idle (32x32)_10.png"),
    pg.image.load("Idle (32x32)_11.png"),
        
]
window=pg.display.set_mode((width,height))

class GameSprite:
    def __init__(self,image,x,y,width,height,iw,ih):
        self.image=pg.transform.scale(pg.image.load(image),(iw,ih))
        self.rect=pg.Rect(x,y,width,height)
        self.count = 0
        self.left = False
        self.right= False
        # self.player_l = player_l
        # self.player_r = player_r
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    

class Animation(GameSprite):
   
    # def __init__(self, image, x, y, width, height, iw, ih, frames):
    #     super().__init__(image, x=x, y=y, width=width, height=height, iw=iw, ih=ih)
    #     self.frames = frames
    #     self.current_frame = 0
    #     self.animation_speed = 10  # frames per second
    #     self.last_update = pg.time.get_ticks()

    # def update(self):
    #     self.animate()
    #     window.blit(self.image, (self.rect.x, self.rect.y))

    # def animate(self):
    #     now = pg.time.get_ticks()
    #     if now - self.last_update > 1000 / self.animation_speed:
    #         self.last_update = now
    #         self.current_frame = (self.current_frame + 1) % len(self.frames)
    #         self.image = self.frames[self.current_frame]
    def update(self):
            keys = pg.key.get_pressed()

            if keys[pg.K_LEFT] :
                self.rect.x -= 3
                self.left = True
                self.right = False

            elif keys[pg.K_RIGHT] :
                self.left = False
                self.right = True
                self.rect.x += 3
            else:
                self.right = self.left = False
            
    def animation(self):
        if self.left:
            self.count = (self.count + 1) % len(frog_l)  
            window.blit(frog_l[self.count], (self.rect.x, self.rect.y))
        elif self.right:
            self.count = (self.count + 1) % len(frog_l)  
            window.blit(frog_l[self.count], (self.rect.x, self.rect.y))
        else:
            self.count = (self.count + 1) % len(frog_l)  
            window.blit(frog_l[self.count], (self.rect.x, self.rect.y))

class Object(GameSprite):
    def move(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rect.y-=5
        if keys[pg.K_DOWN]:
            self.rect.y+=5
        if keys[pg.K_LEFT]:
            self.rect.x-=5
        if keys[pg.K_RIGHT]:
            self.rect.x+=5

def load_animation(image_path, frame_width, frame_height, num_frames):
    image = pg.image.load(image_path).convert_alpha()
    frames = []
    for i in range(num_frames):
        frame = pg.Surface((frame_width, frame_height), pg.SRCALPHA)
        frame.blit(image, (0, 0), (i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames

# frog=pg.transform.scale(pg.image.load("frog.png"),(width,height))

frog_l=[
    pg.image.load("Idle (32x32)_1.png"),
    pg.image.load("Idle (32x32)_2.png"),
    pg.image.load("Idle (32x32)_3.png"),
    pg.image.load("Idle (32x32)_4.png"),
    pg.image.load("Idle (32x32)_5.png"),
    pg.image.load("Idle (32x32)_6.png"),
    pg.image.load("Idle (32x32)_7.png"),
    pg.image.load("Idle (32x32)_8.png"),
    pg.image.load("Idle (32x32)_9.png"),
    pg.image.load("Idle (32x32)_10.png"),
    pg.image.load("Idle (32x32)_11.png"),
        
]

frog = Animation("Idle (32x32)_6.png", 100, 250, 50, 50, 50, 50) 

fon=pg.transform.scale(pg.image.load("fonmain.png"),(width,height))
clock = pg.time.Clock()

run =True

while run:
    for e in pg.event.get():
        if e.type==pg.QUIT:
            run =False
    window.blit(fon,(0,0))

    frog.animation()
    frog.update()
    pg.display.update()
    clock.tick(60)