\# Music Recognition - Data Pipeline \& Notebooks



Complete pipeline for building a music recognition system using YAMNet embeddings.



\## Overview



This repository contains the data processing pipeline for creating a music recognition database. The system downloads songs from YouTube, extracts audio embeddings using Google's YAMNet model, and generates a searchable database for real-time song identification.



\## Notebooks



\### 1. Download Songs

Downloads a diverse dataset of 1000+ songs from YouTube across multiple genres and languages.



\*\*Duration\*\*: 2-4 hours



\*\*Output\*\*: Audio files in MP3/M4A format (~2-3 GB)



\### 2. Extract Embeddings

Processes audio files through YAMNet to generate 1024-dimensional embeddings for each song.



\*\*Duration\*\*: 8-10 hours on CPU



\*\*Output\*\*: 

\- Embeddings array (1000 × 1024)

\- Metadata CSV with song information



\### 3. Real-time Recognition

Tests the recognition system with live audio input and validates accuracy.



\## Quick Start



Install dependencies:

```bash

pip install -r requirements.txt

```



Run notebooks in order:

```bash

jupyter notebook

```



\## System Requirements



\- Python 3.8+

\- 10 GB free disk space

\- Stable internet connection

\- 8-16 GB RAM



\## Configuration



Update paths in notebooks to match your system:



```python

AUDIO\_FOLDER = r"C:\\path\\to\\audio\_files"

OUTPUT\_DIR = r"C:\\path\\to\\embeddings\_database"

```



\## Generated Files



The pipeline creates:

\- Audio dataset (2-3 GB)

\- Embeddings database (4 MB)

\- Song metadata (CSV)



Note: Audio files and embeddings are not included in this repository due to size constraints.



\## Technology Stack



\- TensorFlow 2.20

\- YAMNet (Google Research)

\- librosa for audio processing

\- yt-dlp for downloads

\- NumPy \& Pandas for data handling



\## Related



Frontend web application: \[music-recognition-frontend](https://github.com/Rahma-jelassi/music-recognition-frontend)



\## License



MIT License
## Configuration

After cloning the repository, you need to configure paths in the notebooks:

### For Notebook 2: Extract Embeddings

Open `2_extract_embeddings.ipynb` and update these paths:

```python
# Audio files location (from downloads)
AUDIO_FOLDER = r"C:\Users\Rahmaa\Desktop\deep learning\downloadSongs\audio_dataset_1000"

# Where to save embeddings
OUTPUT_DIR = r"C:\Users\Rahmaa\Desktop\deep learning\audio_embeddings_database"
```

**Change to YOUR paths:**
```python
AUDIO_FOLDER = r"C:\YOUR\PATH\TO\audio_dataset_1000"
OUTPUT_DIR = r"C:\YOUR\PATH\TO\audio_embeddings_database"
```

### For Notebook 3: Recognition

Open `3_recognition_realtime.ipynb` and update:

```python
# Device for audio capture
DEVICE_INDEX = 1  # Find yours with: sd.query_devices()

# Database location
DATABASE_DIR = r"C:\YOUR\PATH\TO\audio_embeddings_database"
```

### For Script: Download Songs

Open `scripts/downloadSongs.py` and update:

```python
OUTPUT_DIR = r"C:\YOUR\PATH\TO\audio_dataset_1000"
```

### Quick Setup Example

```python
# Example configuration for Windows
AUDIO_FOLDER = r"C:\Users\YourName\Music\audio_dataset"
OUTPUT_DIR = r"C:\Users\YourName\Music\embeddings"

# Example for Mac/Linux
AUDIO_FOLDER = "/home/yourname/music/audio_dataset"
OUTPUT_DIR = "/home/yourname/music/embeddings"
```
