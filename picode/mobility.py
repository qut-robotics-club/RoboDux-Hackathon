import turtle
# import serial

class Mobility():
    def __init__(self):
        self.pendown = True
        self.targetPos = []

        self.window = turtle.Screen()
        self.window.bgcolor("blue")
        self.window.setup(width=1000, height=800)
        self.window.title("Preview")
        self.window.listen()

        self.character = turtle.Turtle()
        self.character.shape("turtle")
        self.character.penup()
        self.character.goto(0, 0)
        self.character.speed(1)

    def arrived(self) -> bool:
        print(f"Arrived at x: {self.targetPos[0]} y: {self.targetPos[1]} pendown: {self.pendown}")
        return True

    def goto(self, pos):
        self.targetPos = pos
        self.pendown = self.targetPos[2]
        print(f"Going to x: {self.targetPos[0]} y: {self.targetPos[1]} pendown: {self.pendown}")
        if self.pendown:
            self.character.pendown()
        else:
            self.character.penup()
        self.character.goto(pos[0] - 500, -pos[1] + 400)