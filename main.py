import cv2
import pygame

from hand_tracking import HandTracker
from gesture import getCommand
from environment import *

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drone Simulator")

clock = pygame.time.Clock()

# ---------------- Drone ---------------- #

x = WIDTH // 2
y = HEIGHT // 2

speed = 5

# Load Drone Image
drone_img = pygame.image.load("assets/drone.png").convert_alpha()
drone_img = pygame.transform.scale(drone_img, (80, 80))

angle = 0
target_angle = 0

# ---------------- Camera ---------------- #

tracker = HandTracker()
cap = cv2.VideoCapture(0)

font = pygame.font.SysFont("Arial", 30)

running = True

while running:

    # ---------------- Events ---------------- #

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------- Webcam ---------------- #

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    frame, points = tracker.findHand(frame)

    command = getCommand(points)

    # ---------------- Movement ---------------- #

    if command == "UP":
        y -= speed
        target_angle = 0

    elif command == "DOWN":
        y += speed
        target_angle = 180

    elif command == "LEFT":
        x -= speed
        target_angle = 90

    elif command == "RIGHT":
        x += speed
        target_angle = -90

    # Smooth Rotation

    angle += (target_angle - angle) * 0.15

    # Window Boundary

    x = max(40, min(WIDTH - 40, x))
    y = max(40, min(HEIGHT - 40, y))

    # ---------------- Draw Environment ---------------- #

    drawSky(screen)
    drawSun(screen)
    drawClouds(screen)
    drawMountains(screen)
    drawBuildings(screen)
    drawTrees(screen)
    drawGrass(screen)
    drawRoad(screen)
    drawBirds(screen)

    # ---------------- Drone Shadow ---------------- #

    pygame.draw.ellipse(
        screen,
        (30, 30, 30),
        (x - 22, y + 28, 45, 12)
    )

    # ---------------- Drone Image ---------------- #

    rotated_drone = pygame.transform.rotate(drone_img, angle)

    drone_rect = rotated_drone.get_rect(center=(x, y))

    screen.blit(rotated_drone, drone_rect)

    # ---------------- HUD ---------------- #

    altitude = HEIGHT - y

    speed_text = font.render(f"Speed : {speed}", True, (255, 255, 255))
    altitude_text = font.render(f"Altitude : {int(altitude)}", True, (255, 255, 255))
    command_text = font.render(f"Command : {command}", True, (255, 255, 255))

    screen.blit(speed_text, (10, 10))
    screen.blit(altitude_text, (10, 45))
    screen.blit(command_text, (10, 80))

    pygame.display.flip()

    # ---------------- OpenCV ---------------- #

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) == 27:
        break

    clock.tick(60)

cap.release()
cv2.destroyAllWindows()
pygame.quit()