# pedometer algorithm

import serial
import numpy as np
from scipy.fftpack import fft
import os


ser = serial.Serial("COM3",115200) # computer serial port is COM3
gz = []  # the gyroscope of z-axis
i_step = []
flag = False

def  count_step(g_window):
    # applying fft algorithm
    sliding_window = len(g_window)
    T = 0.05   # 50ms
    g_windowf = fft(g_window)
    g_f = 2.0/sliding_window * np.abs(g_windowf[0:sliding_window//2])
    xf = np.linspace(0.0, 1.0/(2.0*T), sliding_window//2)

    index = np.where(np.logical_and(xf>=0.6, xf<=2))
    index_1 = np.where(np.logical_and(xf>=0, xf<=0.6))
    if index[0].size == 0:
        return 0
    else:
        xf_between = xf[index]
        g_windowf_between = g_f[index]
        # g_windowf_between_1 = g_f[index_1]
        if np.mean(g_windowf_between) >= 2.5:
            index_max = np.where(g_windowf_between == max(g_windowf_between))
            count_step = xf_between[index_max[0][0]]*1.2
            return count_step
        else:
            return 0

while True:
    cc = str(ser.readline())
    raw_data = cc.split(",")
    if (len(cc)<16) or len(raw_data) != 3:
        continue
    else:
        gz.append(float(raw_data[1]))

        if len(gz)% 50 == 0:
            flag = True
            i_th_step =  round(count_step(gz))
            i_step.append(i_th_step)
            if i_th_step == 0:
              flag = False
              gz = []
        os.system('cls')
        if flag:
          print("Current Status: Walking")
          print("Step Count:", sum(i_step))
        else:
          print("Current Status: Standing or Typing")
          print("Step Count:", sum(i_step))
