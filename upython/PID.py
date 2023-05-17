TIME_STEP = 0.1
class PID(object):
    def __init__(self, Kp, Ki, Kd,target):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = target
        self.error = 0
        self.error_last = 0
        self.integral_error = 0
        self.derivative_error = 0
        self.output = 0
    def compute(self, pos):
        self.error = target - pos
        self.integral_error += self.error * TIME_STEP
        self.derivative_error = (self.error - self.error_last)/TIME_STEP
        self.error_last = self.error
        self.output = self.Kp*self.error + self.Ki*self.integral_error + self.Kd*self.derivative_error
        return self.output