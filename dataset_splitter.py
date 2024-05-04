import os
import shutil
import random

# Define directories
source_dir = "C://Users//user//Downloads//capstone gitignore//Roads Kenya"
train_dir = "C://Users//user//Downloads//capstone gitignore//Roads Kenya//train"
val_dir = "C://Users//user//Downloads//capstone gitignore//Roads Kenya//validation"
test_dir = "C://Users//user//Downloads//capstone gitignore//Roads Kenya//test"

# Define label directories
labels = ["good", "fair", "poor", "flooded", "unpaved"]

# Define splitting ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create train, validation, and test directories
for label in labels:
    os.makedirs(os.path.join(train_dir, label), exist_ok=True)
    os.makedirs(os.path.join(val_dir, label), exist_ok=True)
    os.makedirs(os.path.join(test_dir, label), exist_ok=True)

# Function to split files
def split_files(source, train, val, test, ratios):
    files = os.listdir(source)
    random.shuffle(files)
    train_files = files[:int(len(files) * ratios[0])]
    val_files = files[int(len(files) * ratios[0]):int(len(files) * (ratios[0] + ratios[1]))]
    test_files = files[int(len(files) * (ratios[0] + ratios[1])):]
    
    # Copy files to train directory
    for file in train_files:
        shutil.copy(os.path.join(source, file), os.path.join(train, file))
    
    # Copy files to validation directory
    for file in val_files:
        shutil.copy(os.path.join(source, file), os.path.join(val, file))
    
    # Copy files to test directory
    for file in test_files:
        shutil.copy(os.path.join(source, file), os.path.join(test, file))

# Split files for each label
for label in labels:
    source_label_dir = os.path.join(source_dir, label)
    train_label_dir = os.path.join(train_dir, label)
    val_label_dir = os.path.join(val_dir, label)
    test_label_dir = os.path.join(test_dir, label)
    
    split_files(source_label_dir, train_label_dir, val_label_dir, test_label_dir, [train_ratio, val_ratio, test_ratio])
