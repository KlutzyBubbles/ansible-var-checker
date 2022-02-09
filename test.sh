/usr/bin/python3 -m pip install -r requirements.txt
/usr/bin/python3 -m pip install pytest pytest-cov
/usr/bin/python3 -m pytest --cov-report html --cov ansiblevarchecker ./tests -vv