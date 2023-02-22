ARG PYVERSION=3.10.10
FROM python:${PYVERSION}-slim-bullseye

WORKDIR /app
COPY requirements.txt repro.py .

RUN pip install -r requirements.txt

ENV COVERAGE_DEBUG=process,pid

CMD ["coverage", "run", "repro.py"]
