class Cargo:
    def __init__(self, weight):
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None):
        self.name = name
        self.weight = weight
        self.coords = coords
        if self.coords is None:
            self.coords = [0, 0]

    def go_forward(self, distance=1):
        self.coords[1] += distance

    def go_back(self, distance=1):
        self.coords[1] -= distance

    def go_right(self, distance=1):
        self.coords[0] += distance

    def go_left(self, distance=1):
        self.coords[0] -= distance

    def get_info(self):
        return f'Robot: {self.name}, Weight: {self.weight}'


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None):
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, distance=1):
        self.coords[2] += distance

    def go_down(self, distance=1):
        self.coords[2] -= distance


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: int,
            coords: list = None
    ):
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo):
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self):
        self.current_load = None
