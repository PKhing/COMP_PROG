# Lab_BNK48 
import pygame as pg
cnt = 0
def edge(ball_rect,ball_speed):
    if ball_rect.left < 0:
        ball_speed[0] = abs(ball_speed[0])
    if ball_rect.right > width:
        ball_speed[0] = -abs(ball_speed[0])
    if ball_rect.top < 0:
        ball_speed[1] = abs(ball_speed[1])
    if ball_rect.bottom > height:
        ball_speed[1] = -abs(ball_speed[1])
def collision(b1_r,b1_spd,b2_r,b2_spd):
    r1 = (b1_r.right-b1_r.left)/2
    x1 = (b1_r.right+b1_r.left)/2
    y1 = (b1_r.top+b1_r.bottom)/2
    r2 = (b2_r.right-b2_r.left)/2
    x2 = (b2_r.right+b2_r.left)/2
    y2 = (b2_r.top+b2_r.bottom)/2
    if(r1+r2>=((x2-x1)**2+(y2-y1)**2)**(1/2)):
        global cnt
        cnt+=1
        soundeffect.play()
        if x1<x2:
            b1_spd[0]=-abs(b1_spd[0]) 
            b2_spd[0]=abs(b2_spd[0])
        else: 
            b1_spd[0]=abs(b1_spd[0]) 
            b2_spd[0]=-abs(b2_spd[0])
        if y1<y2:
            b1_spd[1]=-abs(b1_spd[1])   
            b2_spd[1]=abs(b2_spd[1])
        else:
            b1_spd[1]=abs(b1_spd[1])   
            b2_spd[1]=-abs(b2_spd[1])
        upspeed(b1_spd)
        upspeed(b2_spd)
def upspeed(spd):
    global cnt
    if cnt>=10:
        return
    if spd[0]<0:
        spd[0]-=1
    if spd[0]>0:
        spd[0]+=1
    if spd[1]<0:
        spd[1]-=1
    if spd[1]>0:
        spd[1]+=1
    


# TODO 1 : กำหนด width : 1000 , height : 600 และ FPS : 60
width = 1000
height = 600
FPS = 60

# TODO 2 : กำหนดค่าสีดังนี้ pink : (197,142,195) , white : (255,255,255)
pink = (197,142,195)
white = (255,255,255)

# TODO 3 : กำหนดความเร็วให้กับ member แต่ละคน [ 3 member ]
ball1_speed = [2,2]
ball2_speed = [-3,4]
ball3_speed = [3,-2]

# TODO 4 : initialize pygame variable and create clock
pg.init()
clock = pg.time.Clock()
running = True

# TODO 5 : create screen [pygame.display.set_mode] 
# and set caption [pygame.display.set_caption] => "BNK_BALL (Heavy Collision)"
screen = pg.display.set_mode((width,height))
pg.display.set_caption("BNK_BALL (Heavy Collision)")

# TODO 6
#Load sound [change your sound filepath according to your computer]
pg.mixer.init()
pg.mixer.music.load("c:/Users/Khing/Desktop/Code/Python/Workshop/Workshop1-BNK_BALL_student/source/sound.mp3")
pg.mixer.music.play(-1, 0.0)

# ใช้คำสั่ง soundeffect.play() เพื่อเล่นเสียง effect ตอนลูกบอลชนกัน
soundeffect = pg.mixer.Sound("c:/Users/Khing/Desktop/Code/Python/Workshop/Workshop1-BNK_BALL_student/source/effect.wav")
soundeffect.set_volume(0.3)
# Choose 3 members from BNK48 and create pygame object from  get_rect
# [ load , resize , get_rect ]

# Member 1 [size : (150 , 150) , center : (500 , 250) ]
ball1_img = pg.image.load("c:/Users/Khing/Desktop/Code/Python/Workshop/Workshop1-BNK_BALL_student/source/BNK48/Wee_cc.png").convert_alpha()
ball1_img = pg.transform.scale(ball1_img, (150, 150))
ball1_rect = ball1_img.get_rect(center=(500,250))

