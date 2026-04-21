import os
import shutil
import kagglehub
 
DATASET = "ardamavi/27-class-sign-language-dataset"
OUT_DIR = "data"
 
 
def main():
    print("Downloading dataset...")
    cache_path = kagglehub.dataset_download(DATASET)
    print(f"Cached at: {cache_path}")
 
    os.makedirs(OUT_DIR, exist_ok=True)
 
    for fname in ("X.npy", "Y.npy"):
        src = os.path.join(cache_path, fname)
        dst = os.path.join(OUT_DIR, fname)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
            print(f"Copied {fname} → {OUT_DIR}/")
        else:
            print(f"Warning: {fname} not found in {cache_path}")
 
    print("Done!")
 
 
if __name__ == "__main__":
    main()