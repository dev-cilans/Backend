# Backend
Backend for youtubnlp.com
![ytnlp-architecture](https://user-images.githubusercontent.com/31156696/89206709-4aedba00-d5d7-11ea-9b9c-b7ec6ad23a45.png)

## Prerequisites
- Docker
- Git

## Setup
```bash
# Get repository
$ git clone https://github.com/YouTubeNLP/Backend.git
$ cd Backend/
```
```bash
# Create ynlp image
$ docker build --tag ynlp .
# Create backend container
$ docker run --detach --name backend --publish 80:80 ynlp
 ```

## Examples
| Environment | Example 
| - | - 
| `Development` | `http://localhost:80`
| `Production` | `https://youtubenlp.us-south.cf.appdomain.cloud`

```bash
$ # All service endpoints
$ curl "http://localhost:80/"
$ curl "https://youtubenlp.us-south.cf.appdomain.cloud/"
```

| Parameter | Example 
| - | - 
| `video_id` | `1ylleTbizgU`

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

## API Reference
https://app.swaggerhub.com/apis-docs/youtubenlp/backend/0.0.1