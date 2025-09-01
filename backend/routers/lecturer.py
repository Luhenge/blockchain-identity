from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from iroha_helper import issue_credential_on_chain, read_public_key

router = APIRouter()

class IssueCredentialBody(BaseModel):
    lecturer: str = Field(..., examples=["lecturer"])
    student: str = Field(..., examples=["alice"])
    credential_type: str = Field(..., examples=["grade"])
    value: str = Field(..., examples=["A"])

@router.post("/issue-credential")
def issue_credential(body: IssueCredentialBody):
    # sanity: student key must exist (as proxy for account existence in stub)
    if not read_public_key(body.student):
        raise HTTPException(status_code=404, detail=f"Student {body.student}@test has no keypair")
    if not read_public_key(body.lecturer):
        raise HTTPException(status_code=404, detail=f"Lecturer {body.lecturer}@test has no keypair")
    result = issue_credential_on_chain(
        lecturer=body.lecturer,
        student=body.student,
        credential_type=body.credential_type,
        value=body.value
    )
    return {"ok": True, "tx": result}

@router.get("/whoami")
def whoami():
    return {"role": "lecturer", "message": "Lecturer routes ready"}
