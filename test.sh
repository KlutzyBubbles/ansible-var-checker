/usr/bin/python3 -m pip install -r requirements.txt
/usr/bin/python3 -m pip install pytest pytest-cov
/usr/bin/python3 -m pytest --cov-report xml:avc.xml --cov-report html --cov avc ./tests -vv