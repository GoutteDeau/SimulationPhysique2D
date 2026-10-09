from physics.ball import Ball
from physics.rectangle import Rectangle

from ui.renderers.ball_renderer import BallRenderer
from ui.renderers.rectangle_renderer import RectangleRenderer


class CanvasRenderer:
    """Dessine les objets physiques sur un Canvas Tkinter"""
    def __init__(self, canvas, scale=50, ground_margin=40):
        self.canvas = canvas
        self.scale = scale
        self.ground_margin = ground_margin

        self.renderers = {}


    def world_to_screen(self, x, y):
        """Convertit les coordonnées du monde en coordonnées écran"""
        width = max(self.canvas.winfo_width(), 1)
        height = max(self.canvas.winfo_height(), 1)

        screen_x = width/2 + x*self.scale
        screen_y = height - self.ground_margin - y*self.scale

        return screen_x, screen_y


    def screen_to_world(self, screen_x, screen_y):
        """Convertit les coordonnées écran en coordonnées du monde"""

        width = max(self.canvas.winfo_width(), 1)
        height = max(self.canvas.winfo_height(), 1)

        world_x = (screen_x - width/2)/self.scale
        world_y = (height - self.ground_margin - screen_y)/self.scale

        return world_x, world_y


    def register_renderer(self, body_type, renderer):
        """Associe un type d'objet à son renderer"""
        self.renderers[body_type] = renderer


    def draw_world(self, world):
        """Efface l'image précédente et dessine les objets du monde"""
        self.canvas.delete("all")

        width = max(self.canvas.winfo_width(), 1)
        height = max(self.canvas.winfo_height(), 1)
        ground_y = height - self.ground_margin

        # Dessine le sol
        self.canvas.create_line(
            0,
            ground_y,
            width,
            ground_y,
            fill="#292929",
            width=2,
            tags="ground",
        )

        for body in world.bodies:
            renderer = self.renderers.get(type(body))

            if renderer is None:
                continue

            renderer.draw(self.canvas, body, self.world_to_screen, self.scale)
