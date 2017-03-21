FROM alpine:3.5

ADD . /aws-snapshot-tool

RUN apk update && apk add python-dev py-pip && \
    pip install --upgrade pip && \
    pip install -r /aws-snapshot-tool/requirements.txt && \
    chmod a+x /aws-snapshot-tool/snapshot && \
    cp /aws-snapshot-tool/snapshot /etc/periodic/daily

CMD crond -d 8 -f
