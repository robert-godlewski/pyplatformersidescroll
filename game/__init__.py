import pygame

from .character import Character


class Platformer:
    def __init__(self) -> None:
        pygame.init()
        # Tupple in RGB
        self.bg_color = (255,255,255)
        self.width = 1280
        self.height = 720
        # Frames Per Second
        self.fps = 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Platformer")
        player_size = 20
        self.player = Character((255,0,0), player_size, player_size, self.width/2, self.height-player_size)


    def run(self):
        clock = pygame.time.Clock()
        running = True
        # delta time in seconds since last frame
        dt = 0
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(self.bg_color)

            self.player.draw(self.screen)
            keys = pygame.key.get_pressed()
            # if keys[pygame.K_UP] or keys[pygame.K_w]:
            #     player_pos.y -= 300 * dt
            # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            #     player_pos.y += 300 * dt
            if keys[pygame.K_LEFT]:
                self.player.move_left(dt)
            if keys[pygame.K_RIGHT]:
                self.player.move_right(dt)

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            dt = clock.tick(self.fps)/1000

        pygame.quit()
