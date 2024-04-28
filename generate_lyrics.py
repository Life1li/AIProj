import argparse
import json
import numpy as np
import pronouncing  # for rhyme and syllable counting

# Set up argument parser
parser = argparse.ArgumentParser(description='Generate rhyming song verses')
parser.add_argument('-m', '--model', type=str, help='Path to the model file', default="all_grams.txt")
parser.add_argument('-len', '--length', type=int, help='Number of stanzas to generate', default=1)
args = parser.parse_args()

def load_model(model_path):
    with open(model_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_rhymes(word):
    rhymes = pronouncing.rhymes(word)
    return rhymes if rhymes else [word]

def generate_line(all_grams, rhyme_word=None, words_limit=7):
    line = []
    words_count = 0
    
    if rhyme_word:
        # Choose a rhyming word from the available rhymes that is also in the model
        rhyme_candidates = [word for word in find_rhymes(rhyme_word) if word in all_grams and all_grams[word] > 0]
        if rhyme_candidates:
            end_word = np.random.choice(rhyme_candidates)
        else:
            end_word = rhyme_word  # fallback if no suitable rhymes found
        
        line.append(end_word)
        all_grams[end_word] -= 1
        words_count += 1

    # Fill the rest of the line up to the word limit
    while words_count < words_limit:
        possible_words = [word for word in all_grams.keys() if all_grams[word] > 0]
        if not possible_words:
            break
        word = np.random.choice(possible_words)
        line.insert(0, word)  # add to the beginning to maintain rhyme at end
        all_grams[word] -= 1
        words_count += 1

    return ' '.join(line)

def generate_stanza(all_grams, words_limit=4):
    # Generate the first two lines with an AABB rhyme scheme
    first_line = generate_line(all_grams, words_limit=words_limit)
    second_line = generate_line(all_grams, rhyme_word=first_line.split()[-1], words_limit=words_limit)
    third_line = generate_line(all_grams, words_limit=words_limit)
    fourth_line = generate_line(all_grams, rhyme_word=third_line.split()[-1], words_limit=words_limit)

    return first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line

if __name__ == '__main__':
    model_path = args.model
    num_stanzas = args.length
    all_grams = load_model(model_path)

    stanzas = []
    for _ in range(num_stanzas):
        stanza = generate_stanza(all_grams)
        stanzas.append(stanza)

    # Print all stanzas separated by two new lines for clarity
    print("\n\n".join(stanzas))
