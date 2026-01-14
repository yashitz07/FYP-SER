# Deployment Guide for Speech Emotion Recognition App

This guide explains how to deploy the SER (Speech Emotion Recognition) system on Hugging Face Spaces.

## Option 1: Deploy on Hugging Face Spaces (RECOMMENDED)

### Prerequisites
- Hugging Face account (create free at https://huggingface.co)
- Git (already installed)

### Step 1: Create a Hugging Face Repository

1. Go to https://huggingface.co/new
2. Create a new Space (not a model/dataset)
3. Select "Streamlit" as the Space SDK
4. Name it `speech-emotion-recognition` or similar
5. Set visibility to "Public" or "Private"
6. Create the Space

### Step 2: Clone and Push Your Project

```bash
# Clone your local project
cd final_year_project

# Add Hugging Face remote
git remote add huggingface https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME

# Push to Hugging Face
git push huggingface master  # or main, depending on your branch name
```

### Step 3: Configure for Hugging Face

Create a `packages.txt` file for system dependencies:

```text
libsndfile1
ffmpeg
```

Update `requirements.txt` with all dependencies:

```
streamlit==1.52.2
librosa==0.11.0
tensorflow==2.20.0
scikit-learn==1.8.0
pandas==2.3.3
numpy==2.3.5
matplotlib==3.10.8
seaborn==0.13.2
scipy==1.17.0
soundfile==0.13.1
kagglehub==0.4.0
```

### Step 4: Set up Environment Variables (if needed)

If using Kaggle API for dataset download:

1. In Hugging Face Spaces, go to Settings > Secrets
2. Add `KAGGLE_USERNAME` and `KAGGLE_KEY` if using private datasets
3. Create `~/.kaggle/kaggle.json` with credentials

### Step 5: Update app.py for Hugging Face

The current `app.py` is already configured for Hugging Face Spaces. Key features:
- Uses Streamlit caching
- No heavy computations on page load
- Supports file uploads
- Lightweight demo predictions

### Deploy!

```bash
git add .
git commit -m "Deploy to Hugging Face Spaces"
git push huggingface
```

Your app will be live at: `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`

---

## Option 2: Deploy on Streamlit Cloud

### Prerequisites
- Streamlit Cloud account (free at https://streamlit.io/cloud)
- GitHub account with your repo pushed

### Steps

1. Go to https://share.streamlit.io
2. Click "Deploy an app"
3. Select your GitHub repository
4. Choose the branch and file (`app.py`)
5. Click Deploy

Your app will be live at: `https://share.streamlit.io/YOUR_USERNAME/YOUR_REPO/YOUR_BRANCH/app.py`

---

## Option 3: Deploy on Docker/AWS/Google Cloud

### Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libsndfile1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:

```bash
docker build -t ser-app .
docker run -p 8501:8501 ser-app
```

---

## Option 4: Deploy on AWS with Streamlit

1. **Create EC2 Instance**
   - Ubuntu 20.04 LTS
   - Install Python 3.9+

2. **Setup on Instance**
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip git
   git clone <your-repo>
   cd final_year_project
   pip install -r requirements.txt
   ```

3. **Run with Streamlit**
   ```bash
   streamlit run app.py \
     --server.port 80 \
     --server.address 0.0.0.0 \
     --server.headless true
   ```

4. **Use PM2 for persistence**
   ```bash
   npm install -g pm2
   pm2 start "streamlit run app.py" --name ser-app
   pm2 startup
   pm2 save
   ```

---

## Testing Locally Before Deployment

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Open browser to http://localhost:8501
```

---

## Troubleshooting

### Issue: ModuleNotFoundError
**Solution:** Ensure all packages are in `requirements.txt`

### Issue: Audio file not processing
**Solution:** Ensure `librosa` and `soundfile` are installed with system audio libraries

### Issue: Memory/Timeout on Hugging Face
**Solution:** 
- Use lighter models (quantization)
- Cache model loading
- Optimize feature extraction

### Issue: Large file upload fails
**Solution:**
- Set `server.maxUploadSize = 200` in Streamlit config
- Compress audio before upload

---

## Performance Optimization

### For Hugging Face Spaces (Free Tier)

1. **Use Cached Models**
   ```python
   @st.cache_resource
   def load_model():
       return tf.keras.models.load_model('model.h5')
   ```

2. **Optimize Feature Extraction**
   - Reduce audio resolution
   - Use smaller feature sets
   - Cache feature values

3. **Reduce Model Size**
   - Use TensorFlow Lite
   - Quantize weights
   - Use smaller architectures

### Example: Lightweight Model Loading

```python
import streamlit as st

@st.cache_resource
def get_scaler():
    return pickle.load(open('scaler.pkl', 'rb'))

@st.cache_resource
def get_model():
    # Only load model once
    return tf.keras.models.load_model('ser_model_lite.h5')

if st.button("Predict"):
    model = get_model()
    scaler = get_scaler()
    # Use them
```

---

## Production Checklist

- [x] README.md with instructions
- [x] requirements.txt with all dependencies
- [x] .gitignore for sensitive files
- [x] LICENSE file
- [x] Streamlit app with proper error handling
- [ ] Model weights file (serialize and include)
- [ ] Environment variables for sensitive data
- [ ] Tests for core functionality
- [ ] Logging and monitoring
- [ ] Regular updates and maintenance

---

## Next Steps

1. **Push to GitHub** (if not already done)
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/final_year_project
   git push -u origin master
   ```

2. **Create Hugging Face Space** and link to GitHub

3. **Test deployment** by accessing the live URL

4. **Share with others** and collect feedback

5. **Monitor and improve** based on usage

---

## Useful Links

- Streamlit Deployment: https://docs.streamlit.io/deploy/streamlit-community-cloud
- Hugging Face Spaces: https://huggingface.co/docs/hub/spaces
- Docker Deployment: https://docs.docker.com/get-started/
- AWS Streamlit: https://docs.aws.amazon.com/

---

## Support & Community

- Streamlit Community: https://discuss.streamlit.io
- Hugging Face Community: https://discuss.huggingface.co
- GitHub Issues: Create issues in your repo for bugs

---

Happy deploying! 🚀
