class TemperatureSystem: 
    def __init__(self, alpha, initialTemp):
        self.alpha = alpha
        self.temp = initialTemp
    
    def updateTemp(self, heat_power, dt): 
        self.temp += self.alpha * heat_power * dt 
        return self.temp 
