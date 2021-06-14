from random import randint
import pygame

pygame.init()

white = (255,255,255)
blue = (20,100,125)
black = (108,108,248)
red = (255,10,10)

screen_width=900
screen_height=600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("SNAKE GAME")
pygame.display.update()

font=pygame.font.SysFont(None,55)
clock = pygame.time.Clock()

bg = pygame.image.load("index1.jpg")
bgrect=bg.get_rect()
sn = pygame.image.load("index.png")
snrect=sn.get_rect()

def text_screen(text,color,x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot(gameWindow,color,snak_list,snake_size):
    for x,y in snak_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])


def gameloop():
    hscore=0
    try :
        f=open("hiscore.txt","r")
        hscore=int(f.read())
        f.close()
    except :
        f=open("hiscore.txt","w")
        f.write("0")
        hscore=0
        f.close()

    snak_list=[]
    snk_len=1
    exit_game=False
    game_over=False
    snake_x = 10
    snake_y = 55
    snake_size = 20
    velocity_x=3
    velocity_y=3
    fps = 60
    direction="right"
    food_x=randint(20,screen_width-20)
    food_y=randint(50,screen_height-20)
    score=0

    while not exit_game:
        if game_over:
            gameWindow.blit(bg, bgrect)
            text_screen("Score is "+str(score)+"    High Score"+str(hscore),blue,5,5)
            s="_"*screen_width
            text_screen(s,black,0,20)
            text_screen("Game Over!! Press Enter to continue", blue, 130,230)
            if score>=hscore:
                hscore=score
                f=open("hiscore.txt","w")
                f.write(str(hscore))
                f.close()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else :

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if snk_len>1:
                            if not direction=="left":
                                direction="right"
                        else :
                            direction="right"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if snk_len>1:
                            if not direction=="right":
                                direction="left"
                        else :
                            direction="left"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if snk_len>1:
                            if not direction=="down":
                               direction="up"
                        else:
                            direction="up"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if snk_len>1:
                            if not direction=="up":
                                direction="down"
                        else :
                            direction="down"
            
            if direction=="right":
                snake_x+=velocity_x
            elif direction=="left":
                snake_x-=velocity_x
            elif direction=="up":
                snake_y-=velocity_y
            elif direction=="down":
                snake_y+=velocity_y

            if (snake_x<5 or snake_x>screen_width-5 or snake_y<55 or snake_y>screen_height-5):
                game_over=True

            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score+=10
                food_x=randint(20,screen_width-20)
                food_y=randint(50,screen_height-20)
                snk_len+=5

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snak_list.append(head)

            if len(snak_list)>snk_len:
                del snak_list[0]

            if head in snak_list[:-1]:
                game_over=True

            gameWindow.blit(bg, bgrect)
            if score>hscore:
                hscore=score
            text_screen("Score is "+str(score)+"    High Score"+str(hscore),blue,5,5)
            s="_"*screen_width
            text_screen(s,black,0,20)
            pygame.draw.circle(gameWindow, red, (food_x,food_y), 10)
            plot(gameWindow,red,snak_list,snake_size)
            pygame.display.update()
            pygame.display.flip()
            clock.tick(fps)

def welcome():
    gameWindow.blit(bg, bgrect)
    gameWindow.blit(sn, snrect)
    font2=pygame.font.SysFont("Monotype corsiva",105)
    screen_text = font2.render("Snake Game", True, blue)
    gameWindow.blit(screen_text, [251,100])
    gameWindow.blit(font.render("Press Spacebar to continue",True,blue),[200,300])
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
    
welcome()
