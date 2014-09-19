"""
Runs an attached Medium Motor for 50 turns.

This is the example used on the site README.

HARDWARE:
    Medium Motor plugged into any motor port.
"""
from ev3.lego import MediumMotor
d = MediumMotor()
d.reset()
d.run_forever(50, regulation_mode=False)
d.stop()
exit()
