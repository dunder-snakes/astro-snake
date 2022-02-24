import pytest
from game.constants import *
# from game.game import Game

def test_display_x():
    assert DISPLAY_X == 600

def test_display_y():
    assert DISPLAY_Y == 600

def test_frames_per_second():
    assert FPS == 60

def test_distance():
    assert SNAKE_SPEED == 5

def test_points():
    assert POINTS == 1000



