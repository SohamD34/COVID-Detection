from google.colab import drive
drive.mount('/content/drive')

"""# DATASET"""

combined_dataset = []
Y_values = []

"""## Pneumonia chest scans"""

# Commented out IPython magic to ensure Python compatibility.
%cd /content/drive/MyDrive/COVID-19_Radiography_Dataset/COVID-19_Radiography_Dataset/Viral Pneumonia/images

''' STORING THE IMAGES OF CHEST SCANS FOR PNEUMONIA  '''

files = os.listdir('.')
image_files = []

for file in files:
    if file.endswith(('jpg', 'jpeg', 'png', 'bmp')):
        image_files.append(file)

image_list = []
for image_file in image_files:
    img = Image.open(image_file).convert('L')
    resized_img = img.resize((250, 250))
    img_array = np.array(resized_img)
    image_list.append(img_array)
    img = None
    img_array = None

pneumonia_imgs = image_list
combined_dataset.extend(pneumonia_imgs)

for i in range(len(pneumonia_imgs)):
    Y_values.append(0)
pneumonia_imgs = None
image_list = None

# Commented out IPython magic to ensure Python compatibility.
%rm -rf /content/drive/MyDrive/COVID-19_Radiography_Dataset/COVID-19_Radiography_Dataset/Viral Pneumonia

"""## COVID datasets"""

df = pd.read_excel('/content/drive/MyDrive/COVID-19_Radiography_Dataset/COVID-19_Radiography_Dataset/COVID.metadata.xlsx')
urls = list(df['URL'])
uniq_urls = list(set(urls))

!git clone https://github.com/ieee8023/covid-chestxray-dataset.git

!git force clone https://github.com/armiro/COVID-CXNet

!wget https://sirm.org/category/senza-categoria/covid-19/

!wget https://eurorad.org/

"""## Checking and combining all the dataset sources"""

# Commented out IPython magic to ensure Python compatibility.
%cd /content/COVID-CXNet/chest_xray_images/covid19

# Commented out IPython magic to ensure Python compatibility.
%cd /content/covid-chestxray-dataset/images

# Commented out IPython magic to ensure Python compatibility.
%cd /content/drive/MyDrive/COVID-19_Radiography_Dataset/COVID-19_Radiography_Dataset/COVID-19 Dataset/X-ray/COVID

files = os.listdir('.')
image_files = [file for file in files if file.endswith(('jpg', 'jpeg', 'png', 'bmp'))]

image_list = []
for image_file in image_files:
    if len(image_list)<1000:
        img = Image.open(image_file).convert('L')
        resized_img = img.resize((250, 250))
        img_array = np.array(resized_img)
        image_list.append(img_array)
        img = None
        resized_img = None
        img_array = None
    else:
        break

radiology_array = image_list
combined_dataset.extend(radiology_array)
for i in range(len(radiology_array)):
    Y_values.append(1)
image_list = None

# Commented out IPython magic to ensure Python compatibility.
%rm -rf /content/drive/MyDrive/COVID-19_Radiography_Dataset/COVID-19_Radiography_Dataset/COVID-19 Dataset/X-ray/COVID

# Commented out IPython magic to ensure Python compatibility.
%cd /content/drive/MyDrive/SIRM Xrays

files = os.listdir('.')
image_files = [file for file in files if file.endswith(('jpg', 'jpeg', 'png', 'bmp'))]

image_list = []
for image_file in image_files:
    if len(image_list)<1000:
        img = Image.open(image_file).convert('L')
        resized_img = img.resize((250, 250))
        img_array = np.array(resized_img)
        image_list.append(img_array)
        img = None
        resized_img = None
        img_array = None
    else:
        break

sirm_array = image_list
combined_dataset.extend(sirm_array)
for i in range(len(sirm_array)):
    Y_values.append(1)
image_list = None
