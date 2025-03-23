class PIDController: 
    def __init__(self, kp, ki, kd, setpoint):

        # gains 
        self.kp = kp
        self.ki = ki
        self.kd = kd

        #desired position 
        self.setpoint = setpoint

        #initialize prev error to 0 
        self.prev_error = 0

        #represent cumulative error over time; init to 0 
        self.totalErrors = 0 

    def update(self, measured_value, dt):
        '''This function calculates the PID with the given values'''
        
        current_error = self.setpoint - measured_value # current error 

        #measures integral

        self.totalErrors += current_error * dt #sum of all errors times the change in time (rieman sums substitutes for integral)

        #measures derivative; in case 0 we need to set derivative to zero 
        if dt > 0:
            derivative = (current_error - self.prev_error) / dt # think [y(t) - y(t-1) / delta(t)]
        else: 
            derivative = 0 

        # set up prev_error for next loop 
        self.prev_error = current_error 
        
        p = current_error * self.kp
        i = self.totalErrors * self.ki 
        d = derivative * self.kd

        output = p + i + d

        return output






