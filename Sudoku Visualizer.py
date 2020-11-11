import pygame
pygame.font.init()


dis_width = 500
dis_height = 600
cell_color = (185, 224, 210)
box_color = (114, 151, 150)
box_thickness = 6
black = (0, 0, 0)
white = (255, 255, 255)
line_thickness1 = 1
line_thickness2 = 3
speed1 = 50
speed2 = 100
x = 0
y = 0
dif = 500 / 9
val = 0


screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("SUDOKU VISUALIZER")


grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0], 
    [5, 2, 0, 0, 0, 0, 0, 0, 0], 
    [0, 8, 7, 0, 0, 0, 0, 3, 1], 
    [0, 0, 3, 0, 1, 0, 0, 8, 0], 
    [9, 0, 0, 8, 6, 3, 0, 0, 5], 
    [0, 5, 0, 0, 9, 0, 6, 0, 0], 
    [1, 3, 0, 0, 0, 0, 2, 5, 0], 
    [0, 0, 0, 0, 0, 0, 0, 7, 4], 
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

bigFont = pygame.font.SysFont(None, 40)
smallFont = pygame.font.SysFont(None, 22)

def selected():
    for i in range(2):
        pygame.draw.line(screen, box_color, (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), box_thickness)
        pygame.draw.line(screen, box_color, ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), box_thickness) 

def board():
    for i in range(9):
        for j in range(9):
            if(grid[i][j]!=0):
                pygame.draw.rect(screen, cell_color, (i * dif, j * dif, dif + 1, dif + 1))    

                text1 = bigFont.render(str(grid[i][j]), 1, black)  
                screen.blit(text1, (i * dif + 20, j * dif + 17)) 
    for i in range(10):
        if(i%3==0):
            pygame.draw.line(screen, black, (0, i * dif), (500, i * dif), line_thickness2) 
            pygame.draw.line(screen, black, (i * dif, 0), (i * dif, 500), line_thickness2)	
        else:
            pygame.draw.line(screen, black, (0, i * dif), (500, i * dif), line_thickness1) 
            pygame.draw.line(screen, black, (i * dif, 0), (i * dif, 500), line_thickness1)	
         

def is_valid(grid, i, j, val):
    for it in range(9):
        if(grid[i][it] == val):
            return False
        if(grid[it][j] == val):
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3,jt * 3 + 3):
            if(grid[i][j] == val):
                return False
    return True

def solve_backtracking(grid, i, j):
    while(grid[i][j] != 0):
        if(i < 8):
            i += 1
        elif(i == 8 and j < 8):
            i = 0
            j += 1
        elif(i == 8 and j == 8):
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if(is_valid(grid, i, j, it)==True):
            grid[i][j] = it
            global x, y
            x = i
            y = j
            screen.fill(white)
            board()
            selected()
            pygame.display.update()
            pygame.time.delay(speed1)
            if(solve_backtracking(grid, i, j) == 1):
                return True
            else:
                grid[i][j] = 0
            screen.fill(white)
            board()
            selected()
            pygame.display.update()
            pygame.time.delay(speed2) 
    return False

def start():
    text1 = smallFont.render("PRESS ENTER TO START", 1, box_color)
    screen.blit(text1, (150, 540))

def end():
    text1 = smallFont.render("PRESS 'R' TO RESTART THE SUDOKU", 1, box_color)
    screen.blit(text1, (110, 520))
    text2 = bigFont.render("SOLVED!", 1, box_color)
    screen.blit(text2, (190, 552))

loop = True
flag1=0
flag2=0
rs=0
error=0

while loop:
    screen.fill(white)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            loop=False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RETURN):
                flag2=1
            if(event.key == pygame.K_r):
                rs=0
                error=0
                flag2=0
                flag1=0
                grid=[
                    [3, 0, 6, 5, 0, 8, 4, 0, 0], 
                    [5, 2, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 8, 7, 0, 0, 0, 0, 3, 1], 
                    [0, 0, 3, 0, 1, 0, 0, 8, 0], 
                    [9, 0, 0, 8, 6, 3, 0, 0, 5], 
                    [0, 5, 0, 0, 9, 0, 6, 0, 0], 
                    [1, 3, 0, 0, 0, 0, 2, 5, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 7, 4], 
                    [0, 0, 5, 2, 0, 6, 3, 0, 0]
                ]  
    if(flag2 == 1):
        if(solve_backtracking(grid, 0, 0) == False):
            error = 1
        else:
            rs = 1
        flag2 = 0
    if(rs == 1):
        flag1 = 1
        end()
    if(flag1 == 1):
        selected()
    if(flag1 == 0):    
        start()
    board()     

    pygame.display.update() 

pygame.quit()                                        