# -*- coding: utf-8 -*-

from coaster.views import jsonp, requestargs
from .. import app
import nltk


@app.route('/1/nlp/tag', methods=['POST'])
@requestargs('text', 'lang')
def nlp_extract_tags(text, lang=None):
    '''returns list of named entities'''
    
    sample = text
    
    sentences = nltk.sent_tokenize(sample)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)
     
    def extract_entity_names(t):
        entity_names = []
        
        if hasattr(t, 'node') and t.node:
            if t.node == 'NE':
                entity_names.append(' '.join([child[0] for child in t]))
            else:
                for child in t:
                    entity_names.extend(extract_entity_names(child))
                    
        return entity_names
     
    entity_names = []
    for tree in chunked_sentences:
        # Print results per sentence
        # print extract_entity_names(tree)
        
        entity_names.extend(extract_entity_names(tree))
     
    # Print all entity names
    #print entity_names
     
    # Print unique entity names
    result = {'tags': list(set(entity_names))}

    return jsonp({'status': 'ok', 'result': result})
