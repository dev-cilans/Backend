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

## Setup

```bash
# Create service container
$ docker build --tag ynlp .
$ docker run --detach \
--name ynlp_demo \
--publish 8080:8080 \
ynlp
```

## Example

```bash
# Try a post request on the comments endpoint.
# Returns the top k comments for video specified in data.json.
$ curl "http://localhost:8080/score/comments" \
--request POST \
--header "Content-Type: application/json" \
--data @data.json
```

```bash
# Try a post request on the transcript endpoint.
# Returns video transcript for specified video.
$ curl "http://localhost:8080/score/transcript" \
--request POST \
--header "Content-Type: application/json" \
--data @data.json
```

## API Reference
<table>
	<tr>
		<th>Method</th>
		<th>Status</th>
		<th>Url</th>
		<th>Response</th>
	</tr>
	<tr>
		<td>POST</td>
		<td>201</td>
		<td>http://127.0.0.1:8080/score/comments</td>
		<td>
			
{
	
}	
		</td>
	</tr>
	<tr>
		<td>POST</td>
		<td>201</td>
		<td>http://127.0.0.1:8080/score/transcript</td>
		<td>	
{
	
}	
		</td>
	</tr>
</table>
