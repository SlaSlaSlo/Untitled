import pygame

# Generic class names that should be changed later

class base_1():
    img = pygame.image.load(r"Assets/Base1.png")

    # Connection points are where the specified pieces will be blitted and are create by manually finding what coordinate of the base
    # looks like a good spot to place the specified piece.
    connection_points = {"head": (32, 22), "right_arm": (8, 38), "left_arm": (47, 34), "right_leg": (20, 68), "left_leg": (40, 70)}
    original_height = img.get_height()
    original_width = img.get_width()
    # If hooded is true, then arms will be drawn beneath the robot's base. If false, arms will be drawn on top
    hooded_arms = True


class head_1():
    img = pygame.image.load(r"Assets/Head1.png")
    connection_socket = ()

#Armsets feature two arms, and later the two arms may have a set of images (or angles if they'll be animated through rotation) to animate them. Likewise for the legset.
class armset_1():
    class right_arm():
        img = pygame.image.load(r"Assets/Armset1_Right_Arm.png")
        connection_point = (31, 5)
    class left_arm():
        img = pygame.image.load(r"Assets/Armset1_Left_Arm.png")
        connection_point = (4, 9)

class legset_1():
    class right_leg():
        img = pygame.image.load(r"Assets/Legset1_Right_Leg.png")
        connection_point = (21, 9)
    class left_leg():
        img = pygame.image.load(r"Assets/Legset1_Left_Leg.png")
        connection_point = (5, 9)