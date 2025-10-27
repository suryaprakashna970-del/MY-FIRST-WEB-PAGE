import pygame
pygame.init()
# Set up display
gamedisplay = pygame.display.set_mode((500, 600))
pygame.display.set_caption('hunggery barid')



#game specific variables
exit_game = False
game_over = False

#create a game loop
while not exit_game:
    for event in pygame.event.get():
        # quit the game if the user clicks the close button
        if event.type == pygame.QUIT:
            exit_game = True
            # all the event works here
        if event.type == pygame.KEYDOWN:#ARROW KEYS
            if event.key == pygame.K_RIGHT:# right arrow key
                print("right arrow key is pressed")
                print(event)
            elif event.key == pygame.K_LEFT:# left arrow key
                print("left arrow key is pressed")
            elif event.key == pygame.K_UP:# up arrow key
                print("up arrow key is pressed")
            elif event.key == pygame.K_DOWN:# down arrow key
                print("down arrow key is pressed")
            elif event.key == pygame.K_KP_ENTER:# enter key
                print("ENTER key is pressed")
        elif event.type == pygame.MOUSEBUTTONDOWN:# mouse button
            print("mouse button is pressed")
            print(event)
pygame.quit()
quit()