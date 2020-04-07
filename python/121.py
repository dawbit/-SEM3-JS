class WH(Random):
    def seed(self, a=None):
        a, x=divmod(a,30269)
        a, y = divmod(a, 30307)
        a, z = divmod(a, 30323)
        self._seed=int(x)+1, int(y)+1, int(z)+1

    def random(self):
        x,y,z=self._seed
        x=(171*x)%30269
        y = (172 * y) % 30307
        z = (170 * z) % 30323
        return (x/30269.0+y/30307.0+z/30323.0)%1.0