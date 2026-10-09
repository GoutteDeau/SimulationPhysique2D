from physics.body import Body
from physics.ball import Ball
from physics.rectangle import Rectangle


class PhysicsWorld:
    """Gère les objets physique et le temps de simulation"""
    def __init__(self, width=10.0, height=7.0):
        self.bodies = []
        self.time = 0.0
        self.width = float(width)
        self.height = float(height)


    def add_body(self, body):
        """Ajoute un objet au monde"""
        if not isinstance(body, Body):
            raise TypeError("L'objet doit hériter de Body")

        if body in self.bodies:
            raise ValueError("Cet objet est déjà dans le monde")

        self.bodies.append(body)


    def remove_body(self, body):
        """Retir un objet du monde"""
        if body not in self.bodies:
            raise ValueError("Cet objet n'est pas dans le monde")

        self.bodies.remove(body)

    def step(self, dt):
        """Fait avancer tous les objet de dt secondes"""
        if dt <= 0:
            raise ValueError("dt doit être strictement positif")

        for body in self.bodies:
            body.update(dt)

        # Détecter et résoudre les collisions entre objets
        for i, body_a in enumerate(self.bodies):
            for body_b in self.bodies[i + 1:]:
                if isinstance(body_a, Ball) and isinstance(body_b, Rectangle):
                    self.resolve_ball_rectangle_collision(body_a, body_b)

                elif isinstance(body_a, Rectangle) and isinstance(body_b, Ball):
                    self.resolve_ball_rectangle_collision(body_b, body_a)

        self.handle_wall_collisions()
        self.time += dt

    def reset_time(self):
        """Remet l'horloge de simulation à 0"""
        self.time = 0.0


    def handle_wall_collisions(self):
        """Gère la colision avec les bords de la fenêtre"""
        for body in self.bodies:
            if hasattr(body, "radius"):
                half_width = body.radius
                half_height = body.radius
            elif hasattr(body, "width") and hasattr(body, "height"):
                half_width = body.width / 2
                half_height = body.height / 2
            else:
                continue
            
            # Mur gauche
            left_limit = -self.width / 2
            if body.x - half_width < left_limit:
                body.x = left_limit + half_width
                if body.vx < 0:
                    body.vx = -body.vx * body.restitution

            # Mur droit
            right_limit = self.width / 2
            if body.x + half_width > right_limit:
                body.x = right_limit - half_width
                if body.vx > 0:
                    body.vx = -body.vx * body.restitution

            # Sol
            if body.y - half_height < 0:
                body.y = half_height
                if body.vy < 0:
                    body.vy = -body.vy * body.restitution

            # Plafond
            if body.y + half_height > self.height:
                body.y = self.height - half_height
                if body.vy > 0:
                    body.vy = -body.vy * body.restitution


    def check_rectangle_collision(self, rect1, rect2):
        """Vérifie si 2 rectangles sont en collisions"""
        left1 = rect1.x - rect1.width/2
        right1 = rect1.x + rect1.width/2
        bottom1 = rect1.y - rect1.height/2
        top1 = rect1.y + rect1.height/2

        left2 = rect2.x - rect2.width/2
        right2 = rect2.x + rect2.width/2
        bottom2 = rect2.y - rect2.height/2
        top2 = rect2.y + rect2.height/2

        if right1 < left2 or left1 > right2:
            return False
        if top1 < bottom2 or bottom1 > top2:
            return False
        return True


    def check_ball_rectangle_collision(self, ball, rect):
        """Vérifie si 1 rectangle et 1 balle sont en collisions"""
        closest_x = max(rect.x - rect.width/2, min(ball.x, rect.x + rect.width/2))
        closest_y = max(rect.y - rect.height/2, min(ball.y, rect.y + rect.height/2))

        dx = ball.x - closest_x
        dy = ball.y - closest_y

        return dx**2 + dy**2 <= ball.radius**2


    def resolve_ball_rectangle_collision(self, ball, rect):
        if not self.check_ball_rectangle_collision(ball, rect):
            return

        closest_x = max(rect.x - rect.width/2, min(ball.x, rect.x + rect.width/2))
        closest_y = max(rect.y - rect.height/2, min(ball.y, rect.y + rect.height/2))

        dx = ball.x - closest_x
        dy = ball.y - closest_y

        # Déterminer la normale de collision
        if abs(dx) > abs(dy):
            normal = (1.0, 0.0) if dx >= 0 else (-1.0, 0.0)
            penetration = ball.radius - abs(dx)
        else:
            normal = (0.0, 1.0) if dy >= 0 else (0.0, -1.0)
            penetration = ball.radius - abs(dy)

        if penetration > 0:
            ball.x += normal[0] * penetration
            ball.y += normal[1] * penetration

        self.apply_collision_impulse(ball, rect, (-normal[0], -normal[1]), restitution=0.8)


    def apply_collision_impulse(self, body_a, body_b, normal, restitution=0.8):
        relative_vx = body_b.vx - body_a.vx
        relative_vy = body_b.vy - body_a.vy

        relative_speed = (relative_vx*normal[0] + relative_vy*normal[1])

        if relative_speed >= 0:
            return

        inverse_mass_a = 1/body_a.mass
        inverse_mass_b = 1/body_b.mass

        impulse = (-(1 + restitution)*relative_speed/(inverse_mass_a + inverse_mass_b))

        body_a.vx -= impulse * inverse_mass_a * normal[0]
        body_a.vy -= impulse * inverse_mass_a * normal[1]

        body_b.vx += impulse * inverse_mass_b * normal[0]
        body_b.vy += impulse * inverse_mass_b * normal[1]
