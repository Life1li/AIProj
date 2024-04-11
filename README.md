# This project uses a Python script to generate song lyrics based on a trained language model. The script `generate.py` can be customized to generate lyrics of varying lengths and styles, depending on the input model and parameters provided by the user.

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

python create_dataset.py
after generating the artist.json file

python train_model.py --input-dir data --model all_grams.txt
after createing the all_grams.txt file
if error/empty I have added a all_grams file in data.zip move to under AIProj directory and then generate

python generate_lyrics.py
