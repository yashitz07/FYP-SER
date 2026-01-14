#!/usr/bin/env python
"""
Speech Emotion Recognition (SER) Analysis Script
Downloads RAVDESS dataset, extracts features, and trains a deep learning model
"""

import kagglehub
import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Download RAVDESS dataset
print("="*60)
print("STEP 1: DOWNLOADING RAVDESS DATASET")
print("="*60)
path = kagglehub.dataset_download("uwrfkaggler/ravdess-emotional-speech-audio")
print(f"Dataset downloaded to: {path}")

# RAVDESS emotion mapping
emotion_map = {
    '01': 'neutral',
    '02': 'calm',
    '03': 'happy',
    '04': 'sad',
    '05': 'angry',
    '06': 'fearful',
    '07': 'disgust',
    '08': 'surprised'
}

emotion_intensity = {
    '01': 1,  # Neutral
    '02': 2,  # Calm
    '03': 2,  # Happy
    '04': 2,  # Sad
    '05': 2,  # Angry
    '06': 2,  # Fearful
    '07': 2,  # Disgust
    '08': 2   # Surprised
}

# Find all .wav files
search_patterns = [
    os.path.join(path, "Actor_*", "*.wav"),
    os.path.join(path, "audio_speech_actors_01-24", "Actor_*", "*.wav"),
    os.path.join(path, "**", "*.wav")
]

wav_files = []
for pattern in search_patterns:
    matches = glob.glob(pattern, recursive=True)
    wav_files.extend(matches)

wav_files = sorted(list(set(wav_files)))

# Parse filenames and extract comprehensive metadata
metadata = {
    'filepath': [],
    'filename': [],
    'actor_id': [],
    'emotion_id': [],
    'emotion_label': [],
    'intensity': [],
    'statement': [],
    'repetition': [],
    'gender': []
}

for filepath in wav_files:
    filename = os.path.basename(filepath)
    parts = filename.split('-')

    if len(parts) >= 7:
        emotion_id = parts[2]
        if emotion_id in emotion_map:
            metadata['filepath'].append(filepath)
            metadata['filename'].append(filename)
            metadata['actor_id'].append(parts[6].split('.')[0])
            metadata['emotion_id'].append(emotion_id)
            metadata['emotion_label'].append(emotion_map[emotion_id])
            metadata['intensity'].append(emotion_intensity.get(parts[3], 1))
            metadata['statement'].append(parts[4])
            metadata['repetition'].append(parts[5])
            metadata['gender'].append('female' if int(parts[6].split('.')[0]) % 2 == 0 else 'male')

# Create DataFrame for analysis
df_metadata = pd.DataFrame(metadata)
print(f"Total audio files detected: {len(df_metadata)}")
print(f"\nDataset Statistics:")
print(f"Unique actors: {df_metadata['actor_id'].nunique()}")
print(f"Unique emotions: {df_metadata['emotion_label'].nunique()}")
print(f"Gender distribution:")
print(df_metadata['gender'].value_counts())
print(f"\nEmotion distribution:")
emotion_counts = df_metadata['emotion_label'].value_counts()
print(emotion_counts)

# Plot dataset distribution
plt.figure(figsize=(12, 8))
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Emotion distribution
ax1 = axes[0, 0]
emotion_counts.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title('Distribution of Emotion Classes', fontsize=14, fontweight='bold')
ax1.set_xlabel('Emotion', fontsize=12)
ax1.set_ylabel('Count', fontsize=12)
ax1.tick_params(axis='x', rotation=45)

# Gender distribution
ax2 = axes[0, 1]
gender_counts = df_metadata['gender'].value_counts()
gender_counts.plot(kind='pie', ax=ax2, autopct='%1.1f%%', colors=['lightcoral', 'lightblue'])
ax2.set_title('Gender Distribution', fontsize=14, fontweight='bold')
ax2.set_ylabel('')

# Actor-wise distribution
ax3 = axes[1, 0]
actor_counts = df_metadata['actor_id'].value_counts().sort_index()
actor_counts.plot(kind='bar', ax=ax3, color='lightgreen', width=0.8)
ax3.set_title('Samples per Actor', fontsize=14, fontweight='bold')
ax3.set_xlabel('Actor ID', fontsize=12)
ax3.set_ylabel('Number of Samples', fontsize=12)
ax3.tick_params(axis='x', rotation=0)

# Intensity distribution
ax4 = axes[1, 1]
intensity_counts = df_metadata['intensity'].value_counts().sort_index()
intensity_counts.plot(kind='bar', ax=ax4, color='gold')
ax4.set_title('Intensity Level Distribution', fontsize=14, fontweight='bold')
ax4.set_xlabel('Intensity Level', fontsize=12)
ax4.set_ylabel('Count', fontsize=12)

plt.tight_layout()
plt.savefig('dataset_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
print("Dataset distribution plot saved as 'dataset_distribution.png'")

# Prepare data for model
filepaths = df_metadata['filepath'].tolist()
labels = df_metadata['emotion_label'].tolist()
actor_ids = df_metadata['actor_id'].tolist()
genders = df_metadata['gender'].tolist()

print("\n" + "="*60)
print("DATASET SUMMARY FOR PUBLICATION")
print("="*60)
print(f"Total Samples: {len(filepaths)}")
print(f"Number of Actors: {len(set(actor_ids))}")
print(f"Number of Emotion Classes: {len(set(labels))}")
print(f"Classes: {sorted(set(labels))}")
print(f"Average samples per class: {len(filepaths)/len(set(labels)):.1f}")
print("="*60)

# Save metadata to CSV
df_metadata.to_csv('ravdess_metadata.csv', index=False)
print("\nMetadata saved to 'ravdess_metadata.csv'")

print("\n[COMPLETE] Dataset loading and analysis complete!")
print("\nNext steps: Run the feature extraction and model training...")
