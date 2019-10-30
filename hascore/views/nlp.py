# -*- coding: utf-8 -*-

import nltk

from coaster.views import jsonp, requestargs

from .. import app


@app.route('/1/nlp/tag', methods=['GET', 'POST'])
@requestargs('text', 'lang')
def nlp_extract_tags(text, lang=None):
    """
    Return a list of tags extracted from provided text.
    """

    sentences = nltk.sent_tokenize(text)
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
        entity_names.extend(extract_entity_names(tree))

    result = {'tags': list(set(entity_names))}

    return jsonp({'status': 'ok', 'result': result})
