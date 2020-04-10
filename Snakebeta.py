
# import the moubles
import pygame
import random
Setter = input("Select hardness,(1)Hard, (2)Normal, (3)Easy ")
Name = input("Please type in your in game name ")
# pygame acts
pygame.init()
# make varibles
Window_width = 700
Window_height = 700
Window = pygame.display.set_mode((Window_width, Window_height))
pygame.display.set_caption("Snake (Beta version)")
width = 40
timer_count = 0
x_leaf = random.randint(0, 660)
y_leaf = random.randint(0, 660)
x = 0
y = 0
x_mouse = 5
score_plus = 20
y_mouse = 5
lives = 3
Speed_snake = 15
y_button = 630
x_button = 630
leaf_width = 20
font = pygame.font.Font(None, 30)
NameTag_font = pygame.font.Font(None, 15)
Button_font = pygame.font.Font(None, 50)
leaf_height = 20
score = 0
x_c = 0
red = pygame.Color(255, 51, 0)
y_c = 0
checkout_y = 640
mouse_pos = MouseAcess_x, MouseAcess_y = pygame.mouse.get_pos()
checkout_x = 580
height = 40
enemies = []
x_gro = 0
y_gro = 640
width_gro = 970
height_gro = 40
running = True
clock = pygame.time.Clock()
# Set up the game loop
while running:
    mouse = pygame.mouse.get_pos()
    (x_mouse, y_mouse) = pygame.mouse.get_pos()
    timer_count = timer_count + 1
    white = pygame.Color(225, 225, 225)
    Window.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if Button.colliderect(mousegh):
            running = False
            print("Your score is: " + str(score))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_c = x_c + -40
        y_c = 0
    if keys[pygame.K_RIGHT]:
        x_c = x_c + 40
        y_c = 0
    if keys[pygame.K_DOWN]:
        y_c = y_c + 40
        x_c = 0
    if keys[pygame.K_UP]:
        y_c = y_c + -40
        x_c = 0
    if keys[pygame.K_h]:
        Speed_snake = Speed_snake - 2
        print("You used a cheat code!")
    if keys[pygame.K_s]:
        print("You used a cheat code!")
        Speed_snake = Speed_snake + 2
    x = x + x_c
    y = y + y_c
    clock.tick(Speed_snake)
    char1 = pygame.draw.rect(Window, (255, 51, 0), (x_leaf, y_leaf, leaf_width, leaf_height))
    mousegh = pygame.draw.rect(Window, (0, 0, 0), (x_mouse, y_mouse, 15, 15))
    Button = pygame.draw.rect(Window, (0, 0, 0), (x_button, y_button, 100, 35))
    checkout = pygame.draw.rect(Window, red, (checkout_x, checkout_y, 15, 15))
    Button_say = Button_font.render("Exit", True, red)
    Window.blit(Button_say, (x_button, y_button+2))
    char = pygame.draw.rect(Window, (0, 204, 102), (x, y, width, height))
    # Set up the eating apple part!
    if char.colliderect(char1):
        score = score + score_plus
        y = y
        x = x
        y_c = 0
        x_c = 0
        x_leaf = random.randint(0, 660)
        y_leaf = random.randint(0, 660)
        # Leave the game at you like it or not
    if keys[pygame.K_ESCAPE]:
        print("Your score is: " + str(score))
        running = False
    # Go back to your oranigal postion
    if keys[pygame.K_g]:
        y = 0
        x = 0
        x_c = 0
        y_c = 0

    # WIN!!!!!
    if score == 100 or score > 100:
        red = pygame.Color(0, 204, 102)
        winner = font.render("You win! Your score is: " + str(score) + " Press Esc to leave! Or click the Exit button!", True, (0, 0, 0))
        Window.blit(winner, (0, 350))
    # How hard it is
    if Setter == "1":
        if y == 640 or y == -640 or x == 640 or x == -640:
            lives -= 1
            if lives == 3:
                running = False
                print("You lost!")

    if Setter == "3":
        if y == 740 or y == -740 or x == 740 or x == -740:
            y = 0
            x = 0
            x_c = 0
            y_c = 0
    # Display score
    textY = 10
    textX = 10
    def Showscore(x, y):
        score_shower = font.render("Score: " + str(score) + " Get 100 points to win! Speed: " + str(Speed_snake), True, (0, 0, 0))
        Window.blit(score_shower, (x, y))
    Showscore(textX, textY)
    def NameTagShow():
        name_y = y - 30
        name_x = x + 5
        nametag = NameTag_font.render(Name, True, (0, 0, 0))
        Window.blit(nametag, (name_x, name_y))
    if Speed_snake < 15:
        Speed_snake = 15
    NameTagShow()

    # update the screen
    pygame.display.update()
# Make sure pygame does not use wasted rescouses
pygame.quit()