# Devanagari_Numerals_Recognition_System

## Abstract
This project, **"Devanāgarī Numerals Recognition System"**, developed by Umang Goswami, aims to create a robust and reliable system for the recognition of Devanāgarī numerals. The is to develop a highly accurate and efficient Devanāgarī numeral recognition system that can be seamlessly integrated into a wide range of applications, ultimately enhancing the processing and management of Devanāgarī-based data.
The system leverages state-of-the-art machine learning algorithms to accurately identify hand-written Devanāgarī numerals, enabling highly efficient and precise data processing in various applications that necessitate Devanāgarī numeral recognition. These applications span diverse domains, including document processing, financial data analysis, and information extraction from Devanāgarī-based documents. 
By harnessing advanced computational techniques, this innovative system promises to significantly enhance the accuracy and productivity of tasks involving Devanāgarī numeral recognition, contributing to improved data management and analysis across various industries and research fields. 
## Technologies Used
The Devanāgarī Numerals Recognition System utilizes a combination of advanced machine learning techniques and image processing algorithms to achieve high-accuracy recognition of Devanāgarī numerals. Specifically, the system employs Convolutional Neural Networks as the primary deep learning architecture for image classification.
The neural networks are trained on a large and diverse dataset of Devanāgarī numeral images, comprising a total of 26,500 samples. This extensive training enables the system to learn the distinctive features and patterns associated with each numeral, allowing for highly accurate recognition of hand-written Devanāgarī numerals. The system's performance has been extensively evaluated, demonstrating its robustness and reliability in a variety of real-world applications.
In brief various technologies used for the development of the aforementioned project are as follows:
- **IDE:** Pycahrm 2024.1 (Professional Edition)
- **Programming Language:** Python v. 3.12
- **Various Libraries used:** `scikit-learn`, `OpenCV`, `TensorFlow`, `NumPy`, `SciPy`, `Keras`, `pillow`, etc. For the complete list of libraries use see `requirements.txt`
Specifications of the computer systems used for development of the project are: 
- **Processor:** 12th Gen Intel(R) Core(TM) i7-12650H @ 2.30 GHz
- **Installed RAM:** 16.0 GB (15.7 GB usable)
- **Internal Storage:** 1 GB SSD
- **System type:** 64-bit operating system, x64-based processor
- **OS:** Windows 11 Home Single Language,  version 23H2
## All Libraries used – requirements.txt
`absl-py==2.1.0`
`astunparse==1.6.3`
`blinker==1.9.0`
`certifi==2024.8.30`
`charset-normalizer==3.4.0`
`click==8.1.7`
`colorama==0.4.6`
`Flask==3.1.0`
`Flask-Cors==5.0.0`
`flatbuffers==24.3.25`
`gast==0.6.0`
`google-pasta==0.2.0`
`grpcio==1.68.1`
`h5py==3.12.1`
`idna==3.10`
`itsdangerous==2.2.0`
`Jinja2==3.1.4`
`joblib==1.4.2`
`keras==3.7.0`
`libclang==18.1.1`
`Markdown==3.7`
`markdown-it-py==3.0.0`
`MarkupSafe==3.0.2`
`mdurl==0.1.2`
`ml-dtypes==0.4.1`
`namex==0.0.8`
`numpy==2.0.2`
`opencv-python==4.10.0.84`
`opt_einsum==3.4.0`
`optree==0.13.1`
`packaging==24.2`
`protobuf==5.29.1`
`Pygments==2.18.0`
`requests==2.32.3`
`rich==13.9.4`
`scikit-learn==1.5.2`
`scipy==1.14.1`
`setuptools==75.6.0`
`six==1.17.0`
`tensorboard==2.18.0`
`tensorboard-data-server==0.7.2`
`tensorflow==2.18.0`
`tensorflow_intel==2.18.0`
`termcolor==2.5.0`
`threadpoolctl==3.5.0`
`typing_extensions==4.12.2`
`urllib3==2.2.3`
`Werkzeug==3.1.3`
`wheel==0.45.1`
`wrapt==1.1`
## System Requirements
The system requirements for the successful installation and operation of the Devanāgarī Numerals Recognition System are as follows:
### Hardware Requirements:
- **Processor:** The system requires at least an Intel Core i5 processor or an equivalent, with a clock speed of 2.0 GHz or higher. This level of processing power is necessary to handle the computationally intensive tasks involved in the recognition and classification of the Devanāgarī numerals.
- **RAM:** A minimum of 8 GB of RAM is recommended for the smooth operation of the system. This amount of memory ensures that the system can efficiently load and process the large datasets required for training and running the machine learning models.
- **Storage:** The system requires 25 GB of available disk space to accommodate the installation files, the training dataset, and any additional resources needed for the recognition process.
- **Display:** A display with a resolution of 1080p or higher is recommended for optimal visualization and interaction with the system's interface.
### Software Requirements:
- **Operating System:** The Devanāgarī Numerals Recognition System is designed to operate on at least Windows 10 or Windows 11 operating systems, or their equivalent. These modern operating systems provide the necessary software environment and libraries to support the system's functionality.
- **Python:** The system requires Python version 3.12 or higher to be installed, as the codebase and supporting libraries are developed using this programming language. This version of Python ensures compatibility with the latest advancements in machine learning and image processing libraries.
### Dataset used for training
The Devanāgarī Numerals Recognition System was developed using a comprehensive dataset of 26,500 Devanāgarī numeral images. I had modified/restructured the dataset, its file structures as to better suit my project needs and feasibility. The dataset was obtained from the following source:
> Handwritten Devanāgarī characters - vowels and numerals (38,750 isolated images + 9,200 isolated images). (2023). [Dataset]. In Mendeley Data (Version 4). doi:10.17632/pxrnvp4yy8.4 Retrived from https://data.mendeley.com/datasets/pxrnvp4yy8/4 

whose description may be found in the research paper – 

> Prashanth, D. S., Mehta, R. V. K., & Challa, N. P. (2021). A multi-purpose dataset of Devanāgarī script comprising of isolated numerals and vowels. Data in Brief, 40, 107723. https://doi.org/10.1016/j.dib.2021.107723 Retrieved from https://pdf.sciencedirectassets.com/311593/1-s2.0-S2352340921X00078/1-s2.0-S2352340921009987/main.pdf 
## Output
<img width="948" height="449" alt="image" src="https://github.com/user-attachments/assets/0e6e638c-ecfa-4a2b-8d14-d3e7c2179caa" />
<img width="948" height="442" alt="image" src="https://github.com/user-attachments/assets/46120a3d-e70e-4f21-880a-85f688a3c73d" />

## References
> Handwritten Devanāgarī characters - vowels and numerals (38,750 isolated images + 9,200 isolated images). (2023). [Dataset]. In Mendeley Data (Version 4). doi:10.17632/pxrnvp4yy8.4 Retrived from https://data.mendeley.com/datasets/pxrnvp4yy8/4

> Prashanth, D. S., Mehta, R. V. K., & Challa, N. P. (2021). A multi-purpose dataset of Devanāgarī script comprising of isolated numerals and vowels. Data in Brief, 40, 107723. https://doi.org/10.1016/j.dib.2021.107723 Retrived from https://pdf.sciencedirectassets.com/311593/1-s2.0-S2352340921X00078/1-s2.0-S2352340921009987/main.pdf
