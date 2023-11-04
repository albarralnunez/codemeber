<div align="center">

![Codember](./codember.webp)

# :technologist: [Codember Solutions](https://codember.dev)

</div>


## Installation instructions:
```bash
rtx install
poetry install
poetry run pip-compile --output-file=./third_parties/python/requirements_lock.txt third_parties/python/requirements.txt
poetry run pip install -r third_parties/python/requirements_lock.txt
```

## 2023
### [Challenge 1](./2023/CHALLENGE_01/%20CHALLENGE_01.md): 
Python version:
```
bazel run //2023/CHALLENGE_01/python/...
```
