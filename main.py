from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Game(BaseModel):
    name: str
    completed: bool = False

games = []

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/games")
def create_game(game: Game):
    games.append(game)
    return games

@app.get("/games", response_model=list[Game])
def list_games(limit: int = 10):
    return games[0:limit]

@app.get("/games/{game_id}", response_model=Game)
def get_game(game_id: int) -> Game:
    if game_id < len(games):
        return games[game_id]
    else:
        raise HTTPException(status_code=404, detail=f"Game {game_id} not found")