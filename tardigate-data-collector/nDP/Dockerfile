FROM node:alpine

WORKDIR /usr/src/app

RUN apk add --update py-pip && apk add py3-setuptools

RUN npm i nodemon

COPY package.json package.json

RUN npm install

COPY . .

EXPOSE 3000

CMD ["./node_modules/nodemon/bin/nodemon.js","data_collector1"]

