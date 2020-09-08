from isanlp.processor_udpipe import ProcessorUDPipe
from isanlp import PipelineCommon

def create_pipeline(delay_init=False):
    return PipelineCommon([(ProcessorUDPipe('/src/parser_UDPIPE/model.udpipe'),
                              ['morph'],
                              {'tokens' : 'tokens',
                               'sentences' : 'sentences',
                               'lemma': 'lemma',
                               'postag' : 'postag',
                               'morph' : 'morph',
                               'syntax_dep_tree' : 'syntax_dep_tree'}
                             )],
                            name='default')
