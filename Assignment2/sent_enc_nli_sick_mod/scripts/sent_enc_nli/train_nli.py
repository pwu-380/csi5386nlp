import numpy
import os

from nli import train

if __name__ == '__main__':
    model_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
    train(
    saveto           = './{}.npz'.format(model_name),
    reload_          = True,
    dim_word         = 300,
    dim              = 300,
    patience         = 3,
    n_words          = 2260,
    decay_c          = 0.,
    clip_c           = 10.,
    lrate            = 0.0004,
    optimizer        = 'adadelta',
    maxlen           = 100,
    batch_size       = 32,
    valid_batch_size = 32,
    dispFreq         = 10,
    validFreq        = 1000,
    saveFreq         = 1000,
    use_dropout      = True,
    verbose          = False,
    datasets         = ['../../data/word_sequence/premise_SICK_train2.txt.tok',
                        '../../data/word_sequence/hypothesis_SICK_train2.txt.tok',
                        '../../data/word_sequence/label_SICK_train2.txt'],
    valid_datasets   = ['../../data/word_sequence/premise_SICK_trial2.txt.tok',
                        '../../data/word_sequence/hypothesis_SICK_trial2.txt.tok',
                        '../../data/word_sequence/label_SICK_trial2.txt'],
    test_datasets    = ['../../data/word_sequence/premise_SICK_test_annotated2.txt.tok',
                        '../../data/word_sequence/hypothesis_SICK_test_annotated2.txt.tok',
                        '../../data/word_sequence/label_SICK_test_annotated2.txt'],
    dictionary       = '../../data/word_sequence/vocab_cased.pkl',
    # embedding        = '../../data/glove/glove.840B.300d.txt',
    )


