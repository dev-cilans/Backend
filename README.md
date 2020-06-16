# Backend

This is just a demo

## Prerequisites
- Docker
- Git

```bash
# Setup
$ git clone git@github.com:YouTubeNLP/Backend.git
$ cd Backend/
```

```bash
# Create service container
$ docker build --tag ynlp .
$ docker run --detach \
--name ynlp_demo \
--publish 8080:8080 \
ynlp
```

```bash
$ # Try a post request on this endpoint
$ curl "http://localhost:8080/score" \
--request POST \
--header "Content-Type: application/json" \
--data @data.json
```


