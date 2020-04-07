class Circle(object):
    def __init__(self,x0,y0,r):
        self.x0, self.y0, self.r = x0, y0, r
    def area(self):
        return 3.14*self.r**2
    def cir(self):
        return 2*3.14*self.r