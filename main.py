#!/usr/bin/env python3

from src.constants import *
from src.game import *

def main():
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()

    game = Game2048()

    game.generate_new_tile()
    game.generate_new_tile()

    running = True

    while running:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_ESCAPE]:
                running = False

            if pressed[pygame.K_DOWN]:
                moved = game.move_numbers(DOWN)
                if moved:
                    game.generate_new_tile()

            if pressed[pygame.K_UP]:
                moved = game.move_numbers(UP)
                if moved:
                    game.generate_new_tile()

            if pressed[pygame.K_RIGHT]:
                moved = game.move_numbers(RIGHT)
                if moved:
                    game.generate_new_tile()

            if pressed[pygame.K_LEFT]:
                moved = game.move_numbers(LEFT)
                if moved:
                    game.generate_new_tile()


        screen.fill((0, 0, 0))
        game.draw_game(screen)
        pygame.display.flip()

        clock.tick(60)



if __name__ == '__main__':
    main()
    pygame.quit()
