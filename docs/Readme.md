## Build Documentation:  
This is a template of multi-language documents
#### Install Requirements

```python
pip install -r requirements.txt
```
create a new dir named as the language such as zh,cp all the things in Template to zh.  
#### Build Documentation
`python generate.py language option`
if you build at the first time, run
```python
python generate.py zh fbuild
```
if the main project update, run
```python
python generate.py zh rebuild
```
if you modify the po files, run
```python
python generate.py zh update
```

##Notice
if you manage the doc on the readthedocs,mo files are not necessary,they only care po,rst,conf 