# Applies a butterworth filter to low-pass filter a simulated sinusoidal
# signal. Output plots of the simulated sigmal and its frequency 
# spectrum before and after filtering.

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Filter specs
f1 = 25 # [ Hz ]
f2 = 50 # [ Hz ]
N = 10 # Order of the filter
fs = 1000 # [ Hz ]
duration = 1 # [ seconds ]

# Generate the time vector of 1 second duration
t = np.linspace(0, duration, fs) # 1000 samples in 1 second , fs = 1000 Hz
# Generate the signal containing f1 and f2
s = np.exp(1j*2*np.pi*f1*t) + np.exp(1j*2*np.pi*f2*t)

# Add randome noise
mu, sigma = 0, 1 # mean and standard deviation
nr = np.random.default_rng().normal(mu, sigma, len(t))
ni = np.random.default_rng().normal(mu, sigma, len(t))
n = nr + ni * 1j
sig = s + n

# filter signal to remove the 50 Hz signal
sos = signal.butter(N, 35, 'lp', fs = 1000, output = 'sos')
filtered = signal.sosfiltfilt(sos, sig)

# Frequency spectrum of sig
n = fs * duration
yf_sig = fft(sig)
xf = fftfreq(n, 1 / fs)

# Frequency spectrum of filtered
yf_filt = fft(filtered)

# Display the signal
fig, (ax1, ax2) = plt.subplots(2, 1, sharex = False)
ax1.plot(t, np.real(sig))
ax1.grid(True)
ax1.axis([0, 1, -2, 2])
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")
ax1.set_title("25 Hz and 50 Hz sinusoids")

ax2.plot(xf, np.abs(yf_sig)/n)
ax2.grid(True)
ax2.axis([-100, 100, -1, 1])
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Amplitude")
ax2.set_title("Spectrum of sig")
plt.tight_layout()
plt.show()

# Display the filtered signal
fig, (ax3, ax4) = plt.subplots(2, 1, sharex = False)
ax3.plot(t, np.real(filtered))
ax3.grid(True)
ax3.set_title("After 35 Hz low-pass filter")
ax3.axis([0, 1, -2, 2])
ax3.set_ylabel("amplitude")
ax3.set_xlabel("Time (seconds)")

ax4.plot(xf, np.abs(yf_filt)/n)
ax4.grid(True)
ax4.axis([-100, 100, -1, 1])
ax4.set_xlabel("Frequency (Hz)")
ax4.set_ylabel("Amplitude")
ax4.set_title("Spectrum of filtered sig")
plt.tight_layout()
plt.show()

print("\nGo U.C. Davis Aggies!\n")