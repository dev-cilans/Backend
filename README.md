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
# Returns video transcript for specified video.
$ curl "http://localhost/score/transcripts/2DG3pMcNNlw" 
```

```bash
#Returns thumbnails,title, channel-name ,view,time.
$ curl "http://localhost/video/2DG3pMcNNlw" 
```

```bash
#Returns description of video
$ curl "http://localhost/video/2DG3pMcNNlw/description" 
```

```bash
#Returns keywords 
$ curl "http://localhost/video/2DG3pMcNNlw/keywords" 
```
```bash
#Returns document of api.
http://localhost/docs
#Alternative API documentation
http://localhost/redoc
```
## API Reference
https://app.swaggerhub.com/apis-docs/youtubenlp/backend/0.0.1