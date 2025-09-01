from fastapi import APIRouter

router = APIRouter(
    prefix="/identity",
    tags=["Identity"]
)

# Example: Create a digital identity
@router.post("/create")
def create_identity(name: str, role: str):
    """
    Creates a digital identity (admin, student, lecturer).
    """
    return {"message": f"Identity created for {name}", "role": role}

# Example: Verify an identity
@router.get("/verify/{name}")
def verify_identity(name: str):
    """
    Verifies if a digital identity exists.
    """
    # Later, this will check blockchain state
    return {"verified": True, "name": name}
