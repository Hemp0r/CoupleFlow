# Define variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
UVICORN = $(PYTHON) -m uvicorn
APP = app.main:app

.PHONY: help
help:
	@echo "Makefile for Backend Management"
	@echo "Usage:"
	@echo "  make setup         Create a virtual environment and install dependencies"
	@echo "  make run           Run the backend server"
	@echo "  make test          Run tests"
	@echo "  make lint          Run linter (flake8)"
	@echo "  make clean         Clean up virtual environment and temporary files"
	@echo "  make freeze        Freeze current dependencies into requirements.txt"

# Setup virtual environment and install dependencies
setup:
	python3 -m venv $(VENV)
	source venv/bin/activate
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt

# Run the server
run:
	$(UVICORN) $(APP) --reload

# Run tests
test:
	$(PYTHON) -m pytest tests

# Lint ALL THE THINGS
lint:
	isort .
	black .
	$(PYTHON) -m flake8 app

# Clean virtual environment and temporary files
clean:
	rm -rf $(VENV) __pycache__ */__pycache__

# Freeze dependencies into requirements.txt
freeze:
	$(PIP) freeze > $(REQ)

sql-init:
	$(PYTHON) -m app.scripts.db_init
