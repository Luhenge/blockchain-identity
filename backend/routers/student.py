from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from iroha_helper import get_identity_profile

router = APIRouter()

@router.get("/profile/{name}")
def student_profile(name: str):
    profile = get_identity_profile(name)
    if not profile["publicKey"]:
        raise HTTPException(status_code=404, detail=f"Student {name}@test not found or no keys")
    return {"ok": True, "profile": profile}

class ProofRequest(BaseModel):
    attribute: str

@router.post("/prove/{name}")
def prove_attribute(name: str, body: ProofRequest):
    # TODO Week 4: real selective disclosure. For now, stub.
    return {
        "ok": True,
        "name": f"{name}@test",
        "attribute": body.attribute,
        "proof": "stub-proof"
    }
