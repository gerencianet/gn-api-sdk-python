#Local install
 pip install -e .

#Development install
python setup.py develop

#Running tests

py.test --cov=gerencianet --cov-config .coveragerc --cov-report html --cov-report term-missing
