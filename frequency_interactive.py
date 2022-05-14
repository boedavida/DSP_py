# Interactive illustration of the relationship between 
# a sine-wave's frequency and it's Fourier transfrom.

# The code runs in a Jupyter-like code cell within Python code
# defined with a # %% comment. Click Run Cell. An interactive plot 
# opens in an interactive window. Move the frequency slider at the 
# top of the interactive plot and watch the sine wave frequency and 
# the Fourier transform plots change simultaneously. 

# Requirements: Python 3, ipywidgets, numpy, scipy, matplotlib, and
# Jupyter. Recommend using Visual Studio Code or other IDE that 
# supports Jupyter-like code cells. 

# %%
from ipywidgets import interact, IntSlider
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt 


@interact(frequency=IntSlider(min=1, max=100))
def plot_sin(frequency):
    xs = np.linspace(0, 1, 1000)
    fs = 1000
    T = 1/fs
    N = len(xs)
    xf = fftfreq(N, T)
    y = np.sin(2*np.pi*frequency*xs)
    f = fft(y)
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(xs, y, label='sin(x) frequency = %s' % (frequency))
    ax[0].grid()
    ax[0].set_title('Sine Wave')
    ax[0].set_xlabel('Time (s)')
    ax[1].plot(xf, abs(f)/N, label='FFT, sin(x) frequency = %s' % (frequency))
    ax[1].grid()
    ax[1].set_xlim([-100, 100])
    ax[1].set_title('Fourier Transform of Sine Wave')
    ax[1].set_xlabel('Frequency (Hz)')
    fig.tight_layout()
    plt.show()

# %%
