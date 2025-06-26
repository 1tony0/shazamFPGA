# 🎵 DE10-Nano Music Recognition System (Shazam Clone)

This project done by Antonio and Skye implements a real-time music recognition system on the **Terasic DE10-Nano FPGA SoC**, inspired by **Shazam**. It captures audio from a USB microphone, performs FFT and peak detection on the FPGA, and uses the ARM processor running Linux to match extracted fingerprints against a local song database.

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
````

---

## 🧱 Project Structure

```
de10nano-music-id/
├── fpga/                # All VHDL logic
│   ├── fft_engine.vhd
│   ├── windowing.vhd
│   ├── peak_picker.vhd
│   └── fifo_interface.vhd
│
├── linux/               # Python scripts on Linux (HPS)
│   ├── record_audio.py
│   ├── send_to_fpga.py
│   ├── read_from_fpga.py
│   ├── fingerprint.py
│   ├── match_db.py
│   └── main.py
│
├── db/                  # Audio fingerprint database
│   ├── fingerprints.sqlite
│   ├── build_db.py
│   └── audio_clips/
│       └── song1.wav ...
│
└── README.md
```

---

## 🚀 Setup Instructions

### 1. FPGA Side (Quartus)

* Open Quartus and create a new project
* Add all VHDL files from `fpga/`
* Instantiate FFT IP core (512-point, fixed-point)
* Compile and flash bitstream to FPGA

### 2. Linux Side (DE10-Nano HPS)

* Flash Ubuntu or Debian to SD card for HPS
* Enable USB mic support (test with `arecord`)
* Clone this repo on the board and install Python dependencies

```bash
sudo apt update && sudo apt install python3-pip alsa-utils
pip3 install numpy scipy sounddevice sqlite3
```

* Populate your fingerprint database:

```bash
cd db/
python3 build_db.py
```

* Add `.wav` clips (16kHz, mono, short samples) to `audio_clips/`

---

## 📈 How to Use

### Step-by-Step:

```bash
cd linux/
python3 main.py
```

This script will:

1. Record a short audio sample via USB mic
2. Send raw audio to FPGA for FFT + peak picking
3. Read frequency peaks from FPGA
4. Generate audio fingerprints
5. Search for best matching song in database
6. Output song title and match confidence

---

## 🧪 Example Output

```bash
🎙️ Recording audio for 5 seconds...
📡 Sending to FPGA...
📊 Reading FFT peaks...
🔎 Matching fingerprints in database...
✅ Match: "Bohemian Rhapsody" by Queen
🎯 Confidence: 92.3% (184 peak hashes matched)
```

---

## 🔧 Troubleshooting

* No mic input? Try: `arecord -l` to list devices.
* Mic not detected? Try a different USB port or add ALSA config.
* Mismatched FFT? Check windowing function in `windowing.vhd`.
* Incorrect peaks? Plot using `debug_peaks.py` to visualize.
* No matches? Ensure `.wav` files in `db/audio_clips/` are short, mono, and preprocessed.

---

## 🌱 Future Work

* Replace FFT with MFCC feature extractor
* Add LCD display / LED indicator for song match
* Optimize peak matching with C++ backend
* Stream audio over Wi-Fi from external device

---

## 👥 Authors

* Partner A – FPGA & VHDL
* Partner B – Linux, Python & database
* Based on academic research and open-source libraries like Chromaprint, Dejavu, and Spiral FFT.
