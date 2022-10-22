# Rainy word Socket Server
[![Dockerhub](https://img.shields.io/docker/automated/yuuhatevim/rainyword)](https://hub.docker.com/r/yuuhatevim/rainyword)

Table of Contents
- [Reminder](#reminder)
- [Running Docker Image](#run-docker-container)
- [TODO](#todo-lists)

Everything can be config inside the config file.

The default settings is *localhost* with port *6969*.

## Reminder
Please dont push to the master respository. Just make a pull request and I will manually merge it together.<br>
As this code is continous integrate to Dockerhub.

## Run docker container
`docker run -p 6969:6969 yuuhatevim/rainyword:<tag>`

## Developing with Docker image
`docker build -t yuuhatevim/rainyword:test .`
Run your image as a container
`docker run -p 6969:6969 yuuhatevim/rainyword:test
Remove your test image
`docker rmi yuuhatevim/rainyword:test

## TODO Lists
1. Word List implementation
2. Server can force close client