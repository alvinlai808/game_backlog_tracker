# Installation
1. Open terminal and navigate to the root directory of the project
2. Run `python3 -m venv .venv`
3. Run `source .venv/bin/activate`
4. Run `pip install -r requirements.txt`

# Launch Server
1. Run `uvicorn main:app --reload`
2. Open `http://127.0.0.1:8000` in your browser

# API Reference (CURL Commands)
## Add game
`curl -X POST -H "Content-Type: application/json" -d '{"name":<string>,"completed":<boolean>}' 'http://127.0.0.1:8000/games'`

## Get specific game
`curl -X GET http://127.0.0.1:8000/games/<integer>`

## Get list of games
`curl -X GET 'http://127.0.0.1:8000/games?limit=<integer>'`
