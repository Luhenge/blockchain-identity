# 🎓 Secure Digital Identity System using Blockchain (Hyperledger Iroha + FastAPI)

## 📌 Overview
This project implements a **university digital identity system** on a **permissioned blockchain**.  
It replaces the traditional centralized identity layer with a **blockchain-backed system** that improves **security, privacy, and user control**.

Built with:
- **Hyperledger Iroha (v1.5.0, Dockerized)**
- **FastAPI (Python backend)**
- **Postgres (ledger state + extra storage)**

---

## 🛠 Features (Planned & Implemented)

### ✅ Week 1 (done)
- [x] Set up Docker-based **Hyperledger Iroha + Postgres**.
- [x] Generated key pairs for `admin`, `student`, and `lecturer` accounts.
- [x] Configured **genesis block** with peers & public keys.
- [x] Created **FastAPI backend skeleton** with routes for admin/student/lecturer.

### 🔜 Next (Week 2–3)
- [ ] Implement identity APIs (register, login, issue credentials).
- [ ] Connect backend → Iroha CLI/API for blockchain transactions.
- [ ] Integrate Postgres for persistence.

### 📆 Later
- [ ] Mobile/Web frontend (student portal, lecturer dashboard, admin console).
- [ ] Security & authentication layer.
- [ ] Final testing, evaluation, and documentation.

---

## ⚡ Tech Stack
- **Blockchain:** Hyperledger Iroha (Docker)
- **Backend API:** FastAPI (Python)
- **Database:** Postgres
- **Containerization:** Docker & Docker Compose
- **Frontend (planned):** React Native (mobile) / React.js (web)
