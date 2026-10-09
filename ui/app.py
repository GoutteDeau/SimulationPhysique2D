import tkinter as tk

from physics.ball import Ball
from physics.rectangle import Rectangle

from physics.world import PhysicsWorld

from ui.renderer import CanvasRenderer
from ui.renderers.ball_renderer import BallRenderer
from ui.renderers.rectangle_renderer import RectangleRenderer


class SimulationApp:
    """Interface graphique de la simulation physique"""
    def __init__(self):
        self.running = False
        self.dt = 0.02
        self.after_id = None

        self.root = tk.Tk()
        self.root.title("Simulation physique 2D")
        self.root.geometry("900x600")
        self.root.minsize(500, 350)

        self.world = PhysicsWorld()
        self.ball = Ball(x=0, y=5, vx=1, vy=0, radius=0.4)
        self.rectangle = Rectangle(x=2, y=2, vx=-0.5, vy=0, width=1.5, height=0.8)
        self.world.add_body(self.ball)
        self.world.add_body(self.rectangle)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.main_frame, bg="#7a7979", highlightthickness=0)
        self.canvas.pack(side="right", fill="both", expand=True)

        self.properties_frame = tk.Frame(self.main_frame, width=260, padx=12, pady=12, bg="#555555")
        self.properties_frame.pack(side="left", fill="y")
        self.properties_frame.pack_propagate(False)

        self.renderer = CanvasRenderer(self.canvas, scale=50)
        self.renderer.register_renderer(Ball, BallRenderer())
        self.renderer.register_renderer(Rectangle, RectangleRenderer())

        self.selected_body = None
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        controls = tk.Frame(self.root)
        controls.pack(fill="x", padx=10, pady=10)

        self.start_button = tk.Button(controls, text="Démarrer", command=self.toggle_simulation)
        self.start_button.pack(side="left", padx=5)

        reset_button = tk.Button(controls, text="Réinitialiser", command=self.reset_simulation)
        reset_button.pack(side="left", padx=5)

        self.root.after(100, self.draw)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw(self):
        """Met à jour l'affichage"""
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        self.world.width = canvas_width/self.renderer.scale
        self.world.height = (canvas_height - self.renderer.ground_margin)/self.renderer.scale

        self.renderer.draw_world(self.world)

    def toggle_simulation(self):
        """Démarre ou met en pause la simulation."""
        self.running = not self.running

        if self.running:
            self.start_button.config(text="Pause")
            self.animate()
        else:
            self.start_button.config(text="Démarrer")

            if self.after_id is not None:
                self.root.after_cancel(self.after_id)
                self.after_id = None

    def animate(self):
        """Effectue un pas physique puis programme le suivant"""
        if not self.running:
            return

        self.world.step(self.dt)
        self.draw()
        self.update_properties()

        self.after_id = self.root.after(20, self.animate)


    def on_canvas_click(self, event):
        """Selectionne un objet avec la souris"""
        world_x, world_y = self.renderer.screen_to_world(event.x, event.y)
        self.selected_body = None

        for body in reversed(self.world.bodies):
            if body.contains_point(world_x, world_y):
                self.selected_body = body
                break

        self.show_properties(self.selected_body)

    
    def show_properties(self, body):
        """Affiche les propriétés de l'objet séléctionner"""
        for widget in self.properties_frame.winfo_children():
            widget.destroy()

        self.property_entries = {}

        tk.Label(self.properties_frame, text="PROPRIÉTÉS", font=("Arial", 14, "bold"), bg="#eeeeee").pack(anchor="w", pady=(0, 12))

        if body is None:
            tk.Label(self.properties_frame, text="Sélectionne un objet", bg="#eeeeee").pack(anchor="w")
            return

        tk.Label(self.properties_frame, text=body.__class__.__name__, font=("Arial", 12, "bold"), bg="#eeeeee").pack(anchor="w", pady=(0, 8))

        properties = [
            ("Position X", "x"),
            ("Position Y", "y"),
            ("Vitesse X", "vx"),
            ("Vitesse Y", "vy"),
            ("Gravité", "gravity"),
            ("Restitution", "restitution")
        ]

        if isinstance(body, Ball):
            properties.extend([
                ("Rayon", "radius")
            ])
        elif isinstance(body, Rectangle):
            properties.extend([
                ("Largeur", "width"),
                ("Hauteur", "height")
            ])

        for label_text, attribute in properties:
            row = tk.Frame(self.properties_frame, bg="#eeeeee")
            row.pack(fill="x", pady=3)

            tk.Label(row, text=label_text, bg="#eeeeee", width=11, anchor="w").pack(side="left")

            entry = tk.Entry(row, width=10)
            entry.insert(0, str(getattr(body, attribute)))
            entry.pack(side="right", fill="x", expand=True)

            self.property_entries[attribute] = entry

        tk.Button(self.properties_frame, text="Appliquer", command=lambda: self.apply_properties(body)).pack(fill="x", pady=(12, 0))


    def apply_properties(self, body):
        """Applique les nouvelles propriétés saisie dans le paneau de configuration"""
        try:
            values = {
                name: float(entry.get())
                for name, entry in self.property_entries.items()
            }

            if isinstance(body, Ball):
                if values["radius"] <= 0:
                    raise ValueError("Le rayon doit être strictement positif")
                if not 0 <= values["restitution"] <= 1:
                    raise ValueError("La restitution doit être comprise entre 0 et 1")
                if values["y"] < values["radius"]:
                    raise ValueError("La balle ne peut pas commencer sous le sol")

            elif isinstance(body, Rectangle):
                if values["width"] <= 0 or values["height"] <= 0:
                    raise ValueError("La largeur et la hauteur doivent être positives")

            for name, value in values.items():
                setattr(body, name, value)

            self.show_properties(body)
            self.draw()

        except ValueError as error:
            from tkinter import messagebox
            messagebox.showerror("Valeur invalide", str(error), parent=self.root)


    def update_properties(self):
        """Actualise en temps réel les propriéter de l'objet selectionné"""
        if self.selected_body is None:
            return

        body = self.selected_body

        values = {
            "x": body.x,
            "y": body.y,
            "vx": body.vx,
            "vy": body.vy,
            "gravity": body.gravity,
            "restitution": body.restitution
        }

        if isinstance(body, Ball):
            values.update({
                "radius": body.radius
            })
        elif isinstance(body, Rectangle):
            values.update({
                "width": body.width,
                "height": body.height
            })

        for name, value in values.items():
            entry = self.property_entries.get(name)

            if entry is not None:
                entry.delete(0, tk.END)
                entry.insert(0, f"{value:.2f}")


    def reset_simulation(self):
        """Remet la simulation dans son état initial"""
        self.running = False

        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.start_button.config(text="Démarrer")

        self.ball.reset(x=0, y=5, vx=1, vy=0)
        self.rectangle.reset(x=2, y=2, vx=-0.5, vy=0)

        self.world.reset_time()
        self.draw()
        self.update_properties()


    def close(self):
        """Ferme proprement la fenêtre"""
        self.running = False

        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.root.destroy()

    def run(self):
        """Lance la boucle d'événements Tkinter"""
        self.root.mainloop()