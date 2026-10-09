class RectangleRenderer:
    """Responsable du dessin d'un rectangle sur un Canvas"""
    def draw(self, canvas, rectangle, world_to_screen, scale):
        screen_x, screen_y = world_to_screen(rectangle.x, rectangle.y)

        half_width = rectangle.width * scale/2
        half_height = rectangle.height * scale/2

        canvas.create_rectangle(
            screen_x - half_width,
            screen_y - half_height,
            screen_x + half_width,
            screen_y + half_height,
            fill="#a04000",
            width=2,
            tags="body",
        )