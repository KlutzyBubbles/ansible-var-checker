python3 -m pip install -r requirements.txt
python3 -m pip install pytest pytest-cov
python3 -m pytest --cov-report html --cov ansiblevarchecker ./tests -vv
