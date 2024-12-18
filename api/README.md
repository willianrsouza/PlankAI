# Fast API - Server

**This guide will help you set up the project, install dependencies, and run the application.**

## 1. Set Up Virtual Environment

**First, create and activate a virtual environment to isolate the project dependencies.**

For **Windows**:

```bash

.\venv\Scripts\Activate

```

For **Mac/Linux:**:

```bash

source venv/bin/activate

```
## 2. Install Dependencies

**Once the virtual environment is activated, install the required dependencies using pip:**

```bash

pip install -r requirements.txt

```
## 3. Start the Project

**To run the project, execute the main.py file:**

```bash

python main.py

```

**Or**

```bash

uvicorn main:app --reload

```

## 3. Access the Documentation

**FastAPI automatically generates interactive API documentation (Swagger):**

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc UI:** http://localhost:8000/redoc

