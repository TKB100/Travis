import pygame
import math

WIDTH = 800
HEIGHT = 600
BACKGROUND = (0, 0, 0)

EYE_COLOR = (255, 255, 255)
EYE_WIDTH = 80
EYE_HEIGHT = 120
EYE_GAP = 80

GLASSES_COLOR = (255, 0, 0)
FRAME_THICKNESS = 6
FRAME_PAD = 20

MOUTH_COLOR = (255, 255, 255)
MOUTH_WIDTH = 160
MOUTH_HEIGHT = 60
MOUTH_THICKNESS = 6

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Travis")
clock = pygame.time.Clock()

center_x = WIDTH // 2
center_y = HEIGHT // 2

left_eye_x = center_x - EYE_GAP // 2 - EYE_WIDTH
right_eye_x = center_x + EYE_GAP // 2
eye_y = center_y - EYE_HEIGHT // 2

frame_width = EYE_WIDTH + FRAME_PAD * 2
frame_height = EYE_HEIGHT + FRAME_PAD * 2
frame_y = eye_y - FRAME_PAD
left_frame_x = left_eye_x - FRAME_PAD
right_frame_x = right_eye_x - FRAME_PAD

bridge_start = (left_frame_x + frame_width, center_y)
bridge_end = (right_frame_x, center_y)

mouth_x = center_x - MOUTH_WIDTH // 2
mouth_y = frame_y + frame_height + 30

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    pygame.draw.ellipse(screen, EYE_COLOR, (left_eye_x, eye_y, EYE_WIDTH, EYE_HEIGHT))
    pygame.draw.ellipse(screen, EYE_COLOR, (right_eye_x, eye_y, EYE_WIDTH, EYE_HEIGHT))

    pygame.draw.rect(screen, GLASSES_COLOR, (left_frame_x, frame_y, frame_width, frame_height), FRAME_THICKNESS, border_radius=20)
    pygame.draw.rect(screen, GLASSES_COLOR, (right_frame_x, frame_y, frame_width, frame_height), FRAME_THICKNESS, border_radius=20)
    pygame.draw.line(screen, GLASSES_COLOR, bridge_start, bridge_end, FRAME_THICKNESS)

    pygame.draw.arc(screen, MOUTH_COLOR, (mouth_x, mouth_y, MOUTH_WIDTH, MOUTH_HEIGHT), math.pi, 2 * math.pi, MOUTH_THICKNESS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()