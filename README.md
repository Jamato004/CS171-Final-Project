# 27-Class Sign Language Recognition

CNN-based classifier for 27 ASL hand gestures, trained on the [27-Class Sign Language Dataset](https://www.kaggle.com/datasets/ardamavi/27-class-sign-language-dataset) by Arda Mavi.

**CS171-01 — Introduction to Machine Learning**  
Noah Jones, Jacob Timoteo, Chase Potter

---

## Results

| Model | Test Accuracy | Test Loss | Epochs |
|-------|:---:|:---:|:---:|
| Custom CNN | 86.14% | 0.4013 | 72 |
| ResNet50 (fine-tuned) | 96.01% | 0.1979 | 20 |

---

## Project Structure

```
CS171-Final-Project/
├── data/               # Dataset files (gitignored — download separately)
├── models/             # Saved .keras model files (gitignored — download from Drive)
├── notebooks/
│   └── sign_language_cnn.ipynb
├── results/
│   ├── training_history.json
│   └── resnet50_history.json
├── src/
│   └── load_dataset.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Setup

**1. Install dependencies**
```bash
pip install tensorflow kagglehub numpy scikit-learn matplotlib pillow
```

**2. Download the dataset**
```bash
python src/load_dataset.py
```
This downloads `X.npy` and `Y.npy` into `data/`.

**3. Download large files from Google Drive**

The following files are too large for GitHub — download them and place in the correct folders:

| File | Folder | Link |
|------|--------|------|
| `X_train.npy` | `data/` | [Google Drive](https://drive.google.com/drive/folders/1DLyvWdAKw32bnVdOFVQx3sfcegathm7f) |
| `X_test.npy` | `data/` | [Google Drive](https://drive.google.com/drive/folders/1DLyvWdAKw32bnVdOFVQx3sfcegathm7f) |
| `resnet50.keras` | `models/` | [Google Drive](https://drive.google.com/drive/folders/1DLyvWdAKw32bnVdOFVQx3sfcegathm7f) |

**4. Open the notebook**
```bash
cd notebooks
jupyter notebook sign_language_cnn.ipynb
```

---

## Running the Notebook

The notebook has two modes:

**Skip training (recommended)** — Run **Section 7.1** to load the saved model and data, then jump straight to evaluation (Section 8+).

**Run training from scratch** — Skip Section 7.1 and run sections 1–7 in order. Training the custom CNN takes ~3.2 hours on CPU. GPU strongly recommended.

---

## Dataset

- **Source:** [Kaggle — 27 Class Sign Language Dataset](https://www.kaggle.com/datasets/ardamavi/27-class-sign-language-dataset)
- **Size:** 22,801 images across 27 classes
- **Participants:** 173 individuals
- **Classes:** Digits 0–9, letters a–e, phrases (hello, yes, no, please, bye, good, good morning, little bit, pardon, project, whats up), and NULL
- **Format:** 128×128 RGB images, pixel values normalized to [0, 1]
