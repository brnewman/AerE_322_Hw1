import matplotlib.pyplot as pyplot
import numpy as np
import hw01.importData as importData
import hw01.smoothData as smoothData
import hw01.fitSineCurve as fitSineCurve
import hw01.morseDecoder as morseDecoder


# Get data from file
filename = '/home/brnewman/Documents/AerE_322/HW1_Data.txt'
data = importData.getData(filename)
x = data[:,0]
y = data[:,1]
raw_data = []
for i in range(len(y)):
    raw_data.append(y[i])

# Plot raw data
pyplot.plot(x, y, ':', label='Raw Data')

# Get smoothed data
y_avg = smoothData.smooth(x, y)

# trim smoothed data

# Plot smoothed data
pyplot.plot(x[4:len(x)-4], y_avg[4:len(y)-4], label='Running Average')

# Fit data to a sine curve
data_fit = fitSineCurve.fit_sin(x, y_avg)

# Plot sine fit data
pyplot.plot(x, data_fit["fitfunc"](x), label='Sine fit')

pyplot.show()

# Subtract baseline
leveled_1 = smoothData.smooth(x, np.subtract(raw_data, y_avg))
leveled_2 = smoothData.smooth(x, np.subtract(raw_data, data_fit["fitfunc"](x)))

# leveled_1 = np.subtract(raw_data, y_avg)
# leveled_2 = np.subtract(raw_data, data_fit["fitfunc"](x))

pyplot.plot(x, raw_data, label="Raw Data")
pyplot.plot(x, leveled_1, label="Leveled(Avg)")
pyplot.plot(x, leveled_2, label='Leveled(fit)')
pyplot.legend()
pyplot.show()

morse2 = morseDecoder.morseDecode(x, leveled_2)
print(morse2)