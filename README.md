# Backend
Backend for https://youtubenlp.com
![ytnlp-architecture](https://user-images.githubusercontent.com/31156696/89206709-4aedba00-d5d7-11ea-9b9c-b7ec6ad23a45.png)

## Directory Structure
```bash
$ tree
.
|-- Dockerfile # build for production
|-- Procfile # init file for ibm cloud
|-- README.md # documentation
|-- requirements.txt # all packages required in the project
|-- runtime.txt # current project python version
|-- spec # api specification
|   `-- swagger.yml # swagger genereate openapi spec
|-- src
|   |-- __init__.py
|   |-- main.py # init point for backend
|   |-- v1 # version 1 of services
|   |   |-- __init__.py
|   |   `-- service # all services
|   |       |-- comment
|   |       |   `-- __init__.py
|   |       |   `-- comment.py
|   |       |-- emotion
|   |       |   `-- __init__.py
|   |       |   `-- emotion.py
|   |       |-- lda
|   |       |   `-- __init__.py
|   |       |   `-- lda.py
|   |       |-- ner
|   |       |   `-- __init__.py
|   |       |   `-- ner.py
|   |       |-- sentiment
|   |       |   `-- __init__.py
|   |       |   `-- sentiment.py
|   |       |-- video # return 
|   |       |   `-- __init__.py
|   |       |   `-- video.py
|   |       `-- world-cloud
|   |           `-- __init__.py
|   |       |   `-- world_cloud.py
|   `-- v2
|       |-- __init__.py
|       `-- service
|           `-- __init__.py
`-- tests # tests/mocks for backend
    |-- integration # integration tests with nlp and frontend repo
    |-- test-requirements.txt # all packages required for project tests 
    `-- unit # sepearte tests for each service

16 directories, 26 files
```

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
$ docker run --detach --name backend --publish 80:80 ynlp
 ```

## Setup (Development)
```bash
# Get repository
$ git clone https://github.com/YouTubeNLP/Backend.git && cd Backend/
# Install all packages locally
# Some kind of virtual environment is recommened like miniconda or virtualenv
(your-env-name) $ pip install -r requirements.txt
# Create backend container
(your-env-name) $ uvicorn main:app
 ```

## Examples
| Environment | Host 
| - | - 
| `Development` | `http://localhost:80`
| `Staging` | `https://youtubenlp.us-south.cf.appdomain.cloud`
| `Production` | `https://api.youtubenlp.com`

```bash
$ # All service endpoints
$ curl "http://localhost:80/" # development
$ curl "https://youtubenlp.us-south.cf.appdomain.cloud/" # staging
$ curl "api.youtubenlp.com/" # production (under construction)
```

| Parameter | Example 
| - | - 
| `video_id` | `1ylleTbizgU`
| `environment` | `http://localhost:80/`

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
