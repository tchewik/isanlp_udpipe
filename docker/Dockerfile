FROM inemo/isanlp

# install UDPipe
RUN pip install -U pip
RUN pip install ufal.udpipe

ENV PARSER_UDPIPE=/src/parser_UDPIPE/
COPY models.tar.gz $PARSER_UDPIPE
RUN cd $PARSER_UDPIPE && tar -xf models.tar.gz

COPY pipeline_object.py /src/parser_UDPIPE/src/pipeline_object.py
ENV PYTHONPATH=/src/parser_UDPIPE/src/

CMD [ "python", "/start.py", "-m", "pipeline_object", "-a", "PPL_UDPIPE" ]
