"""
Rocket Controller Testing Software
"""
import numpy as np

class CPU:
    def __init__(self, clk_speed):
        self.gyro = np.zeros((3, 1))
        self.accel = np.zeros((3, 1))
        self.hz = clk_speed
        
cpu = CPU(5e6)

print(cpu.accel)