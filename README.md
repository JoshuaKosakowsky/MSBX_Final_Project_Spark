# MSBX 5420 Final Project
## Distributed Data Modeling & Analysis with PySpark

This repository provides a **reproducible, scalable data analytics framework** for the MSBX 5420 Final Project.

The project is designed to support:

- Large-scale data processing using **PySpark**
- Local development using **Docker**
- Distributed execution on **AWS EMR clusters**
- Collaborative team workflows using a structured codebase

---

## 🚀 Quick Start

---

## 🪟 Windows

### 1. Install Required Software

- Docker Desktop  
- GitHub Desktop (or Git)  
- VS Code (recommended)

Ensure Docker Desktop is running before starting.

---

### 2. Clone the Repository

Using GitHub Desktop:

- File → Clone Repository
- Select this repo

Or via terminal:

```bash
git clone https://github.com/JoshuaKosakowsky/MSBX_Final_Project_Spark.git
cd MSBX_Final_Project_Spark
```

---

### 3. Start the Development Environment

```powershell
.\scripts\up.ps1
```

---

### 4. Open Jupyter

Go to:

http://localhost:8888

Open:

notebooks/00_run_pipeline.ipynb

---

## 🍎 macOS

### 1. Install Required Software

- Docker Desktop for Mac
- Git
- VS Code (recommended)

Install Git if needed:

```bash
xcode-select --install
```

(Optional) Install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify installations:

```bash
docker --version
git --version
```

Ensure Docker Desktop is running before continuing.

---

### 2. Clone the Repository

```bash
git clone https://github.com/JoshuaKosakowsky/MSBX_Final_Project_Spark.git
cd MSBX_Final_Project_Spark
```

---

### 3. Start the Development Environment

```bash
docker compose -f docker/docker-compose.yml up --build
```

---

### 4. Open Jupyter

Go to:

http://localhost:8888

Open:

notebooks/00_run_pipeline.ipynb

---

## 🛑 Stop the Environment

### Windows

```powershell
.\scripts\down.ps1
```

### macOS

```bash
docker compose -f docker/docker-compose.yml down
```

---

## 📁 Project Structure

MSBX_Final_Project_Spark/

- src/project/        → Core PySpark pipeline code  
- notebooks/          → Exploration and presentation notebooks  
- configs/            → Environment configuration  
- docker/             → Docker setup  
- scripts/            → Start/stop scripts  
- data/               → Raw/processed data (not committed)  
- outputs/            → Generated tables/figures  

---

## 🧠 Development Philosophy

- Notebooks are for exploration and presentation only  
- All logic lives in `src/project/`  
- Configuration is externalized in `configs/`  
- No hard-coded file paths  

Pipeline flow:

Ingest → Transform → Analyze → Output

---

## ⚙️ Local vs Cluster Execution

Local:

configs/local.yaml  

Cluster:

configs/cluster.yaml  

---

## 🔥 Why Docker?

Without Docker:

- Inconsistent environments  
- Dependency issues  

With Docker:

- Reproducible environment  
- Same setup for all team members  
- Easy onboarding  

---

## 🧪 Running Without Notebook (Optional)

```bash
python -m project.cli --config configs/local.yaml
```

---

## 📊 Spark UI

http://localhost:4040

---

## 📌 Team Guidelines

- Do NOT commit raw datasets  
- Keep logic inside `src/project/`  
- Use notebooks only for exploration  
- Make meaningful commits  
- Coordinate structural changes  

---

## 🎯 Course Deliverables

- Project proposal  
- Project presentation  
- PySpark analysis  
- Final report  
- AWS EMR deployment  

---

## 👨‍💻 MSBX 5420 Final Project Team

University of Colorado Boulder