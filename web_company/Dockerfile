FROM python:3

WORKDIR /scrapy
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "scrapy", "crawl", "yellow"]
#, "-o", "Data_crawl/test_docker.csv" ]

