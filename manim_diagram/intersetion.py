from manim import *

# class ManualIntersection(Scene):
#     def construct(self):
#         # Create shapes
#         square = Square(side_length=2, color=BLUE, fill_opacity=0.5).shift(LEFT)
#         circle = Circle(radius=1, color=RED, fill_opacity=0.5).shift(RIGHT)

#         # Position the shapes to overlap partially
#         square.move_to(LEFT * 0.5)
#         circle.move_to(RIGHT * 0.5)

#         # Add the shapes to the scene
#         self.add(square, circle)
#         self.wait(1)

#                 # Manually create an intersection area
#         intersection_shape = Arc(radius=1, angle= PI, color=GREEN, fill_opacity=1).rotate(PI/2)
#         intersection_shape.move_to(circle, LEFT)

#         # Add the intersection shape to the scene
#         self.add(intersection_shape)
#         self.wait(1)

from manim import *

class IntersectionExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1)
        sq.move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1)
        cr.move_to([-1.3, 0.7, 0])
        un = Intersection(sq, cr, color=GREEN, fill_opacity=1)
        un.move_to([1.5, 0, 0])
        self.add(sq, cr, un)