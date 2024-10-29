from manim import *

class TestScene(Scene):
    def construct(self):
        # Create a circle
        circle = Circle()

        # Set the color and stroke width of the circle
        circle.set_stroke(color=BLUE, width=6)

        # Animate the creation of the circle
        self.play(Create(circle))

        # Add a pause at the end
        self.wait(2)
