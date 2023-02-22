# Deadlock python 3.10.10

Relevant bugreports:

* https://github.com/python/cpython/issues/102126
* https://github.com/HypothesisWorks/hypothesis/issues/3585
* https://github.com/nedbat/coveragepy/issues/1559
* https://github.com/actions/runner/issues/2454

This repository provides a smaller reproducible example by combinding coverage.py and
hypothesis. For convenience, a dockerfile is available (as I don't have Py 3.10 on my
system available yet).

## Usage

Building image for particular python versions:

### Building

```bash
docker build --build-arg PYVERSION=3.10.10 --tag pydeadlock:3.10.10 .
docker build --build-arg PYVERSION=3.10.9 --tag pydeadlock:3.10.9 .
```

### Running

Running the container essentially runs:

```bash
coverage run repro.py
```

Run with 3.10.9 and container exits, run with 3.10.10 and process hangs:

```bash
docker run --rm -it pydeadlock:3.10.9
    1.6a63: cwd is now '/app'
    1.6a63: New process: executable: '/usr/local/bin/python'
    1.6a63: New process: cmd: ['/usr/local/bin/coverage', 'run', 'repro.py']
    1.6a63: New process: pid: 1, parent pid: 0
irrelevant
    1.6a63: atexit: pid: 1, instance: <coverage.control.Coverage object at 0x7f4161e1f700>
```

```bash
docker run --rm -it pydeadlock:3.10.10
    1.4de3: cwd is now '/app'
    1.4de3: New process: executable: '/usr/local/bin/python'
    1.4de3: New process: cmd: ['/usr/local/bin/coverage', 'run', 'repro.py']
    1.4de3: New process: pid: 1, parent pid: 0
irrelevant
    1.4de3: atexit: pid: 1, instance: <coverage.control.Coverage object at 0x7f8084a2f790>

# <hangs>
```
