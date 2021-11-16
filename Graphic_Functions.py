import pygame.math
import math

from Robot_Pieces import *
from Screens import *


def draw_robot(base, head, arms, legs, weapon=None, stance="neutral", stance_sequence=0, placement=(500,500)):
    right_arm = arms.right_arm
    left_arm = arms.left_arm
    right_leg = legs.right_leg
    left_leg = legs.left_leg

    if weapon != None:
        pass
    if stance == "neutral":
        head_socket = base.connection_points["head"]
        right_arm_socket = base.connection_points["right_arm"]
        left_arm_socket = base.connection_points["left_arm"]
        right_leg_socket = base.connection_points["right_leg"]
        left_leg_socket = base.connection_points["left_leg"]

        middle_layer.blit(left_arm.img, (placement[0] + left_arm_socket[0] - left_arm.connection_point[0], placement[1] + left_arm_socket[1] - left_arm.connection_point[1]))
        robot_base = middle_layer.blit(base.img, placement)
        middle_layer.blit(head.img, (placement[0] + head_socket[0] - head.img.get_width()//2, placement[1] - head_socket[1]))
        middle_layer.blit(right_arm.img, (placement[0] + right_arm_socket[0] - right_arm.connection_point[0], placement[1] + right_arm_socket[1] - right_arm.connection_point[1]))
        middle_layer.blit(right_leg.img, (placement[0] + right_leg_socket[0] - right_leg.connection_point[0], placement[1] + right_leg_socket[1] - right_leg.connection_point[1]))
        middle_layer.blit(left_leg.img, (placement[0] + left_leg_socket[0] - left_leg.connection_point[0], placement[1] + left_leg_socket[1] - left_leg.connection_point[1]))
    elif stance == "terrible walking animation":
        head_socket = base.connection_points["head"]
        right_arm_socket = base.connection_points["right_arm"]
        left_arm_socket = base.connection_points["left_arm"]
        right_leg_socket = base.connection_points["right_leg"]
        left_leg_socket = base.connection_points["left_leg"]

        middle_layer.blit(left_arm.img, (placement[0] + left_arm_socket[0] - left_arm.connection_point[0], placement[1] + left_arm_socket[1] - left_arm.connection_point[1]))
        robot_base = middle_layer.blit(pygame.transform.rotate(base.img, (1 * stance_sequence) - ((stance_sequence//9)* ((stance_sequence-9)*2))), placement)
        middle_layer.blit(head.img, (placement[0] + head_socket[0] - head.img.get_width()//2, placement[1] - head_socket[1]))
        if stance_sequence >= 9:
            middle_layer.blit(pygame.transform.rotate(right_leg.img, stance_sequence *2 ), (placement[0] + right_leg_socket[0] + (robot_base.width - base.original_width) - right_leg.connection_point[0], placement[1] + right_leg_socket[1] - (robot_base.height - base.original_height) - right_leg.connection_point[1]))
            middle_layer.blit(pygame.transform.rotate(left_leg.img, (3 * stance_sequence) - ((stance_sequence//9)* ((stance_sequence-9)*6))), (placement[0] + left_leg_socket[0] + (robot_base.width - base.original_width) - left_leg.connection_point[0], placement[1] + left_leg_socket[1] - (robot_base.height - base.original_height) - left_leg.connection_point[1]))
            middle_layer.blit(pygame.transform.rotate(right_arm.img, (7 * stance_sequence) - ((stance_sequence//9)* ((stance_sequence-9)*14))), (placement[0] + right_arm_socket[0] + (robot_base.width - base.original_width) - right_arm.connection_point[0], placement[1] + right_arm_socket[1] + (robot_base.height - base.original_height) - right_arm.connection_point[1]))
        else:
            middle_layer.blit(pygame.transform.rotate(left_leg.img, (3 * stance_sequence) - ((stance_sequence//9)* ((stance_sequence-9)*6))), (placement[0] + left_leg_socket[0] + (robot_base.width - base.original_width) - left_leg.connection_point[0], placement[1] + left_leg_socket[1] - (robot_base.height - base.original_height) - left_leg.connection_point[1]))
            middle_layer.blit(pygame.transform.rotate(right_leg.img, 18 - ((stance_sequence-9)*2)), (placement[0] + right_leg_socket[0] + (robot_base.width - base.original_width) - right_leg.connection_point[0], placement[1] + right_leg_socket[1] - (robot_base.height - base.original_height) - right_leg.connection_point[1]))
            middle_layer.blit(pygame.transform.rotate(right_arm.img, (7 * stance_sequence) - ((stance_sequence//9)* ((stance_sequence-9)*14))), (placement[0] + right_arm_socket[0] + (robot_base.width - base.original_width) - right_arm.connection_point[0], placement[1] + right_arm_socket[1] + (robot_base.height - base.original_height) - right_arm.connection_point[1]))

        print("width: " +str(robot_base.width), ", height: " + str(robot_base.width))
