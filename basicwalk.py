import numpy
from spotpuppy.models import quadruped_base
from spotpuppy.utils.pid_control import pid_controller
import math
import time


# Must extend the base class
class quadruped(quadruped_base.quadruped):
    def __init__(self, **kwargs):
        # Initialise the base class
        super().__init__(**kwargs)

        self.state = 2
        self.trot_speed = numpy.array(2)
        self.trot_rotation = 0.0

        self.t = 0
        self.elapsed = time.time()

    '''
    def _get_custom_json_params(self):
        pass
        
    def _set_custom_json_params(self):
        pass
    '''

    def _on_update(self):
        current_time = time.time()
        self.t += (current_time - self.elapsed) * 2
        self.elapsed = self.t
        self.state_walk()

    def state_walk(self):
        # Rear legs are 3/4 of a cycle behind front to aid balance.
        leg0 = max(math.sin(math.pi * self.t), 0) * -3
        leg1 = max(math.sin((math.pi * self.t) + math.pi), 0) * -3
        leg2 = max(math.sin((math.pi * self.t) + (math.pi * (-1.5))), 0) * -3
        leg3 = max(math.sin((math.pi * self.t) + (math.pi * (-0.5))), 0) * -3
        self.quad_controller.set_leg(0, self.get_dir("global.down") * (leg0 + 7))
        self.quad_controller.set_leg(1, self.get_dir("global.down") * (leg1 + 7))
        self.quad_controller.set_leg(2, self.get_dir("global.down") * (leg2 + 7))
        self.quad_controller.set_leg(3, self.get_dir("global.down") * (leg3 + 7))
