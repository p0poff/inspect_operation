FROM python:3.11

WORKDIR /app

RUN apt update && apt install -y libpq-dev && pip install --no-cache-dir requests pyyaml PyGreSQL

# docker build -t inspect_operation_img .
# docker run -it --name i_operation  -v $(pwd)/src:/app inspect_operation_img /bin/bash
# docker start i_operation
# docker exec i_operation ls -l