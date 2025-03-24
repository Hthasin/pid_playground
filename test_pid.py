from pid import PIDController

test_one = PIDController(0.1, 0.2, 5, setpoint=10)

measured_value = 2 
dt = 0.5

for _ in range(10):  # simulate 3 steps
    output = test_one.update(measured_value, dt)
    measured_value += output * dt
    print(output)
    print(f"Integral so far: {test_one.totalErrors}")





