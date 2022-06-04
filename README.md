# DSP_py
Digital signal processing codes implemented in Python 3

butterworth_filter.py:

Requires Python 3, Numpy, Scipy, and Matplotlib.
Applies a butterworth filter to low-pass filter a simulated sinusoidal
signal. Outputs plots of the simulated sigmal and its frequency 
spectrum before and after filtering.


frequency_interactive.py:

Interactive illustration of the relationship between a sine-wave's frequency and it's Fourier transfrom.
The code runs in a Jupyter-like code cell within Python code defined with a # %% comment. Click Run Cell. An interactive plot opens in an interactive window. Move the frequency slider at the top of the interactive plot and watch the sine wave frequency and the Fourier transform plots change simultaneously. Requirements: Python 3, ipywidgets, numpy, scipy, matplotlib, and Jupyter. Recommend using Visual Studio Code or other IDE that supports Jupyter-like code cells. For documentation on Visual Studio Code, see https://code.visualstudio.com/docs/python/jupyter-support-py#_jupyter-code-cells. 

frequency_interactive.ipynb:

Interactive illustration of the relationship between a sine-wave's frequency and it's Fourier transfrom in a Jupyter notebook.
Run the code cells. An interactive plot opens. Move the frequency slider at the top of the interactive plot and watch the sine wave frequency and the Fourier transform plots change simultaneously. Requirements: Python 3, ipywidgets, numpy, scipy, matplotlib, and Jupyter. 

notch_filter.py:

Requires Python 3, Numpy, Scipy, and Matplotlib.
Creates and applies an IIR notch filter using scipy

notch_filter.ipynb:

Requires Python 3, Numpy, Scipy, Matplotlib, and Jupyter.
In a Jupyter notebook, creates and applies an IIR notch filter using scipy

binary_to_numpy.py

Requires Python 3 and Numpy
Writes a numpy array to a binary file and reads data from a binary file and puts the data into a numpy array

binary_to_numpy.ipynb

Requires Python 3, Numpy and Jupyter
Writes a numpy array to a binary file and reads data from a binary file and puts the data into a numpy array
