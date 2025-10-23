

---

```markdown
# 🚀 WSO2 API Manager + FastAPI Student API Integration

A simple **Student Management API** built with **FastAPI**, integrated with **WSO2 API Manager 4.5.0** to demonstrate secure API management, authentication, and gateway flow.  
This project showcases how enterprises like **Hayleys IT** can use WSO2 as a central API Gateway to manage, secure, and monitor backend microservices.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Setup & Run Locally](#setup--run-locally)
- [WSO2 API Configuration](#wso2-api-configuration)
- [Testing the API via Postman](#testing-the-api-via-postman)
- [Screenshots](#screenshots)
- [Advantages for Enterprise Projects](#advantages-for-enterprise-projects)
- [Author](#author)
- [License](#license)

---

## 🧠 Overview

This project demonstrates how to:
- Build a lightweight REST API using **FastAPI**
- Expose it securely through **WSO2 API Manager**
- Manage authentication, throttling, and routing through the API Gateway
- Test requests using **Postman**

It’s ideal for academic demonstrations, internship portfolios, and learning enterprise API integration.

---

## 🏗️ Architecture

```

Postman (Client)
│
▼
WSO2 API Gateway (localhost:8280 / 8243)
│
▼
FastAPI Backend (localhost:8000)
│
▼
Response returned to Client

```

### Request Flow:
1. Client sends a request (with Bearer Token or API Key) to **WSO2 Gateway**
2. Gateway verifies credentials using the **Key Manager**
3. Gateway routes request to backend **FastAPI** endpoint
4. Response flows back securely through WSO2

---

## ✨ Features

| Feature | Description |
|----------|--------------|
| 🔐 **Authentication** | OAuth2 and API Key-based access |
| 🚦 **Rate Limiting** | Configure request quotas per app/user |
| 🧩 **Centralized Gateway** | Securely routes all microservices |
| 📈 **Monitoring Ready** | Integrates with WSO2 Analytics / ELK |
| 🔄 **Versioning** | Host `/v1.0.0`, `/v2.0.0` APIs simultaneously |
| 🌐 **Cross-Origin Support** | Allow access from web frontends |

---

## 🧰 Tech Stack

- **Backend:** FastAPI (Python)
- **API Gateway:** WSO2 API Manager 4.5.0
- **Client:** Postman
- **Language:** Python 3.12+
- **Runtime:** Uvicorn

---

## 📂 Folder Structure

```

wso2-student-api/
│
├── backend/
│   ├── main.py                  # FastAPI app
│   ├── requirements.txt
│   └── **init**.py
│
├── wso2-config/
│   ├── student_api_publisher.png   # Screenshots of API creation
│   ├── api_gateway_flow.png        # Gateway architecture diagram
│   └── README.md
│
├── .gitignore
├── LICENSE
└── README.md

````

---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/wso2-student-api.git
cd wso2-student-api
````

### 2️⃣ Install FastAPI

```bash
pip install fastapi uvicorn
```

### 3️⃣ Run the Backend

```bash
uvicorn backend.main:app --reload --port 8000
```

Check at 👉 [http://localhost:8000/students](http://localhost:8000/students)

### 4️⃣ Start WSO2 API Manager

```bash
cd wso2am-4.5.0/bin
api-manager.bat
```

Access portals:

* Publisher: [https://localhost:9443/publisher](https://localhost:9443/publisher)
* Dev Portal: [https://localhost:9443/devportal](https://localhost:9443/devportal)
* Admin Console: [https://localhost:9443/carbon](https://localhost:9443/carbon)

Login:

```
Username: admin
Password: admin
```

---

## 🧩 WSO2 API Configuration

1. **Create New API**

   * In Publisher → `Create → REST API → From Scratch`
   * Name: `StudentAPI`
   * Context: `/student`
   * Version: `1.0.0`
   * Endpoint: `http://localhost:8000`
   * Click **Create**

2. **Add Resource**

   * Path: `/students`
   * Method: `GET`
   * Save

3. **Enable Security**

   * Runtime Configurations → Enable ✅ OAuth2 and ✅ API Key

4. **Deploy & Publish**

   * Go to Deployments → Deploy New Revision → Select Default Env → **Deploy**
   * Lifecycle → **Publish**

---

## 🧪 Testing the API via Postman

### Option 1 — Using OAuth2 Token

1. In **Developer Portal**, subscribe to your API
2. Generate **Access Token**
3. In Postman:

   ```
   GET https://localhost:8243/student/1.0.0/students
   ```

   Header:

   ```
   Authorization: Bearer <ACCESS_TOKEN>
   ```

### Option 2 — Using API Key (easier for demo)

1. Enable `API Key` in Runtime Configurations
2. Generate Key in Dev Portal
3. In Postman:

   ```
   GET http://localhost:8280/student/1.0.0/students
   ```

   Header:

   ```
   ApiKey: <YOUR_API_KEY>
   ```

✅ You should receive:

```json
[
  {"id": 1, "name": "Ayesha", "course": "IT", "year": 3},
  {"id": 2, "name": "Nimal", "course": "CS", "year": 2},
  {"id": 3, "name": "Kavindu", "course": "SE", "year": 4}
]
```

---

## 📸 Screenshots

| Description          | Example                                 |
| -------------------- | --------------------------------------- |
| WSO2 Publisher       | `wso2-config/student_api_publisher.png` |
| Gateway Flow Diagram | `wso2-config/api_gateway_flow.png`      |

---

## 🏢 Advantages for Enterprise Projects

| Aspect                   | Benefit                                                         |
| ------------------------ | --------------------------------------------------------------- |
| **Centralized Security** | All APIs are managed, authenticated, and monitored in one place |
| **Scalability**          | Multiple backend services under one gateway                     |
| **Visibility**           | Monitor usage analytics and API health                          |
| **Policy Management**    | Enforce throttling, quotas, and version control                 |
| **Ease of Integration**  | Standard interface for internal and external clients            |

💡 *Used by enterprises like Hayleys, WSO2, and government tech agencies to build secure API ecosystems.*

---


---

### ✅ After adding it
1. Save it as `README.md` in your repo root.  
2. Stage and commit:
   ```bash
   git add README.md
   git commit -m "docs: add detailed project README"
   git push
````




