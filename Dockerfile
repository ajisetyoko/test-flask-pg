from python:3.10

# Install PostgreSQL Client
RUN apt-get update && apt-get install -y lsb-release && \
    echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && apt-get install -y postgresql && apt-get clean all

COPY requirepments.txt /tmp/requirepments.txt
RUN pip install -r /tmp/requirepments.txt

RUN pip install torch torchvision

WORKDIR /app
COPY /app /app

RUN chmod +x start.sh

CMD ./start.sh