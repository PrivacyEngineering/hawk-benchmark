FROM python:3.9.16
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt update && apt install nano
COPY . .
ENTRYPOINT ["tail", "-f", "/dev/null"]