from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Game(BaseModel):
    name: str
    completed: bool = False
    priority: int = 0

games = [
    Game(name="Elden Ring", priority=2),
    Game(name="Halo", priority=0),
    Game(name="Zelda", priority=1),
    Game(name="Mario", priority=3),
    Game(name="Tetris", priority=0)
]

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

def get_sort_value(game):
    if game.priority == 0:
        return 999999
    
    return game.priority

@app.get("/games/priority", response_model=list[Game])
def prioritize_games():
    games.sort(key=get_sort_value)
    return games

@app.get("/games/{game_id}", response_model=Game)
def get_game(game_id: int) -> Game:
    if game_id < len(games):
        return games[game_id]
    else:
        raise HTTPException(status_code=404, detail=f"Game {game_id} not found")
    
    
