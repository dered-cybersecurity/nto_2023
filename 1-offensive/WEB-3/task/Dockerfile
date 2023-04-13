FROM node:latest

ENV PORT=3000

COPY package.json package.json

RUN npm install

COPY health.bash /usr/bin/
COPY . .

EXPOSE 3000

CMD ["npm", "start"]
