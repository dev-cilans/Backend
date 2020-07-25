# Backend


## Prerequisites
- Docker
- Git

```bash
# Setup
$ https://github.com/YouTubeNLP/Backend.git
$ cd Backend/
```

## Setup

```bash
# Create service container
$ docker build --tag fastapi_ynlp .
$ docker run --detach --name fastapi_backend --publish 80:80 fastapi_ynlp
 ```
## Example

```bash
# Try a post request on the comments endpoint.
# Returns the top k comments for video specified in data.json.
$  curl "http://localhost/score/comments" --request POST --header "Content-Type: application/json" --data @data.json
```

```bash
# Try a post request on the transcript endpoint.
# Returns video transcript for specified video.
$ curl "http://localhost/score/transcripts" --request POST --header "Content-Type: application/json" --data @data.json
```
## API Reference
https://app.swaggerhub.com/apis-docs/youtubenlp/backend/0.0.1
