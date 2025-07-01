import sounddevice as sd
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

fs = 16000  # Sample rate
duration = 5  # seconds

print("Recording...")
audio = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype='float32')
sd.wait()
print("Done recording.")

# Plot spectrogram
f, t, Sxx = scipy.signal.spectrogram(audio[:, 0], fs=fs, nperseg=512, noverlap=256)
plt.pcolormesh(t, f, 10 * np.log10(Sxx + 1e-10), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.title('Spectrogram of Recording')
plt.colorbar(label='dB')
plt.show()
