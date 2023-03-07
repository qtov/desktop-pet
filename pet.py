import tkinter as tk
import time


class Pet:
    screen_width = 1920
    screen_height = 1080
    taskbar_height = 30
    speed_up_multiplier = 5
    direction = -2
    # Hardcoded cause I don't care anymore at 1AM tonight, yup.
    size = 170

    def speed_up(self, e):
        if e.x < 70:
            self.direction = abs(self.direction) * self.speed_up_multiplier
            return
        self.direction = abs(self.direction) * -self.speed_up_multiplier

    def slow_down(self, e):
        self.direction //= self.speed_up_multiplier

    def generate_gifs(self):
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

    def setup_window(self):
        self.window = tk.Tk()
        self.window.config(background='black')
        self.window.wm_attributes('-transparentcolor', 'black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.geometry(f'{self.size}x{self.size}+{self.x}+{self.y}')
        self.window.after(0, self.update)

    def create_label(self):
        self.label = tk.Label(self.window, bd=0, bg='black')
        self.label.configure(image=self.img)
        self.label.pack()
        self.label.bind("<Enter>", self.speed_up)
        self.label.bind("<Leave>", self.slow_down)

    def __init__(self):
        self.x = 1040  # artitrary number
        self.y = self.screen_height - self.size  # above taskbar on a 1080p monitor
        self.setup_window()
        self.generate_gifs()
        self.create_label()

    def change_time(self, direction):
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
        self.change_time(direction)

    def update(self):
        self.go()
        if self.x < -self.size:
            self.direction = abs(self.direction)
        elif self.x > self.screen_width:
            self.direction = -abs(self.direction)

        self.window.geometry(f'{self.size}x{self.size}+{self.x}+{self.y}')
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(10, self.update)  # 10 is frames number for my gif
        self.window.lift()

    def run(self):
        self.timestamp = time.time()
        self.window.mainloop()


if __name__ == '__main__':
    pet = Pet()
    pet.run()
