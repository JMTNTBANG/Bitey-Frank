FROM node:24-alpine3.21

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]
