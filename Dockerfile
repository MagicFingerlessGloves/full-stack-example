FROM postgres:16

ENV POSTGRES_DB=catsdb
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

COPY create-data.sql /docker-entrypoint-initdb.d/