FROM python:3.10.8 as builder
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
COPY needed_pkgs/Log_Handler-1.0-py3-none-any.whl /app/needed_pkgs/
RUN pip install needed_pkgs/Log_Handler-1.0-py3-none-any.whl

RUN pytest

EXPOSE 8000
CMD ["python", "app.py"]