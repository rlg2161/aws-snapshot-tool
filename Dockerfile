FROM alpine:3.5

ADD . /snapshot

RUN apk update && apk add curl python-dev py-pip && \
    pip install --upgrade pip && \
    pip install -r /snapshot/requirements.txt && \
    chmod a+x /snapshot/snapshot && \
    cp /snapshot/snapshot /etc/periodic/daily

CMD crond -d 8 -f
