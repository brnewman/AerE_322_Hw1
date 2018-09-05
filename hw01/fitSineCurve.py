import numpy as np
import scipy
from scipy.optimize import leastsq
import matplotlib.pyplot as plt


# Fits data to a sin curve
def fit_sin(t,y):
    # guess_mean = np.mean(y)
    # guess_std = 3*np.std(y)/(2**.5)/(2**.5)
    # guess_phase = 0
    # guess_freq = 1
    # guess_amp = 1
    #
    # data_first_guess = guess_std*np.sin(t+guess_phase)+guess_mean
    #
    # optimize_func = lambda x: x[0]*np.sin(x[1]*t+x[2]) + x[3] - y
    # est_amp, est_freq, est_phase, est_mean = leastsq(optimize_func, [guess_amp, guess_freq, guess_phase, guess_mean])[0]
    # data_fit = est_amp*np.sin(est_freq*t+est_phase) + est_mean
    #
    # fine_t = np.arange(0, max(t), max(t)/len(t))
    # data_fit = est_amp*np.sin(est_freq*t+est_phase) + est_mean
    #
    # # plt.plot(t, y, ':')
    # # plt.plot(t, data_first_guess, label='first guess')
    # # plt.plot(fine_t, data_fit, label='after fitting')
    # # plt.legend()
    # # plt.show()
    #
    # return data_fit, fine_t

    f = np.fft.fftfreq(len(t), (t[1]-t[0]))
    Fy = abs(np.fft.fft(y))
    guess_freq = abs(f[np.argmax(Fy[1:])+1])
    guess_amp = np.std(y)*2.**0.5
    guess_offset = np.mean(y)
    guess = np.array([guess_amp, 2.*np.pi*guess_freq, 0., guess_offset])

    def sinfunc(t, A, w, p, c): return A * np.sin(w*t + p) + c
    popt, pcov = scipy.optimize.curve_fit(sinfunc, t, y, p0=guess)
    A, w, p, c = popt
    f = w/(2.*np.pi)
    fitfunc = lambda t: A * np.sin(w*t + p) + c
    return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "periods": 1./f, "fitfunc": fitfunc, "maxcov": np.max(pcov), "rawres": (guess, popt, pcov)}

