FROM inemo/isanlp

# install UDPipe
RUN pip install -U pip
RUN pip install ufal.udpipe

RUN mkdir /src/parser_UDPIPE && cd /src/parser_UDPIPE && wget -O model.udpipe https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-3131/russian-syntagrus-ud-2.5-191206.udpipe

COPY pipeline_object.py /src/parser_UDPIPE/src/pipeline_object.py
ENV PYTHONPATH=/src/parser_UDPIPE/src/

CMD [ "python", "/start.py", "-m", "pipeline_object"]
