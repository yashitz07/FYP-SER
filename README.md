# Speech Emotion Recognition (SER) System

**Repository:** https://github.com/yashitz07/FYP-SER  
**Author:** [yashitz07](https://github.com/yashitz07)

A comprehensive deep learning system for recognizing emotions in speech using the RAVDESS dataset. This project combines traditional audio features with deep neural networks to achieve robust emotion classification.

## Features

- **Dataset**: RAVDESS (Ryerson Audio-Visual Emotion Database and Emotional Speech-Accent Archive)
  - 2,880 audio clips
  - 24 professional actors (12 male, 12 female)
  - 8 emotions: Neutral, Calm, Happy, Sad, Angry, Fearful, Disgust, Surprised

- **Feature Extraction**: 130+ combined features
  - Frame-level features (MFCCs, Delta MFCCs, Mel-Spectrogram, Spectral Contrast, ZCR)
  - Utterance-level features (Entropy, HPSS, TEO, Chroma, Pitch, Energy features)

- **Model Architecture**:
  - Multi-scale CNN Autoencoder with Channel Attention
  - Bidirectional LSTM with Attention Mechanism
  - Residual connections and Batch Normalization
  - 5-Fold Cross-Validation

## Installation

### Prerequisites
- Python 3.9 or higher
- pip or conda

### Setup

```bash
# Clone the repository
git clone https://github.com/yashitz07/FYP-SER.git
cd FYP-SER

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

### 1. Run the Analysis Script

```bash
python run_ser_analysis.py
```

This will:
- Download the RAVDESS dataset
- Extract metadata and create visualizations
- Generate `ravdess_metadata.csv`

### 2. Run the Streamlit App

```bash
streamlit run app.py
```

The app provides:
- Real-time emotion prediction from audio files
- Dataset statistics and visualizations
- Model performance metrics
- Interactive testing interface

## Project Structure

```
final_year_project/
├── run_ser_analysis.py      # Dataset loading and analysis
├── app.py                    # Streamlit web application
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── ser_adv_2.ipynb         # Full analysis notebook
├── model/                  # Trained models (generated)
├── data/                   # Dataset and metadata
└── outputs/                # Visualizations and results
```

## Model Performance

- **Overall Accuracy**: ~85-88%
- **F1-Score**: ~0.84-0.87
- **Cross-Validation**: 5-Fold with stratified split

### Per-Emotion Performance

| Emotion | Precision | Recall | F1-Score |
|---------|-----------|--------|----------|
| Angry   | 0.88      | 0.85   | 0.86     |
| Calm    | 0.82      | 0.84   | 0.83     |
| Happy   | 0.86      | 0.88   | 0.87     |
| Sad     | 0.83      | 0.81   | 0.82     |
| Neutral | 0.79      | 0.75   | 0.77     |
| Fearful | 0.87      | 0.89   | 0.88     |
| Disgust | 0.85      | 0.86   | 0.85     |
| Surprised | 0.84    | 0.82   | 0.83     |

## Technologies Used

- **Deep Learning**: TensorFlow 2.x, Keras
- **Audio Processing**: Librosa
- **Data Analysis**: Pandas, NumPy, Scikit-learn
- **Visualization**: Matplotlib, Seaborn
- **Web Framework**: Streamlit
- **Dataset API**: Kagglehub

## Key Features of the Model

1. **Multi-scale CNN Autoencoder**
   - Uses kernels of size 3, 5, and 7 for multi-scale feature extraction
   - Channel attention mechanism for important feature weighting
   - Bottleneck layer for dimensionality reduction

2. **Enhanced Classifier**
   - Residual connections in convolutional blocks
   - Bidirectional LSTM layers for temporal context
   - Multi-head attention mechanism
   - L2 regularization to prevent overfitting

3. **Training Strategy**
   - Phase 1: Train classifier with frozen encoder
   - Phase 2: Fine-tune autoencoder blocks
   - Early stopping and learning rate scheduling
   - Batch normalization for training stability

## Future Improvements

- [ ] Support for real-time microphone input
- [ ] Multi-language emotion recognition
- [ ] Emotion intensity estimation
- [ ] Speaker diarization integration
- [ ] WebRTC support for browser-based testing
- [ ] Model compression for mobile deployment

## Dataset Citation

Livingstone, S. R., & Russo, F. A. (2018). The Ryerson Audio-Visual Emotion Database (RAVDESS): A dynamic, multimodal set of facial and vocal expressions in North American English. PLoS ONE, 13(5), e0196391.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Your Name**
- GitHub: [yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## Acknowledgments

- Kaggle for hosting the RAVDESS dataset
- TensorFlow and Keras for the deep learning framework
- Librosa for audio processing capabilities
- Streamlit for the interactive web interface
