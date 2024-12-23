import pygame

width = 1000
height = 800
scale_sun = 0.00025
scale_planets = 0.005
distance_scale = 20
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar system 2d simulation")

class planet:
    def __init__(self, x, y, radius, img):
        self.x = x
        self.y = y
        self.radius = radius * scale_sun
        self.img = pygame.image.load(img)

    def draw(self, window):
        pygame.transform.scale(self.img, (self.radius/2, self.radius/2))
        window.blit(self.img, (self.x, self.y))



run = True
sun_radius = 432300
sun_x = width / 2 - (sun_radius * scale_sun) * 3/2
sun_y = height / 2 - (sun_radius * scale_sun) * 3/2
sun_color = (255, 120, 0)
sun = planet(sun_x, sun_y, sun_radius, "images/sun.png")

# mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
# p1_radius = 1516
# p1_x = sun_x + 0.39 * distance_scale
# p1_y = sun_y
# # p1_color = 

while run:
    window.fill((0,0,0))
    sun.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()