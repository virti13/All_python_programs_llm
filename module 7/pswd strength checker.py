import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Password Strength Checker")

font = pygame.font.Font(None, 40)

password = "Hello123"

# Check password strength
if len(password) < 6:
    strength = "Weak"
elif len(password) < 10:
    strength = "Medium"
else:
    strength = "Strong"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    title = font.render("Password Strength Checker", True, (0, 0, 0))
    pass_text = font.render("Password: " + password, True, (0, 0, 0))
    result = font.render("Strength: " + strength, True, (0, 0, 0))

    screen.blit(title, (120, 80))
    screen.blit(pass_text, (160, 150))
    screen.blit(result, (160, 220))

    pygame.display.update()

pygame.quit()