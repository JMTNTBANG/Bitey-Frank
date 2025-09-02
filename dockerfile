FROM node:24-alpine3.21

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["./docker-entrypoint.sh"]
