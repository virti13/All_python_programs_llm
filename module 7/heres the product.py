import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Product Store")

font = pygame.font.Font(None, 40)

product = "Apple"
price = 50

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    product_text = font.render("Product: " + product, True, (0, 0, 0))
    price_text = font.render("Price: ₹" + str(price), True, (0, 0, 0))

    screen.blit(product_text, (150, 120))
    screen.blit(price_text, (150, 180))

    pygame.display.update()

pygame.quit()