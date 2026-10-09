from physics.body import Body

class Ball(Body):
    """Représente une balle dans un monde physique en 2D"""

    def __init__(self, x=0.0, y=0.0, vx=0.0, vy=0.0, ax=0.0, ay=0.0, radius=0.3, gravity=9.81, restitution=0.8):
        super().__init__(x=x, y=y, vx=vx, vy=vy, ax=ax, ay=ay, gravity=gravity)

        if radius <= 0:
            raise ValueError("Le rayon doit être strictement positif")

        if not 0 <= restitution <= 1:
            # Restitution de la vitesse au rebond (comprise entre 0 et 1)
            raise ValueError("La restitution doit être comprise entre 0 et 1.")

        self.radius = float(radius)
        self.restitution = float(restitution)


    def contains_point(self, x, y):
        """Indique si un point du monde se trouve dans la balle"""

        dx = x - self.x
        dy = y - self.y

        return dx**2 + dy**2 <= self.radius**2
