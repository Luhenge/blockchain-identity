from fastapi import FastAPI
from routers import admin, student, lecturer

app = FastAPI(title="Blockchain Identity - Backend (dev)")

# include routers
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(student.router, prefix="/student", tags=["Student"])
app.include_router(lecturer.router, prefix="/lecturer", tags=["Lecturer"])

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
