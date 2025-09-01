from pathlib import Path
from typing import Literal

# Configuration – adjust if your paths differ
KEYS_DIR = Path(__file__).resolve().parent.parent / "iroha" / "keys"  # ../iroha/keys
DOMAIN = "test"

# ---- Types ----
Role = Literal["admin", "lecturer", "student"]

# ---- Helpers (stubbed for now) ----
def account_id(name: str) -> str:
    return f"{name}@{DOMAIN}"

def has_keypair(name: str) -> bool:
    """Check if keypair exists for name@domain."""
    pub = KEYS_DIR / f"{name}@{DOMAIN}.pub"
    priv = KEYS_DIR / f"{name}@{DOMAIN}.priv"
    return pub.exists() and priv.exists()

def read_public_key(name: str) -> str | None:
    """Return hex pubkey if exists."""
    pub = KEYS_DIR / f"{name}@{DOMAIN}.pub"
    if pub.exists():
        return pub.read_text().strip()
    return None

# ---- Planned real operations (to implement Week 3) ----
def create_account_on_chain(name: str, role: Role, public_key_hex: str) -> dict:
    """
    TODO (Week 3): call Iroha to create an account.
    For now, simulate success if key exists.
    """
    return {
        "accountId": account_id(name),
        "role": role,
        "publicKey": public_key_hex,
        "status": "created (stub)"
    }

def issue_credential_on_chain(lecturer: str, student: str, credential_type: str, value: str) -> dict:
    """
    TODO (Week 3): submit a transaction (e.g., as asset or detail).
    """
    return {
        "lecturer": account_id(lecturer),
        "student": account_id(student),
        "credential_type": credential_type,
        "value": value,
        "tx_status": "committed (stub)"
    }

def get_identity_profile(name: str) -> dict:
    """
    TODO (Week 3): query Iroha for account/metadata.
    """
    return {
        "accountId": account_id(name),
        "has_keys": has_keypair(name),
        "publicKey": read_public_key(name),
        "roles": ["stub-role"],  # later: real role query
    }
