import cv2
import pygame

from hand_tracking import HandTracker
from gesture import getCommand

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x = 400
y = 300

speed = 5

tracker = HandTracker()

cap = cv2.VideoCapture(0)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    frame, points = tracker.findHand(frame)

    command = getCommand(points)

    if command == "UP":
        y -= speed

    elif command == "DOWN":
        y += speed

    elif command == "LEFT":
        x -= speed

    elif command == "RIGHT":
        x += speed

    screen.fill((30, 30, 30))

    pygame.draw.circle(screen, (0, 255, 0), (x, y), 20)

    font = pygame.font.SysFont(None, 36)
    text = font.render(command, True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.flip()

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

    clock.tick(60)

cap.release()
cv2.destroyAllWindows()
pygame.quit()