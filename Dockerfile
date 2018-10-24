FROM python:alpine3.6

#ADD controller.py /
ENV SERVICE_NAME=similarity-alg

RUN mkdir -p /usr/lib/bizzabo/${SERVICE_NAME}

COPY . /usr/lib/bizzabo/${SERVICE_NAME}

WORKDIR /usr/lib/bizzabo/${SERVICE_NAME}

RUN pip install -r requirements.txt

CMD [ "python", "./controller.py" ]