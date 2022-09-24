

class Mobility():
    def __init__(self):
        self.pendown = True
        self.targetPos = []

    def arrived(self) -> bool:
        print(f"Arrived at x: {self.targetPos[1]} y: {self.targetPos[2]} pendown: {self.pendown}")
        return True

    def goto(self, pos):
        self.pendown = self.targetPos[3]
        print(f"Going to x: {self.targetPos[1]} y: {self.targetPos[2]} pendown: {self.pendown}")