# This project uses a Python script to generate song lyrics based on a trained language model. The script `generate_lyrics.py` can be customized to generate lyrics of varying lengths and styles, depending on the input model and parameters provided by the user.

## Prerequisites
- Python 3.6 or higher
- NumPy package
- `googletrans` package (for translation features if needed)

## Installation
First, clone the repository to your local machine(my terminal was wsl):
then extract the data.zip file

pip or pip3 install numpy
source venv/bin/activate or on windows venv\Scripts\activate
if windows has issues do
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
to activate
venv\Scripts\Activate.ps1

pip3 or pip3 install pronouncing

pip or pip3 install openai lyricsgenius nltk

pip or pip3 install googletrans==4.0.0-rc1

python or python3 create_dataset.py

after generating the artist.json file

python or python3 train_model.py 
after creating the all_grams.txt file
if error/empty I have added a all_grams file in data.zip move to under AIProj directory and then generate

python or python3 generate_lyrics.py
