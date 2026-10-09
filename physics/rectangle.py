
from physics.body import Body


class Rectangle(Body):
    """Rectangle physique défini par son centre, sa largeur et sa hauteur"""

    def __init__(self, x=0.0, y=0.0, vx=0.0, vy=0.0, ax=0.0, ay=0.0, width=1.0, height=1.0, gravity=9.81):
        
        super().__init__(x=x, y=y, vx=vx, vy=vy, ax=ax, ay=ay, gravity=gravity)

        if width <= 0:
            raise ValueError("La largeur doit être strictement positive.")

        if height <= 0:
            raise ValueError("La hauteur doit être strictement positive.")

        self.width = float(width)
        self.height = float(height)


    def contains_point(self, x, y):
        """Indique si un point du monde se trouve dans le rectangle"""

        if not(-self.width/2 <= x - self.x <= self.width/2):
            return False
        if not(-self.height/2 <= y - self.y <= self.height/2):
            return False
        return True
