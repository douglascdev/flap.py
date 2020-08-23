PYTHON=python3
PIP=pip3

clean:
	rm -rf build dist flappy.egg-info .venv

build_package: clean
	$(PYTHON) setup.py sdist bdist_wheel

pip_install: build
	$(PIP) install .

req_install:
	$(PIP) install -r requirements.txt

test_pip_install: clean build_package pip_install
	cd ~;$(PYTHON) -c "from flappy import flappy; flappy()"

