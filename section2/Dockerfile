FROM ubuntu:24.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip curl python3-venv

RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip3 install requests

WORKDIR /app
COPY section1/http_checker.py ./ 

CMD ["python3", "http_checker.py"]