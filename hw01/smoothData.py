# Function to smooth arrays of data using multi-run running average method
def smooth(x, y):
    for i in range(1, len(y)-1):
        y[i] = y[i-1]+(x[i]-x[i-1])*((y[i+1]-y[i-1])/(x[i+1]-x[i-1]))
    span = [5, 11, 31, 51, 61, 31, 11, 5]  # Spans
    for i in range(len(span)):
        span_halved = int((span[i] - 1) / 2)
        for j in range(span_halved, len(x)-span_halved):
            y_avg = 0
            for k in range(j-span_halved, j+span_halved+1):
                y_avg += y[k]
            y_avg = y_avg / span[i]
            y[j] = y_avg
    return y
