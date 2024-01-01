import tkinter as tk

class TrackerVar:
    def __init__(self):
        self.x = tk.DoubleVar()
        self.y = tk.DoubleVar()
        self.z = tk.DoubleVar()
        self.euler_x = tk.DoubleVar()
        self.euler_y = tk.DoubleVar()
        self.euler_z = tk.DoubleVar()
        self.position_components = [ self.x, self.y, self.z ]
        self.rotation_components = [ self.euler_x, self.euler_y, self.euler_z ]

    def get_position(self):
        return (self.x.get(), self.y.get(), self.z.get())
    
    def get_euler_angles(self):
        return (self.euler_x.get(), self.euler_y.get(), self.euler_z.get())
    
    def register_position_update_listener(self, listener):
        self.x.trace_add("write", listener)
        self.y.trace_add("write", listener)
        self.z.trace_add("write", listener)

    def register_rotation_update_listener(self, listener):
        self.euler_x.trace_add("write", listener)
        self.euler_y.trace_add("write", listener)
        self.euler_z.trace_add("write", listener)


class TrackerParams:
    trackers = [
            "Hip",
            "Chest",
            "Left foot",
            "Right foot",
            "Left knee",
            "Right knee",
            "Left elbow",
            "Right elbow",
            "Head"
        ]

    def __init__(self):
        self.tracker_vars = []
        for _ in self.trackers:
            tracker_var = TrackerVar()
            self.tracker_vars.append(tracker_var)