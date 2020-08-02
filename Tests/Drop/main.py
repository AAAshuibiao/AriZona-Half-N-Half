from matplotlib.pyplot import plot, show


class Trace(object):
    def __init__(self):
        self.x = []
        self.y = []
    
    def append_point(self, x, y):
        self.x.append(x)
        self.y.append(y)


class Physics(object):
    def __init__(self):
        self.x = 0
        self.y = 50
        self.vx = 10
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.t = 1 / 1000
        self.k = 1 / 10
        self.trace = Trace()

    def update_acceleration(self):
        self.ax = 0
        self.ay = -9.8
        self.ax -= self.vx * self.k
        self.ay -= self.vy * self.k

    def update_velocity(self):
        self.vx += self.ax * self.t
        self.vy += self.ay * self.t

    def update_position(self):
        self.x += self.vx * self.t
        self.y += self.vy * self.t

    def run(self):
        while(self.y > 0):
            self.trace.append_point(self.x, self.y)
            self.update_acceleration()
            self.update_velocity()
            self.update_position()


test1 = Physics()
test1.run()

print("landing point: " + str(test1.trace.x[-1]))

plot(test1.trace.x, test1.trace.y)
show()
input()
