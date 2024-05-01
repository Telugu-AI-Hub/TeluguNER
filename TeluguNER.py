class TeluguNER:
    def __init__(self):
        # Define dictionaries for named entities
        self.named_entities = {
            'person': {'వ్యక్తి', 'వ్యక్తులు', 'వ్యక్తుడు', 'వ్యక్తుల', 'పేరు', 'వ్యక్తిగత'},
            'location': {'అనంతపురం','స్థలం', 'స్థానం', 'లోకేషన్', 'ప్రాంతం', 'ప్రాంతాలు', 'ప్రాంతంలో', 'స్థానము', 'స్థానాలు', 'నగరం'},
            'organization': {'సంస్థ', 'సంస్థలు', 'సంస్థానము', 'సంస్థాలు', 'సంస్థను', 'సంస్థనులు', 'సంస్థని', 'సంస్థనికి'},
            'number': {'ఒకటి', 'రెండు', 'వంద'},
            'misc': {'తెలుగు'}
        }

    def tag_entities(self, tokens):
        entities = []
        for token in tokens:
            for entity_type, entity_set in self.named_entities.items():
                if token in entity_set:
                    entities.append((token, entity_type))
        return entities

if __name__ == "__main__":
    # Initialize NER tagger
    ner_tagger = TeluguNER()

    # Tokenize input sentence
    sentence = "అనంతపురం లో తెలుగు వారి సంస్థ లో వంద మంది నమోదయ్యారు."
    tokens = sentence.split()

    # Tag named entities
    tagged_entities = ner_tagger.tag_entities(tokens)
    print(tagged_entities)
