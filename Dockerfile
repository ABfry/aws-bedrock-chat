FROM python:3.11.5-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /src
COPY ./app ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements_base.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
