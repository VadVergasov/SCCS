FROM python:3-slim

LABEL org.opencontainers.image.authors="vadim.vergasov2003@gmail.com"

COPY requirements.txt /program/
WORKDIR /program

RUN pip install --no-cache-dir -r requirements.txt

COPY . /program/

VOLUME ["/program/data"]

CMD ["python", "/program/main.py"]
