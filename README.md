# 🎵 DE10-Nano Music Recognition System (Shazam Clone)

This project implements a real-time music recognition system on the **Terasic DE10-Nano FPGA SoC**, inspired by **Shazam**. It captures audio from a USB microphone, performs FFT and peak detection on the FPGA, and uses the ARM processor running Linux to match extracted fingerprints against a local song database.

---

## 📌 Features
- Real-time audio capture from USB microphone
- FPGA-accelerated FFT and peak picking
- ARM-side fingerprinting and hash matching
- Local song database using SQLite
- Full hardware/software co-design (VHDL + Python)

---

## 🛠️ Hardware Requirements
- Terasic DE10-Nano Board (Cyclone V SoC)
- USB Microphone or line-in audio adapter
- MicroSD card (8GB+)
- PC with Quartus Prime (Lite) + Ubuntu/Linux support
- Optional: logic analyzer or oscilloscope (for FPGA debugging)

---

## 💻 Software Requirements
### On PC (for development):
- Intel Quartus Prime Lite (for VHDL development)
- Python 3.8+
- Git
- Optional: Audacity, SoX (for trimming audio)

### On DE10-Nano (Linux side):
- Ubuntu (or Linaro) Linux image running on HPS (ARM Cortex-A9)
- Python packages:  
  ```bash
  pip install sounddevice numpy scipy librosa sqlite3
