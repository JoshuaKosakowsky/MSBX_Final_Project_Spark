MSBX 5420 Final Project
Distributed Data Modeling & Analysis with PySpark

This repository provides a shared, reproducible PySpark development environment for the MSBX 5420 Final Project.

All team members run the same Spark version and dependencies using Docker to ensure consistency across machines.

🚀 Quick Start (Windows)
1. Install Required Software

Docker Desktop

GitHub Desktop (or Git)

VS Code (recommended)

Ensure Docker Desktop is running before starting.

2. Clone the Repository

Using GitHub Desktop:

File → Clone Repository

Select this repo

Or via terminal:

git clone <repo-url>
3. Start the Development Environment

From the project folder:

.\scripts\up.ps1

This will:

Build the Docker image

Start the Spark + Jupyter environment

Mount the project directory inside the container

4. Open Jupyter

Open your browser and go to:

http://localhost:8888

Open:

notebooks/00_run_pipeline.ipynb

Run the notebook cells.

🛑 Stop the Environment

When finished:

.\scripts\down.ps1
📁 Project Structure
MSBX_Final_Project_Spark/
│
├── src/project/        # Reusable PySpark pipeline code
│
├── notebooks/          # Exploration and presentation notebooks
│
├── configs/            # Environment configuration (local vs cluster)
│
├── docker/             # Docker environment definition
│
├── scripts/            # Start/stop scripts
│
├── data/
│   ├── raw/            # Raw local data (NOT committed)
│   └── processed/
│
└── outputs/            # Generated tables and figures
🧠 Development Philosophy

We use a "src layout" architecture:

Notebooks are for exploration and presentation.

All business logic lives in src/project/.

Configuration is externalized in configs/.

No hard-coded file paths inside code.

This keeps the project:

Reproducible

Clean

Scalable

Cluster-deployable

Portfolio-ready

⚙️ Local vs Cluster Execution

Local development uses:

configs/local.yaml

When deploying to the university AWS Spark cluster, we will use:

configs/cluster.yaml

The same codebase runs in both environments.

🔥 Why Docker?

Without Docker:

Different Spark versions

Dependency mismatches

Environment conflicts

With Docker:

Everyone runs the same environment

Setup is one command

The project is reproducible

🧪 Running the Pipeline Without Notebook (Optional)

Inside the container:

python -m project.cli --config configs/local.yaml
📊 Spark UI

When a Spark job is running, the Spark UI is available at:

http://localhost:4040
📌 Team Guidelines

Do NOT commit raw datasets.

Do NOT modify Docker versions without discussion.

Keep transformation logic inside src/project/.

Make meaningful commits (not single-file spam commits).

Discuss structural changes before merging.

🎯 Course Deliverables

This repository supports:

Project proposal

Project presentation

Python analysis code

Final written report

AWS cluster deployment

👨‍💻 MSBX 5420 Final Project Team

University of Colorado Boulder