FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
RUN curl -fsSL https://bun.sh/install | bash
# Instalar Node.js
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
RUN reflex init
CMD ["reflex", "run", "--env", "prod"]
EXPOSE 8005 3005