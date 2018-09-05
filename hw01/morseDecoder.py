import numpy as np
import matplotlib.pyplot as plt

def morseDecode(x, data):
    points = 0
    gap = 0
    morse = []
    decoded = []
    data = data - np.min(data)
    plt.plot(x, data, label='Adjusted')
    plt.legend()
    plt.show()

    for i in range(len(data)):
        if data[i] > 40:
            points += 1
            gap = 0
        elif data[i] <= 40:
            gap += 1
        if points >= 240 and gap >= 70:
            morse.append('dash')
            points = 0
        elif points > 70 and gap > 70:
            morse.append('dot')
            points = 0
        elif gap > 240:
            if morse == ['dot', 'dash']:
                decoded.append('A')
            elif morse == ['dash', 'dot', 'dot', 'dot']:
                decoded.append('B')
            elif morse == ['dash', 'dot', 'dash', 'dot']:
                decoded.append('C')
            elif morse == ['dash', 'dot', 'dot']:
                decoded.append('D')
            elif morse == ['dot']:
                decoded.append('E')
            elif morse == ['dot', 'dot', 'dash', 'dot']:
                decoded.append('F')
            elif morse == ['dash', 'dash', 'dot']:
                decoded.append('G')
            elif morse == ['dash', 'dot', 'dash', 'dash']:
                decoded.append('Y')
            morse = []
            gap = 0
    return decoded
