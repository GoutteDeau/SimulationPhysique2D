class BallRenderer:
    """Responsable du dessin d'une balle sur un Canvas"""
    def draw(self, canvas, ball, world_to_screen, scale):
        screen_x, screen_y = world_to_screen(ball.x, ball.y)
        radius_pixels = ball.radius*scale

        canvas.create_oval(
            screen_x - radius_pixels,
            screen_y - radius_pixels,
            screen_x + radius_pixels,
            screen_y + radius_pixels,
            fill="#8A2BE2",
            width=2,
            tags="body",
        )