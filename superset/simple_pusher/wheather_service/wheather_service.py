import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schema import Whether as SchemaWhether
from models import Whether as ModelWhether

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url="postgresql://postgres:postgres@192.168.88.134:1111/postgres")


@app.post('/whether/', response_model=SchemaWhether)
async def add_whether(whether: SchemaWhether):
    db_whether = ModelWhether(city=whether.city, temp=whether.temp)
    db.session.add(db_whether)
    db.session.commit()
    return db_whether

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)