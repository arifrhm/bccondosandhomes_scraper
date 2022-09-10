venv:
	python3 -m venv venv

activate-venv:
	source ./venv/bin/activate

upgrade-pip:
	pip install --upgrade pip

install-req:
	pip install -r requirements.txt