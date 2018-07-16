# Dismantler
[![PyPI version](https://img.shields.io/pypi/v/dismantler-python.svg)](https://badge.fury.io/py/dismantler-python)
[![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)]()
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dismantler-python.svg)
[![Say Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/harrydrippin)

```
██████╗ ██╗███████╗███╗   ███╗ █████╗ ███╗   ██╗████████╗██╗     ███████╗██████╗ 
██╔══██╗██║██╔════╝████╗ ████║██╔══██╗████╗  ██║╚══██╔══╝██║     ██╔════╝██╔══██╗
██║  ██║██║███████╗██╔████╔██║███████║██╔██╗ ██║   ██║   ██║     █████╗  ██████╔╝
██║  ██║██║╚════██║██║╚██╔╝██║██╔══██║██║╚██╗██║   ██║   ██║     ██╔══╝  ██╔══██╗
██████╔╝██║███████║██║ ╚═╝ ██║██║  ██║██║ ╚████║   ██║   ███████╗███████╗██║  ██║
╚═════╝ ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
```
이 모듈은 Python 코드를 Parse Tree로 해체하며, Parse Tree 그 자체와 Token들, Symbol들을 따로 모은 것을 Dictionary 혹은 JSON 데이터로 얻을 수 있습니다.

## 어디에 쓰는 것인가요?

Dismantler는 Python 코드를 입력으로 받아서 Parse Tree를 빠른 시간 이내에 생성합니다. 또한, 생성된 Parse Tree를 Dictionary나 JSON으로 내보낼 수 있습니다. 원한다면 Token들과 Symbol들의 리스트를 각각 분리된 채로 추출할수도 있습니다. 이 프로젝트는 연구 목적으로 사용하기에 적합합니다. 좋은 예로는 딥러닝 모델에게 코드를 토큰화된 순서를 가지는 데이터로써 학습시키거나, Python code를 해석해서 토큰 레벨로 나누는 등의 작업을 통해 교육용 프로그램 등에 적용될 수 있을 것입니다.

## 기초 사용 방법

```python
>>> import dismantler

>>> d = dismantler.run_from_string('a + 5').dictionary()
>>> print(d)
{
    "type": "symbol",
    "name": "stmt",
    "value": [
        // Nodes...
    ]
}

>>> d = dismantler.run_from_file('file.py').json(indent=4)
>>> print(d)
"{
    "type": "symbol",
    "name": "stmt",
    "value": [
        // Nodes...
    ]
}"
```

## 설치

### pip을 통한 설치
```bash
pip3 install dismantler-python
```

### 소스 파일을 직접 빌드하여 설치
```bash
git clone http://github.com/harrydrippin/dismantler-python
cd dismantler-python
python3 setup.py install
```

## 기여

이 프로젝트는 현재 상당히 작아서, 이 프로젝트에 대한 어떠한 형태의 기여도 매우 환영합니다. Issue나 PR 등을 올려주시면 빠른 시간 안에 확인하겠습니다.