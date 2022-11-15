FROM node:14.0.0-alpine

WORKDIR /code
COPY code .

RUN npm i
RUN npm run postinstall

EXPOSE 3000

ENTRYPOINT [ "npm" ]

CMD ["start"]