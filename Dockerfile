FROM python:2.7-alpine
WORKDIR /workspace
COPY . /workspace

# Environment Variables for future use
ENV BOT_TOKEN telegram_bot_token
ENV UPDATE_INTERVAL 300
ENV RESOURCES_PATH /tbot/resources

RUN pip install -r requirements.txt \
	&& mkdir -p tbot \
	&& mv resources tbot 

VOLUME /tbot
CMD  python robotrss.py
