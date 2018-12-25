from isanlp.processor_udpipe import ProcessorUDPipe
from isanlp import PipelineCommon

PPL_UDPIPE = PipelineCommon([(ProcessorUDPipe('/src/parser_UDPIPE/russian-ud-2.0-170801.udpipe'),
                              ['morph'],
                              {'tokens' : 'tokens',
                               'sentences' : 'sentences',
                               'lemma': 'lemma',
                               'postag' : 'postag',
                               'morph' : 'morph',
                               'synt_dep_tree' : 'synt_dep_tree'}
                             )],
                            name='default')
