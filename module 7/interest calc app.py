import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Interest Calculator")

font = pygame.font.Font(None, 40)

principal = 1000
rate = 5
time = 2

# Simple Interest formula
interest = (principal * rate * time) / 100

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    title = font.render("Interest Calculator", True, (0, 0, 0))
    p_text = font.render("Principal: ₹" + str(principal), True, (0, 0, 0))
    r_text = font.render("Rate: " + str(rate) + "%", True, (0, 0, 0))
    t_text = font.render("Time: " + str(time) + " years", True, (0, 0, 0))
    result = font.render("Simple Interest: ₹" + str(interest), True, (0, 0, 0))

    screen.blit(title, (160, 50))
    screen.blit(p_text, (160, 110))
    screen.blit(r_text, (160, 160))
    screen.blit(t_text, (160, 210))
    screen.blit(result, (160, 270))

    pygame.display.update()

pygame.quit()