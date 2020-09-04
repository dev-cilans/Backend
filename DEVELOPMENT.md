



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

## Secrets
1. Create a [new project](https://console.developers.google.com/projectcreate) in the [Google Developers Console](https://console.developers.google.com).
2. Enable [YouTube Data API v3](https://console.developers.google.com/apis/library/youtube.googleapis.com?id=125bab65-cfb6-4f25-9826-4dcc309bc508).
3. Create two [API Key credentials](https://console.developers.google.com/apis/credentials) so your application can submit API requests.
5. Create a `.env` file in the root diretory of project and paste the keys there:
```bash
cat > .env << EOF
ENVIRONMENT=developement
API_KEY=<your-secret-api-key>
TEST_KEY=<your-secret-test-key>
EOF
```

## Setup (Development)
```bash
# Get repository
$ git clone https://github.com/YouTubeNLP/Backend.git && cd Backend/
# Install all packages locally
# Some kind of virtual environment is recommened like miniconda or virtualenv
(your-env) $ pip install -r requirements-dev.txt
# Create backend container
(your-env) $ uvicorn src.main:app --host=0.0.0.0 --reload
 ```
*Project is served at http://localhost:8000/*

## Code Style
> TODO  

We use `pylint` for code checking and `black` for formatting in our dev pipeline. Execute `pre-commit install` to install git hooks in your .git/ directory.

## Tests
```bash
$ # local
$ pytest
```
```bash
$ # load test
$ python tests/load/async_test_using_multithreading.py
```







