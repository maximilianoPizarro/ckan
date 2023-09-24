FROM python:3.8.5
LABEL maintainer="maximiliano.pizarro.5@gmail.com"
RUN mkdir -p /usr/lib/ckan/default
ADD . /usr/lib/
RUN python3 -m venv /usr/lib/ckan/default
RUN . /usr/lib/ckan/default/bin/activate
WORKDIR /usr/lib/
RUN pip install -r requirements.txt
RUN python setup.py install
#RUN mkdir -p /usr/local/lib/python3.8/site-packages/oauth2
#RUN mv /usr/local/lib/python3.8/site-packages/ckanext/oauth2 /usr/local/lib/python3.8/site-packages/oauth2
CMD ckan -c who.ini run --host 0.0.0.0