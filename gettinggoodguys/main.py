import pygame

from main_loop import MainLoop


def main():
    pygame.init()
    pygame.font.init()

    main_loop = MainLoop()
    main_loop.start_main_loop()


if __name__ == "__main__":
    main()
