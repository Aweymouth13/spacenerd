from manim import *

class ConvergenceVisualization(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],  # x-axis from 0 to 10
            y_range=[0, 2, 0.5],  # y-axis from 0 to 2
            axis_config={"color": BLUE},
        )

        # Create labels for the axes
        x_label = axes.get_x_axis_label("n")
        y_label = axes.get_y_axis_label("Partial Sum")
        
        # Create the graph for the convergence
        graph = axes.plot(lambda x: sum(1 / n**2 for n in range(1, int(x)+1)), color=YELLOW)

        # Create the dot that moves along the graph
        dot = Dot(color=RED)
        self.add(axes, x_label, y_label)

        # Show the graph
        self.play(Create(graph))

        # Initialize the point at (1, 1)
        dot.move_to(axes.c2p(1, 1))
        self.add(dot)

        # Display the convergence process
        n_terms = 10  # Increase number of terms to sum
        partial_sum = 0
        for n in range(1, n_terms + 1):
            term_value = 1 / n**2
            partial_sum += term_value
            
            # Move the dot to the new position
            self.play(dot.animate.move_to(axes.c2p(n, partial_sum)))
            
            # Show the term being added
            term_text = MathTex(f"\\frac{1}{{{n}^2}} = {round(term_value, 4)}").next_to(dot, UP)
            self.play(Write(term_text))

            # Display the running total
            total_text = MathTex(f"Total: {round(partial_sum, 4)}").next_to(term_text, DOWN)
            self.play(Write(total_text))
            self.wait(0.2)  # Shorter pause to speed up animation

            # Clear the term text and total for the next iteration
            self.play(FadeOut(term_text), FadeOut(total_text))

        # Show the final value (which should be pi^2/6)
        final_value = MathTex(r"\frac{\pi^2}{6} \approx " + str(round(partial_sum, 4))).next_to(dot, UP)
        self.play(Write(final_value))
        self.wait(2)

# To run this scene, use:
# manim -ql main.py ConvergenceVisualization --output_file=test_movie.mp4
