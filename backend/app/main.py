from fastapi import FastAPI
from sqlalchemy import text
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database import Base , get_db, engine

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/test-db")
async def test_db(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"db_response": result.scalar()}

@app.get('/')
async def root():
    return {'message' : 'task manger backend running' }