ARG USER=flask
ARG HOME="/home/$USER"
ARG VENV="$HOME/venv"

FROM python:3.9-alpine3.14 as base
FROM base as builder
ARG VENV
RUN apk --update --no-cache add python3-dev libffi-dev gcc musl-dev make libevent-dev build-base
RUN python3 -m venv $VENV
ENV PATH="$VENV/bin:$PATH"
COPY app/requirements.txt /requirements.txt
RUN pip install --no-cache-dir  -r /requirements.txt

FROM base
ARG USER
ARG HOME
ARG VENV
RUN adduser -S $USER
COPY --from=builder $VENV $VENV

USER $USER
WORKDIR $HOME
COPY app/ ./app/

EXPOSE 5000

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=$VENV
ENV PATH="$VENV/bin:$PATH"
ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
CMD ["flask", "run", "--host", "0.0.0.0"]
