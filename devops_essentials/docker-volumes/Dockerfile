FROM alpine:latest
RUN apk add --no-cache curl
COPY config.txt /app/config.txt
RUN mkdir -p /data
VOLUME [ "/data" ]