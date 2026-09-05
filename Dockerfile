FROM ssbots/ssbots_heroku:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && \
    ln -sf /usr/bin/ffmpeg /bin/mediaforge

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]
