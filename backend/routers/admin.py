from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from iroha_helper import create_account_on_chain, read_public_key

router = APIRouter()

class CreateAccountBody(BaseModel):
    name: str = Field(..., examples=["alice"])
    role: str = Field(..., regex="^(admin|lecturer|student)$", examples=["student"])

@router.post("/create-account")
def create_account(body: CreateAccountBody):
    pub = read_public_key(body.name)
    if not pub:
        raise HTTPException(
            status_code=400,
            detail=f"Public key for {body.name}@test not found. Generate keys first in iroha/keys."
        )
    result = create_account_on_chain(body.name, body.role, pub)
    return {"ok": True, "result": result}

@router.get("/whoami")
def whoami():
    return {"role": "admin", "message": "Admin routes ready"}
