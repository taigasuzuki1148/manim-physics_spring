from manim import *
from manim_physics import *
config.background_color = WHITE

class PendulumExample(SpaceScene):
    def construct(self):
        pends = VGroup(*[Pendulum(i) for i in np.linspace(1, 5, 7)])
        self.add(pends)
        for p in pends:
            self.make_rigid_body(p.bobs)
            p.start_swinging()
        self.wait(10)


class MultiPendulumExample(SpaceScene):
    def construct(self):
        p = MultiPendulum(RIGHT, LEFT)
        self.add(p)
        self.make_rigid_body(p.bobs)
        p.start_swinging()
        self.add(TracedPath(p.bobs[-1].get_center, stroke_color=BLUE))
        self.wait(10)

class SpringExample(SpaceScene):
    def construct(self):
        spring = Spring(start = RIGHT, length = 2*2,color = RED)
        d1 = Dot(color=BLACK).move_to(spring.get_start())
        d2 = Dot(color=BLACK).move_to(spring.get_end())
        self.add(spring,d1,d2)