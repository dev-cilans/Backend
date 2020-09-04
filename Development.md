



## Directory Structure
```bash
$ find . -type d -name  "__pycache__" -exec rm -r {} +
$ tree
.
|-- AUTHORS # project auhors for github.com/YouTubeNLP/Backend
|-- CHANGELOG # documentation update for new changes
|-- Dockerfile # docker image for production
|-- Procfile # init file for ibm cloud
|-- README.md # documentation
|-- client_secret_357836004333-pjm620fvcjukarm238q5va992hcv1n6b.apps.googleusercontent.com.json
|-- requirements.txt # all packages required in the project
|-- runtime.txt # current project python version
|-- setup.py # setup current project
|-- spec # openapi-3.0 specification
|   `-- swagger.yml
|-- src
|   |-- main.py # entrypoint for server
|   |-- routes.py
|   |-- settings.py
|   |-- v1
|   |   |-- __init__.py
|   |   `-- service
|   |       |-- Comment
|   |       |   |-- __init__.py
|   |       |   |-- comment.py
|   |       |   `-- comment_downloader.py
|   |       |-- Emotion
|   |       |   |-- __init__.py
|   |       |   `-- emotion.py
|   |       |-- Lda
|   |       |   |-- __init__.py
|   |       |   `-- lda.py
|   |       |-- Ner
|   |       |   |-- __init__.py
|   |       |   `-- ner.py
|   |       |-- Sentiment
|   |       |   |-- __init__.py
|   |       |   `-- sentiment.py
|   |       |-- Transcript
|   |       |   |-- __init__.py
|   |       |   `-- transcript.py
|   |       |-- Video
|   |       |   |-- __init__.py
|   |       |   `-- video.py
|   |       |-- WordCloud
|   |       |   |-- __init__.py
|   |       |   `-- word_cloud.py
|   |       `-- __init__.py
|   `-- v2
|       `-- __init__.py
`-- tests # tests/mocks
    |-- integration # integration tests with nlp and frontend repo
    |-- test-requirements.txt # all packages required for testing
    `-- unit # sepearte tests for each service
        |-- async_test_using_multithreading.py
        |-- test_main.py
        `-- test_response
            |-- keywords_response.txt
            |-- root_response.txt
            |-- video_description.txt
            |-- video_details.txt
            `-- video_transcript.txt

17 directories, 41 files
```

## Setup (Development)
```bash
# Get repository
$ git clone https://github.com/YouTubeNLP/Backend.git && cd Backend/
# Install all packages locally
# Some kind of virtual environment is recommened like miniconda or virtualenv
(your-env-name) $ pip install -r dev-requirements.txt
# Install spacy models
(your-env-name) $ python -m spacy download en_core_web_sm
# Create backend container
(your-env-name) $ uvicorn src.main:app --host=0.0.0.0 --reload
 ```
*Project is served at http://localhost:8000/*


## Tests
```bash
$ # local
$ pytest
```
```bash
$ # docker
$ docker build -t ynlp .\
$ docker --detach --name ynlp-backend-prod --publish 80:80 ynlp\
$ docker exec ynlp-backend-prod pytest
```
```bash
$ # load test
$ python tests/load/async_test_using_multithreading.py
```







