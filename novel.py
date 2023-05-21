import random
import json

def generate_novel():
    with open('words.json', encoding='utf-8') as file:
        data = json.load(file)

    opening = data['opening']
    characters = data['characters']
    conflicts = data['conflicts']
    resolutions = data['resolutions']
    endings = data['endings']

    opening_sentence = random.choice(opening)
    character = random.choice(characters)
    conflict_sentence = random.choice(conflicts)
    resolution_sentence = random.choice(resolutions)
    ending_sentence = random.choice(endings)

    novel = opening_sentence + " Poznajemy " + character + ", który wraz z towarzyszami " + conflict_sentence + " Razem przemierzą niezwykły świat i odkryją nieznane dotąd tajemnice. " + resolution_sentence + " " + ending_sentence

    return novel

print(generate_novel())
