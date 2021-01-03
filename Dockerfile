FROM python:3

WORKDIR /site

COPY ./src/requirements.txt ./src/site ./

RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN mkdir /root/fakenotes

EXPOSE 5000

CMD ["flask", "run","-h", "0.0.0.0"]
