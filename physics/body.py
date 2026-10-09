class Body:
    """Objet physique de base dans un monde 2D
    
    Les distances sont exprimées en mètres et le temps en secondes.
    L'axe x pointe vers la droite et l'axe y vers le haut.
    """

    def __init__(self, x=0.0, y=0.0, vx=0.0, vy=0.0, ax=0.0, ay = 0.0, gravity=9.81, restitution=0.8, mass=1.0):
        self.x = float(x)
        self.y = float(y)

        self.vx = float(vx)
        self.vy = float(vy)

        self.ax = float(ax)
        self.ay = float(ay)

        self.gravity = float(gravity)
        self.restitution = float(restitution)

        self.mass = float(mass)


    def update(self, dt):
        if dt <= 0:
            raise ValueError("dt doit être strictement positif")

        acceleration_x = self.ax
        acceleration_y = self.ay - self.gravity

        self.x += self.vx * dt + 0.5 * acceleration_x * dt**2 # x(t) = x + vx*t + ax*t/2
        self.y += self.vy * dt + 0.5 * acceleration_y * dt**2 # y(t) = y + vy*t + ay*t/2

        self.vx += acceleration_x * dt
        self.vy += acceleration_y * dt


    def reset(self, x=0.0, y=0.0, vx=0.0, vy=0.0):
        """Réinitailise la position et la vitesse"""

        self.x = float(x)
        self.y = float(y)
        self.vx = float(vx)
        self.vy = float(vy)


    def __str__(self):
        return(
            f"{self.__class__.__name__}("
            f"x={self.x:.2f}, y={self.y:.2f}, "
            f"vx={self.vx:.2f}, vy={self.vy:.2f})"
        )