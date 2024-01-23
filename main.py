from fastapi import FastAPI
from migrator import Migrator

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/migrate-from-asana")
def migrate_from_asana():
    migrator = Migrator(
        asana_token="2/1201999580693479/1202070784240484:53ee09bc53519491d6227bbb59456516",
        monday_token="eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjMxMTIxMjQ1OSwiYWFpIjoxMSwidWlkIjo1NDUzOTU0MSwiaWFkIjoiMjAyNC0wMS0xN1QxMzowMjoxMC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MjA3OTk0MjUsInJnbiI6ImV1YzEifQ._BBVy-yeygRNSvaEauCfKTKI8rqErgzB1Ie3DQRKyW4",
    )

    create_board = migrator.create_monday_board_with_asana_project(
        "1205831995552585", 1053044
    )
