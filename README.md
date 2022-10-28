# Rainy word Socket Server
[![Dockerhub](https://img.shields.io/docker/automated/yuuhatevim/rainyword)](https://hub.docker.com/r/yuuhatevim/rainyword)

Table of Contents
- [Reminder](#reminder)
- [Running Docker Image](#run-docker-container)
- [Developing Docker Image](#developing-with-docker-image)
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
`docker run -p 6969:6969 yuuhatevim/rainyword:test`

Remove your test image
`docker rmi yuuhatevim/rainyword:test`

## TODO Lists
1. typed_word.py
2. expired_word.py

## Sender JSON Format
__lobby.py__

return
```json
{
    "Player": [
        {"ID":1, "Point":0},
        {"ID":2, "Point":0}
    ]
}
```

__word_list.py__

return
```json
{
    "word": [
        "word0",
        "word1",
        "word2",
        "word3",
        "word4",
    ]
}
```

__typed_word.py__

return point(ID:1,Point:1)
```json
{
    "point": [1,1]
}
