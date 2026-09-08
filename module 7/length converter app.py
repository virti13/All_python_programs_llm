import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Length Converter")

font = pygame.font.Font(None, 40)

length = 10

# Convert meters to centimeters
cm = length * 100

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    title = font.render("Length Converter", True, (0, 0, 0))
    input_text = font.render("Meters: " + str(length), True, (0, 0, 0))
    result = font.render("Centimeters: " + str(cm), True, (0, 0, 0))

    screen.blit(title, (170, 80))
    screen.blit(input_text, (170, 150))
    screen.blit(result, (170, 220))

    pygame.display.update()

pygame.quit()