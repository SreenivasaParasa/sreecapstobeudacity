setup:
	# Create python virtualenv & source it
	python3 -m venv ~/.capstone

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
	
lint:
	hadolint Dockerfile
	pylint --disable=R,C,W1203 **.py
	
start-api:
	python app.py

all: install lint test