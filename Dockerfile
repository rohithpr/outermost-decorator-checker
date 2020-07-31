# Intentionally using the older version - Python 2.7 as the primary use case
# for this gh action is a legacy repo using Python 2.7, and I will be using
# the ast module. Python 3's ast module fails to parse 2.7 code correctly.
FROM python:2.7

COPY entrypoint.sh /entrypoint.sh
COPY checker.py /checker.py
COPY service.py /service.py

ENTRYPOINT [ "/entrypoint.sh" ]
