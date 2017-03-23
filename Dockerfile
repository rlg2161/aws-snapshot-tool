FROM alpine:3.5

ADD . /aws-snapshot-tool

RUN apk update && apk add python-dev py-pip curl && \
    pip install --upgrade pip && \
    pip install -r /aws-snapshot-tool/requirements.txt && \
    chmod +x /aws-snapshot-tool/bin/snapshot-daily && \
    cp /aws-snapshot-tool/bin/snapshot-daily /etc/periodic/daily

CMD crond -d 8 -f
