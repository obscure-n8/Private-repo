FROM ssbots/ssbots_heroku:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

# Install FFmpeg and create symlink for YT-DLP
RUN apt-get update && apt-get install -y ffmpeg && \
    ln -sf /usr/bin/ffmpeg /bin/mediaforge && \
    ln -sf /usr/bin/ffmpeg /usr/local/bin/ffmpeg

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]
