# Backend
Backend for https://youtubenlp.com
![ytnlp-architecture](https://user-images.githubusercontent.com/31156696/89206709-4aedba00-d5d7-11ea-9b9c-b7ec6ad23a45.png)

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

| Environment | Host 
| - | - 
| `Development` | `http://localhost:8000`
| `Staging` | `https://youtubenlp.us-south.cf.appdomain.cloud`
| `Production` | `https://api.youtubenlp.com`

```bash
$ # All service endpoints
$ curl "http://localhost:8000/" # development
$ curl "https://youtubenlp.us-south.cf.appdomain.cloud/" # staging
$ curl "api.youtubenlp.com/" # production (under construction)
```

---

## Examples

| Parameter | Example Value
| - | - 
| `video_id` | `1ylleTbizgU`
| `environment` | `localhost`

```bash
$ # transcript_service
$ # Returns list of transcripts from video
$ curl "{environment}/transcripts/{video_id}"
```
```bash
$ # comment_service
$ # Returns list of comments from video
$ curl "{environment}/comments/{video_id}"
```
```bash
$ # video_service details
$ # Returns various details related to video
$ curl "{environment}/video/{video_id}"
```
```bash
$ # video_service description
$ # Returns the description text of the video
$ curl "{environment}/video/{video_id}/description"
```
```bash
$ # video_service keywords
$ # Returns a list of keywords related to video
$ curl "{environment}/video/{video_id}/keywords"
```
```bash
$ # ner_service 
$ # Returns Name Entity Recognition
$ curl "{environment}/ner/{video_id}"
```

