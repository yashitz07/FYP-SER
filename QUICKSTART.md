# Quick Start Guide

Get the Speech Emotion Recognition system running in minutes!

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/final_year_project.git
cd final_year_project
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Option A: Run Dataset Analysis
```bash
python run_ser_analysis.py
```

This script will:
- Download the RAVDESS dataset (~1.5GB)
- Extract audio metadata
- Generate dataset statistics
- Create visualizations
- Save metadata to CSV

**Expected Output:**
```
============================================================
STEP 1: DOWNLOADING RAVDESS DATASET
============================================================
Dataset downloaded to: C:\Users\...\ravdess-emotional-speech-audio
Total audio files detected: 2880
...
```

### Option B: Run the Streamlit App
```bash
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

**Features:**
- 🎤 Upload audio files for emotion prediction
- 📊 View dataset statistics
- 🤖 Explore model architecture
- 📈 Check performance metrics

## Project Structure

```
final_year_project/
│
├── app.py                      # Streamlit web application
├── run_ser_analysis.py         # Dataset loading & analysis
├── ser_adv_2.ipynb            # Full Jupyter notebook with analysis
├── requirements.txt            # Python dependencies
├── README.md                   # Detailed documentation
├── DEPLOYMENT.md              # Deployment instructions
├── LICENSE                    # MIT License
│
├── ravdess_metadata.csv       # Generated dataset metadata (after running analysis)
├── dataset_distribution.png   # Generated visualization
└── .gitignore                # Git ignore rules
```

## First-Time Setup Checklist

- [ ] Clone repository
- [ ] Create virtual environment
- [ ] Install dependencies
- [ ] Run `python run_ser_analysis.py` (one-time download)
- [ ] Run `streamlit run app.py`
- [ ] Test with sample audio files

## Common Commands

```bash
# Update dependencies
pip install --upgrade -r requirements.txt

# Run with specific host/port
streamlit run app.py --server.port 8001

# Run without opening browser
streamlit run app.py --logger.level=error

# Run in headless mode (server)
streamlit run app.py --server.headless true
```

## Troubleshooting

### Issue: `kagglehub` authentication
**Solution:** 
```bash
# Set Kaggle API credentials
# Windows: Create C:\Users\<username>\.kaggle\kaggle.json
# Linux/Mac: Create ~/.kaggle/kaggle.json

# Add your Kaggle API key inside
{"username": "YOUR_USERNAME", "key": "YOUR_API_KEY"}
```

### Issue: TensorFlow GPU not working
**Solution:** For CPU-only installation:
```bash
pip install tensorflow-cpu
```

### Issue: Audio library errors
**Solution:**
```bash
# On Windows
pip install --upgrade librosa soundfile

# On macOS
brew install libsndfile

# On Linux
sudo apt-get install libsndfile1
```

### Issue: Port 8501 already in use
**Solution:**
```bash
streamlit run app.py --server.port 8502
```

## Next Steps

1. **Explore the Notebook**: Open `ser_adv_2.ipynb` in Jupyter to see detailed analysis
2. **Deploy the App**: Follow [DEPLOYMENT.md](DEPLOYMENT.md) to deploy to Hugging Face Spaces
3. **Customize the App**: Modify `app.py` to add your own features
4. **Train Your Own Model**: Extend `run_ser_analysis.py` with model training

## Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Librosa Documentation](https://librosa.org)
- [TensorFlow Keras Guide](https://tensorflow.org/guide/keras)
- [RAVDESS Dataset](https://zenodo.org/record/4382563)

## Support

- Create issues on GitHub
- Check existing issues for solutions
- Read the detailed [README.md](README.md)

---

**Happy analyzing emotions in speech! 🎤🎵**
