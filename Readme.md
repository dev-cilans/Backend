# Backend
Backend for https://youtubenlp.com
![ytnlp-architecture](https://user-images.githubusercontent.com/31156696/89206709-4aedba00-d5d7-11ea-9b9c-b7ec6ad23a45.png). If you're a developer checkout the [Development Docs](./Development.md).
## Prerequisites
- Docker
- Git

## Setup (Production)
```bash
# Get repository
$ git clone https://github.com/YouTubeNLP/Backend.git && cd Backend/

# Create ynlp image
$ docker build --tag ynlp .

# Create backend container
$ docker run --detach --name ynlp-backend-prod --publish 8000:8000 ynlp
 ```

## API Reference
https://app.swaggerhub.com/apis-docs/youtubenlp/backend/0.0.1

## Examples

| Environment | Host | Example video_id
| - | - | - 
| `Development` | `http://localhost:8000` | `1ylleTbizgU`
| `Staging` | `https://youtubenlp.us-south.cf.appdomain.cloud` | `1ylleTbizgU`
| `Production` | `https://api.youtubenlp.com` | `1ylleTbizgU`

```bash
$ # All service endpoints
$ curl "http://localhost:8000/" # development
$ curl "https://youtubenlp.us-south.cf.appdomain.cloud/" # staging
$ curl "api.youtubenlp.com/" # production (under construction)
```