# TODO 7 : create object with attribute in each comment
# Member 2 [size : (100 , 100) , center : (250 , 120)]

ball2_img = pg.image.load("c:/Users/Khing/Desktop/Code/Python/Workshop/Workshop1-BNK_BALL_student/source/BNK48/Cherprang_cc.png").convert_alpha()
ball2_img = pg.transform.scale(ball2_img, (100, 100))
ball2_rect = ball2_img.get_rect(center=(250,120))


# Member 3 [size : (120 , 120) , center : (800 , 400)]

ball3_img = pg.image.load("c:/Users/Khing/Desktop/Code/Python/Workshop/Workshop1-BNK_BALL_student/source/BNK48/Pun_cc.png").convert_alpha()
ball3_img = pg.transform.scale(ball3_img, (120, 120))
ball3_rect = ball3_img.get_rect(center=(800,400))

while running:
    # TODO 8 : set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม [clock.tick(...)]
    
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
            pg.quit()

    if running:
        # TODO 9 :ใส่สี background สีชมพู (screen.fill(...))
        screen.fill(pink)

        # TODO 10 : ให้ member ทั้ง 3 คนเคลื่อนที่ตามทิศทางและความเร็วเป็นไปตาม speed ของแต่ละคน
        ball1_rect = ball1_rect.move(ball1_speed)
        ball2_rect = ball2_rect.move(ball2_speed)
        ball3_rect = ball3_rect.move(ball3_speed)

        # TODO 11 : วาด text คำว่า "Heavy Collision" [size : 150 , center :(width/2 , height/3), สีขาว]
        font_name = pg.font.match_font('arial')  # กำหนดชื่อ Font
        font = pg.font.Font(font_name, 150)  # กำหนดขนาด font
        text_surface = font.render("Heavy Collision", True, white) # กำหนด Text และ สี
        text_rect = text_surface.get_rect() # แปลง Surface เป็น object
        text_rect.midtop = (int(width/2), int(height/3)) # ระบุตำแหน่งของ text
        screen.blit(text_surface, text_rect) # เอา Text ใส่ลงใน object ของ Text นั้น

        # TODO 12 : วาด text รหัสนิสิต ลงไป ข้างใต้คำว่า "Heavy Collision" [size : 100 ,center :(width/2 , height/1.5), สีขาว]
        # [ขนาดและตำแหน่งสามารถปรับได้ตามความเหมาะสม]
        font = pg.font.Font(font_name, 100)
        text_surface = font.render("6332031221", True, white) # กำหนด Text และ สี
        text_rect = text_surface.get_rect() # แปลง Surface เป็น object
        text_rect.midtop = (int(width/2), int(height/1.5)) # ระบุตำแหน่งของ text
        screen.blit(text_surface, text_rect) # เอา Text ใส่ลงใน object ของ Text นั้น

        # TODO 13 : เขียนเงื่อนไขไม่ให้ตกกรอบทุกด้านให้กับ member ทั้ง 3 คน
        edge(ball1_rect,ball1_speed)
        edge(ball2_rect,ball2_speed)
        edge(ball3_rect,ball3_speed)

        # Special point ทำให้ลูกบอลชนกันแล้วเด้งในทิศตรงกันข้าม
        collision(ball1_rect,ball1_speed,ball2_rect,ball2_speed)
        collision(ball3_rect,ball3_speed,ball2_rect,ball2_speed)
        collision(ball1_rect,ball1_speed,ball3_rect,ball3_speed)

        ################################################

        # TODO 14 : เอาภาพของ member แต่ละคนใส่ลงใน object ของตนเอง
        screen.blit(ball1_img, ball1_rect)
        screen.blit(ball2_img, ball2_rect)
        screen.blit(ball3_img, ball3_rect)

        ##########################################################

        pg.display.flip()