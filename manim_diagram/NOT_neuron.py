from manim import *

class NotGateDiagram(Scene):
    def construct(self):
        # Create the NOT gate symbol
        triangle = Polygon(
            ORIGIN, 
            UP, 
            DOWN, 
            fill_opacity=0, 
            color=RED
        ).scale(2).shift(LEFT*0.5)

        # Add the circle for the NOT gate
        circle = Circle(radius=0.2, color=RED).shift(RIGHT*1.5)

        # Add the input and output lines
        input_line = Line(LEFT*3, LEFT*1.5, color=WHITE)
        output_line = Line(RIGHT*1.7, RIGHT*3, color=WHITE)

        # Create the input and output labels
        input_label = MathTex("x").next_to(input_line, DOWN, buff=0.2)
        output_label = MathTex("\\hat{y}").next_to(output_line, DOWN, buff=0.2)

        # Group the NOT gate components
        not_gate = VGroup(triangle, circle)

        # Animate the components
        self.play(Create(input_line), Create(output_line))
        self.play(Create(not_gate))
        self.play(Write(input_label), Write(output_label))

        # Keep the final scene
        self.wait()

if __name__ == "__main__":
    from manim import config, tempconfig
    config.quality = "low_quality"
    config.output_file = "not_gate_diagram"
    config.save_last_frame = False
    config.write_all = False
    
    from manim import __main__, config
    from manim.utils.file_ops import open_file
    
    script_name = __file__
    command_line = f"manim {script_name} NotGateDiagram -pql"
    os.system(command_line)