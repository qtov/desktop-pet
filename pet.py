import tkinter as tk
import time


class pet:
    speedUpMultiplier = 5
    direction = -2
    size = 170

    def speedUp(self, e):
        if e.x < 70:
            self.direction = abs(self.direction) * self.speedUpMultiplier
            return
        self.direction = abs(self.direction) * -self.speedUpMultiplier

    def slowDown(self, e):
        self.direction //= self.speedUpMultiplier

    def generateGifs(self):
        # code below generates string for each frame in gif
        # Don't do this kids, never do this.
        # But in life sometimes you do things you should not do.
        # Like putting emoji in code 🙏
        self.frame_index = 0  # setting starting frame
        self.moveleft = [
            tk.PhotoImage(
                file='duck-left.gif',
                format=f'gif -index {i}'
            ).zoom(4).subsample(3)
            for i in range(10)]
        self.moveright = [
            tk.PhotoImage(
                file='duck-right.gif',
                format=f'gif -index {i}'
            ).zoom(4).subsample(3)
            for i in range(10)]
        self.img = self.moveleft[self.frame_index]  # starting direction gif

    def setupWindow(self):
        self.window = tk.Tk()
        self.window.config(background='black')
        self.window.wm_attributes('-transparentcolor', 'black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.geometry(f'{self.size}x{self.size}+{self.x}+{self.y}')
        self.window.after(0, self.update)

    def createLabel(self):
        self.label = tk.Label(self.window, bd=0, bg='black')
        self.label.configure(image=self.img)
        self.label.pack()
        self.label.bind("<Enter>", self.speedUp)
        self.label.bind("<Leave>", self.slowDown)

    def __init__(self):
        self.x = 1040
        self.y = 940
        self.setupWindow()
        self.generateGifs()

        self.timestamp = time.time()
        self.createLabel()
        self.window.mainloop()

    def changetime(self, direction):
        if time.time() <= self.timestamp + 0.05:
            return
        self.timestamp = time.time()
        self.frame_index = (self.frame_index + 1) % 8  # speed of frames change
        self.img = direction[self.frame_index]

    def go(self):
        self.x = self.x + self.direction
        if self.direction < 0:
            direction = self.moveleft
        else:
            direction = self.moveright
        self.changetime(direction)

    def update(self):
        self.go()
        if self.x < 0:
            self.direction = abs(self.direction)
        elif self.x > 1800:
            self.direction = -abs(self.direction)

        self.window.geometry(f'{self.size}x{self.size}+{self.x}+{self.y}')
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(10, self.update)  # 10 is frames number for my gif
        self.window.lift()


if __name__ == '__main__':
    pet()
