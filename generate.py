import argparse
import json
import re
import numpy as np
from googletrans import Translator

# Setup argument parser
parser = argparse.ArgumentParser(description='Get text from model')
parser.add_argument('-m', '--model', type=str, help='path to the file from which the model is loaded.',
                    default="all_grams.txt")
parser.add_argument('-pre', '--prefix', nargs='+',
                    help='optional argument. The beginning of the sentence (one or more words). If not specified, '
                         'select the start word randomly from all words.',
                    default=None)
parser.add_argument('-len', '--length', type=int, help='length of the generated sequence.', default=20)
args = parser.parse_args()

def translate_text(text, dest_language="en"):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

def clear_prefix(text):
    text = re.sub(r'[^\w\s]+|[\d]+', r'', text).strip()
    text = text.strip()
    text = text.lower()
    text = text.replace('\n', ' ')
    return text

def separate_grams(all_grams):
    one_grams = {}
    two_grams = {}
    three_grams = {}
    for gram in all_grams.keys():
        if len(gram.split(' ')) == 1:
            one_grams[gram] = all_grams[gram]
        elif len(gram.split(' ')) == 2:
            two_grams[gram] = all_grams[gram]
        elif len(gram.split(' ')) == 3:
            three_grams[gram] = all_grams[gram]
    return one_grams, two_grams, three_grams

def make_text(all_grams, length, prefix=None):
    one_grams, two_grams, three_grams = separate_grams(all_grams)
    words = list(one_grams.keys())

    arr = []
    if prefix is None or prefix == "":
        arr = np.random.choice(list(two_grams.keys()), 1)[0].split(' ')
    else:
        prefix = clear_prefix(' '.join(prefix))  # Corrected prefix handling
        arr = prefix.split(" ")
        if len(arr) == 1:
            p_arr = []
            for word in words:
                if arr[-1] + " " + word in two_grams.keys():
                    p_arr.append(two_grams[arr[-1] + " " + word] / one_grams[arr[-1]])
                else:
                    p_arr.append(0)
            if sum(p_arr) == 0:
                arr += np.random.choice(list(two_grams.keys()), 1)[0].split(' ')
            else:
                p_arr /= np.sum(p_arr)
                arr.append(np.random.choice(words, 1, p=p_arr)[0])

    for j in range(length - len(arr)):
        p_arr = []
        for word in words:
            if arr[-2] + " " + arr[-1] + " " + word in three_grams.keys():
                p_arr.append(three_grams[arr[-2] + " " + arr[-1] + " " + word] / two_grams[arr[-2] + " " + arr[-1]])
            else:
                p_arr.append(0)
        if np.sum(p_arr) == 0:
            arr += np.random.choice(list(two_grams.keys()), 1)[0].split(' ')
        else:
            p_arr /= np.sum(p_arr)
            arr.append(np.random.choice(words, 1, p=p_arr)[0])

    # Generate the text
    generated_text = " ".join(arr)

    # Translate the generated text
    translated_text = translate_text(generated_text, "en")

    # Print both original and translated text
    print("Original:", generated_text)
    print("Translated:", translated_text)

if __name__ == '__main__':
    model = args.model
    with open(model, 'r', encoding='utf-8') as file:
        all_grams = json.load(file)

    length = args.length
    prefix = args.prefix  # Prefix is now correctly handled within make_text
    make_text(all_grams, length, prefix)