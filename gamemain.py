import numpy,pygame as pg
import game_logic_final as gl
tilecolor = (0,185,255)

def init_grid():
    grid_sizey = 0
    grid_sizex = 0
    mines = 0
    while grid_sizey<5 or grid_sizey>16:
        grid_sizey = int(input("Enter the HEIGHT of the grid (5 to 15)- "))
    while grid_sizex < 5 or grid_sizex > 30:
        grid_sizex = int(input("Enter the WIDTH of the grid (5 to 26)- "))
    while mines < (grid_sizex*grid_sizey)*0.07 or grid_sizey > (grid_sizex*grid_sizey)*0.7:
        mines = int(input("Enter the number of MINES - "))
    gridfun = numpy.zeros((grid_sizey, grid_sizex))
    return grid_sizey, grid_sizex, gridfun, mines


def create_grid():
    for i in range(0,grid_sizey):
        pos_list2 = []
        for j in range(0,grid_sizex):
            pg.draw.rect(screen,tilecolor,[(width/2-((height/tile_side)*grid_sizex/2))+(j*height/tile_side),(height/2-((height/tile_side)*grid_sizey/2))+23+(i*height/tile_side),height/tile_side-8,height/tile_side-8])
            pos_list2.append([(width/2-((height/tile_side)*grid_sizex/2))+(j*height/tile_side),(height/2-((height/tile_side)*grid_sizey/2))+23+(i*height/tile_side)])
        pos_list.append(pos_list2)
        #print(pos_list2)
        pg.time.delay(70)
        pg.display.update()

def click(posx,posy):
    for i in range(0,grid_sizey):
        for j in range(0, grid_sizex):
            if (posx >= pos_list[i][j][0] and posx <= pos_list[i][j][0]+height/tile_side-8) and (posy >= pos_list[i][j][1] and posy <= pos_list[i][j][1]+height/tile_side-8):
                temp = int(grid[i][j])
                #print(temp)
                if temp == -1:
                    uncover_tile(i,j)
                    tile_clickmine()
                else:
                    tile_clicknormal(i,j)


#def value_recurr():
def tile_clickmine():
    counter =  0
    pg.time.delay(1200)
    for k in range(0,grid_sizey):
        for l in range(0,grid_sizex):
            temp = int(grid[k][l])
            #print(temp)
            if temp == -1:
                counter +=1
                uncover_tile(k,l)
                pg.time.delay(10)
                pg.time.delay(250-(counter*20))
    pg.time.delay(1000)
    pg.draw.rect(screen, (0,0,0),(width/2 - 170,height/2 - 60,355,75))
    wintext = "Game Over!"
    font = pg.font.SysFont('Consolas', 60)
    wintext = font.render(wintext, True, (255, 0, 0))
    screen.blit(wintext, (width/2 - 150,height/2 - 50))
    pg.display.update()
    pg.time.delay(2000)

def tile_clicknormal(i,j):
    #grid_row = int(i/grid_sizex)
    #grid_column = i - (grid_row * grid_sizex)
    if uncover[i][j] == 0:
        pg.time.delay(12)
        if grid[i][j] == 0:
            uncover_tile(i, j)
            if j + 1 < grid_sizex:
                tile_clicknormal(i, j+1)
            if i + 1 < grid_sizey and j + 1 < grid_sizex:
                tile_clicknormal(i+1, j+1)
            if j - 1 >= 0:
                tile_clicknormal(i, j-1)
            if i + 1 < grid_sizey:
                tile_clicknormal(i+1, j)
            if i - 1 >= 0:
                tile_clicknormal(i-1, j)
            if i + 1 < grid_sizey and j - 1 >= 0:
                tile_clicknormal(i+1, j-1)
            if i - 1 >= 0 and j + 1 < grid_sizex:
                tile_clicknormal(i-1, j+1)
            if i - 1 >= 0 and j - 1 >= 0:
                tile_clicknormal(i-1, j-1)
        else:
            uncover_tile(i, j)
'''
        for k in range(0,8):
            if k==0:
                i = i+1
            elif k==1:
                i = i+1
                j = j-1
            elif k==2:
                i = i+1
                j = j+1
            elif k==3:
                i = i-1
            elif k==4:
                i = i-1
                j = j+1
            elif k==5:
                i = i-1
                j = j-1
            elif k==6:
                j = j+1
            else:
                j = j-1
            if (i>0 and i<grid_sizey) and j>0 and j<grid_sizex:
                tile_clicknormal(i,j)'''
    #print(height/grid_sizey-12)
    #print(grid[grid_row][i-(grid_row*grid_sizex)])
    #print(i,i/grid_sizey,i%grid_sizey)
    #print(text)


def uncover_tile(i,j):
    uncover[i][j] = 1
    text = str(int(grid[i][j]))
    colorrect = (0,0,0)
    #print(text)
    specialh = 0.07
    specials = 0.8
    color = ()
    if text == '-1':
        text = '*'
        specialh = 0.15
        specials = 0.90
        color = (0,0,0)
        colorrect = (255,0,0)
    elif text == '0':
        color = (255,255,255)
    elif text == '1':
        color = (0,0,255)
    elif text == '2':
        color = (0,255,0)
    else:
        color = (255,0,0)
    pg.draw.rect(screen, colorrect,[pos_list[i][j][0] + 2, pos_list[i][j][1] + 2, height/tile_side - 12, height / tile_side - 12])
    font = pg.font.SysFont('Consolas', int((height / tile_side) * specials))
    text = font.render(text, True, color)
    screen.blit(text, (pos_list[i][j][0] + (height/tile_side) * 0.2, pos_list[i][j][1] + (height / tile_side) * specialh))
    pg.display.update()



'''---------------------------------START------------------------------------------------------------------------------'''
grid_sizey,grid_sizex,grid,mines = init_grid()
tile_side = 17
uncover = numpy.zeros((grid_sizey, grid_sizex))
pos_list = []
pg.init()
mainloop = True
screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
infoobject = pg.display.Info()
height = infoobject.current_h
width = infoobject.current_w
'''class tile:
    side = height/10 #grid_sizey
    value ='''
grid = gl.make_grid(grid,grid_sizey,grid_sizex,mines)
#print(grid)
#mousex = 0
#mousey = 0
font = pg.font.SysFont('Consolas', 170)
text = font.render("Minesweeper", True, (255,255,255))
screen.blit(text,(190,300))
pg.display.update()
pg.time.delay(800)
screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
pg.time.delay(500)
create_grid()
font = pg.font.SysFont('Consolas', 20)
text = font.render("ESC to Exit", True, (255,255,255))
screen.blit(text,(width + 70,height))
pg.display.update()
while mainloop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mainloop=False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                mainloop = False
        if pg.mouse.get_pressed()[0]:
            mouse_posx,mouse_posy = pg.mouse.get_pos()
            #if mouse_posx!=mousex and mouse_posy!=mousey:
            click(mouse_posx,mouse_posy)
        temp = numpy.count_nonzero(uncover == 0)
        if  temp == mines:
            pg.time.delay(1000)
            wintext = "You Win!"
            font = pg.font.SysFont('Consolas', 70)
            pg.draw.rect(screen, (0, 0, 0), (width / 2 - 170, height / 2 - 60, 355, 75))
            wintext = font.render(wintext, True, (0,255,0))
            screen.blit(wintext, (width/2 - 150,height/2 - 50))
            pg.display.update()
            pg.time.delay(2000)
            mainloop = False
            #mousex, mousey = mouse_posx, mouse_posy
            #print(mouse_posx,mouse_posy)
    #screen.fill((255,255,255))
    #pg.display.update()
pg.quit()