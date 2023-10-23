# COVID-Detection
A machine learning based approach to detect COVID cases from X-ray scans of abdominal/chest region of the suspected patient.

## Dataset
The dataset is derived from multiple sources that provided with the images of chest X-rays of COVID affected, normal pneumoniac and healthy people. The sources are cited below.
1. https://github.com/ieee8023/covid-chestxray-dataset
2. https://sirm.org/category/senza-categoria/covid-19/
3. https://github.com/armiro/COVID-CXNet
4. https://eurorad.org/

Preprocessing - 
Resizing and grey-coding of the image data to ensure uniformity
Conversion of images to pixel value data
Dimensionality reduction using PCA and ICA

The model employs Supervised Learning techniques to make predictions regarding the COVID infection status of an individual by analyzing the pixel data extracted from X-ray scans specifically focused on the chest area. The algorithms implemented are -
1. Gaussian Naive Bayes
2. Decision Tree Classifier
3. Random Forest Classifier
4. XGBoost
5. SVM (kernel functions varied)

After conducting the implementations, a comparative analysis of these models was performed, considering the results obtained. The highest achieved testing accuracy approaches an impressive 98%, demonstrating its exceptional performance in real-world scenarios.

## Setup
Create new Python environment
```
conda create -n pyenv python=3.9
```
Activate the environment.
```
conda activate pyenv
```

## Libraries
Navigate to the project directory in your terminal.
```
pip install -r requirements.txt
```
