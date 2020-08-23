PYTHON=python3
PIP=pip3

clean:
	rm -rf build dist flappy.egg-info

build_package:
	$(PYTHON) setup.py sdist bdist_wheel

pip_install: clean build
	$(PIP) install .

req_install:
	$(PIP) install -r requirements.txt

test_pip_install: clean build_package pip_install
	cd ~;$(PYTHON) -c "from flappy import flappy; flappy()"

