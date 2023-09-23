FROM python:3.8.5
LABEL maintainer="maximiliano.pizarro.5@gmail.com"
RUN mkdir -p /usr/lib/ckan/default
ADD . /usr/lib/
RUN python3 -m venv /usr/lib/ckan/default
RUN . /usr/lib/ckan/default/bin/activate
WORKDIR /usr/lib/
RUN pip install -r requirements.txt
RUN python setup.py install
CMD ckan -c who.ini run --host 0.0.0.0