#!/usr/bin/env python3

from src.constants import *
import pygame
import random

class Game2048:
    def __init__(self):
        self.size = GAME_SIZE
        self.structure = [[0 for x in range(self.size)] for y in range(self.size)]


    def __str__(self):
        result = ""
        for y in range(self.size):
            result += str([x for x in self.structure[y]]) + "\n"
        return result


    def __eq__(self, other):
        for y in range(self.size):
            for x in range(self.size):
                if not (self.structure[y][x] == other.structure[y][x]):
                    return False
        return True


    def move_numbers(self, direction):
        print("Move numbers")
        moved_status = False
        if direction == DOWN:
            print("Move down")
            for x in range(GAME_SIZE):
                x_line = []
                for y in range(GAME_SIZE - 1, -1, -1):
                    x_line.append(self.structure[y][x])
                result, moved = self.compute_block_move(x_line)
                if moved:
                    moved_status = True
                for y in range(GAME_SIZE - 1, -1, -1):
                    self.structure[y][x] = result[-y-1]

        if direction == UP:
            print("Move up")
            for x in range(GAME_SIZE):
                x_line = []
                for y in range(GAME_SIZE):
                    x_line.append(self.structure[y][x])
                result, moved = self.compute_block_move(x_line)
                if moved:
                    moved_status = True
                for y in range(GAME_SIZE):
                    self.structure[y][x] = result[y]

        if direction == LEFT:
            print("Move left")
            for index, y_line in enumerate(self.structure):
                result, moved = self.compute_block_move(y_line)
                if moved:
                    moved_status = True
                self.structure[index] = result

        if direction == RIGHT:
            print("Move right")
            for index, y_line in enumerate(self.structure):
                result, moved = self.compute_block_move(y_line, direction=-1)
                if moved:
                    moved_status = True
                self.structure[index] = result

        print("Moved: {}".format(moved_status))
        return moved_status


    def compute_block_move(self, line, direction=1):
        def revert_line(line):
            return [number for number in list(reversed(line))]

        r_line = revert_line(line) if direction == -1 else line

        append_zeros = 0
        result = []
        number_added = False
        for number in r_line:
            if number == 0:
                append_zeros += 1
                number_added = False

            elif number != 0 and len(result) == 0:
                result.append(number)
                number_added = False

            elif number != 0 and len(result) != 0:
                if number == result[-1] and not number_added:
                    result[-1] += number
                    append_zeros += 1
                    number_added = True
                else:
                    result.append(number)
                    number_added = False

        final_result = []

        if direction == 1:
            final_result = result
            for i in range(append_zeros):
                final_result.append(0)

        elif direction == -1:
            for zero in range(append_zeros):
                final_result.append(0)
            for number in revert_line(result):
                final_result.append(number)

        else:
            exit(1)

        moved = True if line != final_result else False
        return final_result, moved


    def generate_new_tile(self):
        new_number = None
        if random.randint(0, 9) == 9:
            new_number = 4
        else:
            new_number = 2

        empty_tiles = []
        for y in range(GAME_SIZE):
            for x in range(GAME_SIZE):
                if self.structure[y][x]==0:
                    empty_tiles.append((y,x))
        if len(empty_tiles) == 0:
            return False

        new_tile_index = random.randint(0, len(empty_tiles) - 1)
        self.structure[empty_tiles[new_tile_index][0]][empty_tiles[new_tile_index][1]] = new_number
        return True

    def draw_game(self, screen):
        self.draw_blocks(screen)
        self.draw_grid(screen)
        # print(game) # prints visual representation of 2d array


    def draw_grid(self, screen):
        for y in range(GAME_SIZE):
            for x in range(GAME_SIZE):
                pygame.draw.rect(screen, GRID_COLOR, pygame.Rect(BASE_START_X + (x * BLOCK_SIZE), BASE_START_Y + (y * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE), 1)


    def draw_blocks(self, screen):
        def draw_number(screen, number, base):
            draw_text = pygame.font.SysFont("comicsansms", TEXT_SIZE).render(str(number), True, (0,0,0))
            text_rect = draw_text.get_rect(center=(int(base[0] + BLOCK_SIZE/2), int(base[1] + BLOCK_SIZE/2)))
            screen.blit(draw_text, text_rect)

        for y in range(GAME_SIZE):
            for x in range(GAME_SIZE):
                current_number = self.structure[y][x]
                if current_number != 0:
                    try:
                        block_color = GAME_COLORS_BY_NUMBER[current_number]
                    except Exception:
                        block_color = GAME_ELSE_COLOR

                    pygame.draw.rect(screen, block_color, pygame.Rect(BASE_START_X + (x * BLOCK_SIZE), BASE_START_Y + (y * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE))
                    draw_number(screen, current_number, (BASE_START_X + (x * BLOCK_SIZE), BASE_START_Y + (y * BLOCK_SIZE)))
