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

