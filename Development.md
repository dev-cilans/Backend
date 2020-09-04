



## Directory Structure

```bash
$ find . -type d -name  "__pycache__" -exec rm -r {} +
$ tree
.
|-- AUTHORS
|-- CHANGELOG
|-- Development.md
|-- Dockerfile
|-- Procfile
|-- Readme.md
|-- dev-requirements.txt
|-- requirements.txt
|-- runtime.txt
|-- setup.py
|-- spec # openapi-3.0 specification
|   `-- swagger.yml
|-- src
|   |-- __init__.py
|   |-- main.py # entrypoint for server
|   |-- routes.py
|   |-- settings.py
|   |-- v1
|   |   |-- __init__.py
|   |   `-- service
|   |       |-- Comment
|   |       |-- Emotion
|   |       |-- Lda
|   |       |-- Ner
|   |       |-- Sentiment
|   |       |-- Transcript
|   |       |-- Video
|   |       |-- WordCloud
|   |       `-- __init__.py
|   `-- v2
|       `-- __init__.py
`-- tests
    |-- integration # integration tests with nlp and frontend repo
    |-- load
    |   `-- async_test_using_multithreading.py
    `-- unit # sepearte tests for each service
        |-- test_main.py
        `-- test_response
            |-- keywords_response.txt
            |-- ner_test.txt
            |-- root_response.txt
            |-- video_comment.txt
            |-- video_description.txt
            |-- video_details.txt
            |-- video_transcript.txt
            `-- wordCount_response.txt
```

## Setup (Development)
```bash
# Get repository
$ git clone https://github.com/YouTubeNLP/Backend.git && cd Backend/
# Install all packages locally
# Some kind of virtual environment is recommened like miniconda or virtualenv
(your-env) $ pip install -r dev-requirements.txt
# Install spacy models
(your-env) $ python -m spacy download en_core_web_sm
# Create backend container
(your-env) $ uvicorn src.main:app --host=0.0.0.0 --reload
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







