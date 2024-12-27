import pygame

width = 1000
height = 800
sun_scale = 0.0004
planets_scale = 0.02
distance_scale = 200
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar system 2d simulation")

class planet:
    def __init__(self, x, y, radius, scale, img):
        self.x = x
        self.y = y
        self.radius = radius * scale
        self.img = pygame.image.load(img)

    def draw(self, window):
        scaled_img = pygame.transform.scale(self.img, (int(self.radius), int(self.radius)))
        window.blit(scaled_img, (int(self.x), int(self.y)))



run = True
sun_radius = 432300
sun_x = width / 2 - (sun_radius * sun_scale)/2
sun_y = height / 2 - (sun_radius * sun_scale)/2
sun = planet(sun_x, sun_y, sun_radius, sun_scale,"images/sun.png")

# mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
p1_radius = 1516
p1_distance = 0.39
p1_x = sun_x + (p1_distance * distance_scale) + (sun_radius * sun_scale)/2
p1_y = sun_y
mercury = planet(p1_x, p1_y, p1_radius, planets_scale, "images/mercury.png")

p2_radius = 3761
p2_distance = 0.72
p2_x = sun_x + (p2_distance * distance_scale) + (sun_radius * sun_scale)/2
p2_y = sun_y
venus = planet(p2_x, p2_y, p2_radius, planets_scale, "images/venus.png")

p3_radius = 3959
p3_distance = 1
p3_x = sun_x + (p3_distance * distance_scale) + (sun_radius * sun_scale)/2
p3_y = sun_y
earth = planet(p3_x, p3_y, p3_radius, planets_scale, "images/earth.png")

p4_radius = 2106
p4_distance = 1.52
p4_x = sun_x + (p4_distance * distance_scale) + (sun_radius * sun_scale)/2
p4_y = sun_y
mars = planet(p4_x, p4_y, p4_radius, planets_scale, "images/mars.png")

p5_radius = 43441
p5_distance = 5.2
p5_x = sun_x + (p5_distance * distance_scale) + (sun_radius * sun_scale)/2
p5_y = sun_y
jupiter = planet(p5_x, p5_y, p5_radius, planets_scale, "images/jupiter.png")

p6_radius = 36184
p6_distance = 9.58
p6_x = sun_x + (p6_distance * distance_scale) + (sun_radius * sun_scale)/2
p6_y = sun_y
saturn = planet(p6_x, p6_y, p6_radius, planets_scale, "images/saturn.png")

p7_radius = 15759
p7_distance = 19.22
p7_x = sun_x + (p7_distance * distance_scale) + (sun_radius * sun_scale)/2
p7_y = sun_y
uranus = planet(p7_x, p7_y, p7_radius, planets_scale, "images/uranus.png")

p8_radius = 15299
p8_distance = 30.05
p8_x = sun_x + (p8_distance * distance_scale) + (sun_radius * sun_scale)/2
p8_y = sun_y
neptune = planet(p8_x, p8_y, p8_radius, planets_scale, "images/neptune.png")

while run:
    window.fill((0,0,0))
    pygame.draw.line(window, (255,255,255), (width/2, 0), (width/2, height), 5) 
    pygame.draw.line(window, (255,255,255), (0, height/2), (width, height/2), 5)
    sun.draw(window)
    mercury.draw(window)
    venus.draw(window)
    earth.draw(window)
    mars.draw(window)
    jupiter.draw(window)
    saturn.draw(window)
    uranus.draw(window)
    neptune.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()