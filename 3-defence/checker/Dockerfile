FROM ubuntu:20.04

ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /checker

ENV PATH "$PATH:/checker"

RUN apt update && apt-get install -y gnupg wget curl unzip --no-install-recommends

RUN wget -q http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_111.0.5563.64-1_amd64.deb -O /tmp/google-chrome-stable.deb && apt install -y /tmp/google-chrome-stable.deb

RUN CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && wget -q --continue -P ./ "http://chromedriver.storage.googleapis.com/$DRIVERVER/chromedriver_linux64.zip" && unzip ./chromedriver* -d . && rm ./chromedriver_linux64.zip

RUN apt install -y python3 python3-pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY src /checker/src
COPY run.sh . 
RUN chmod +x run.sh

ENTRYPOINT ["./run.sh"]
