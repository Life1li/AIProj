# Library to auto generate a dataset of artist lyrics from the genius api and generate new songs based on these lyrics using the nlp n-gram model

## Prerequisites
- Python 3.6 or higher
- NumPy package
- `googletrans` package (for translation features)

## Installation
First, clone the repository to your local machine:

pip install numpy
source venv/bin/activate or on windows venv\Scripts\activate
if windows has issues do
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
to activate
venv\Scripts\Activate.ps1

pip install openai lyricsgenius nltk

pip install googletrans==4.0.0-rc1

python create_dataset_genuis.py
after generating the artist.json file

python train.py --input-dir data --model all_grams.txt
after createing the all_grams.txt file
if error/empty I have added a all_grams file in data.zip move to under AIProj directory and then generate

python generate.py
