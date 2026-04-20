ARG RASA_SDK_VERSION=3.15.1
FROM rasa/rasa-sdk:${RASA_SDK_VERSION}

COPY actions /app/actions
COPY db /app/db

USER root
# install required packages
RUN pip install -U pip
RUN pip install --no-cache-dir -r /app/actions/requirements.txt

USER 1001
CMD ["start", "--actions", "actions"]