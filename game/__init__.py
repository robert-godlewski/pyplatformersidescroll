import pygame

from character import Character


class Platformer:
    def __init__(self) -> None:
        # Tupple in RGB
        self.bg_color = (255,255,255)
        self.width = 1280
        self.height = 720
        # Frames Per Second
        self.fps = 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.title = "Platformer"

    def run(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        clock = pygame.time.Clock()
        running = True
        # delta time in seconds since last frame
        dt = 0

        player_size = 20 # radius of a circle
        player_pos = pygame.Vector2(self.width/2,self.height-player_size)

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(self.bg_color)

            pygame.draw.circle(surface=self.screen, color="red", center=player_pos, radius=player_size)
            keys = pygame.key.get_pressed()
            # if keys[pygame.K_UP] or keys[pygame.K_w]:
            #     player_pos.y -= 300 * dt
            # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            #     player_pos.y += 300 * dt
            if keys[pygame.K_LEFT]:
                player_pos.x -= 300 * dt
            if keys[pygame.K_RIGHT]:
                player_pos.x += 300 * dt

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            dt = clock.tick(self.fps)/1000

        pygame.quit()
