## Build Documentation:
#### Install Requirements

```python
pip install -r docs/requirements.txt
```
create a new dir named as the language such as zh,cp all the things in Template to zh.  
#### Build Documentation
`python generate.py language action option`
if you build at the first time, run
```python
python generate.py -l zh -a fbuild
```  
if your network is not good enough to clone the submodule,run  
``python
python generate.py -l zh -a fbuild -r
``  
if the main project update, run
```python
python generate.py -l zh -a rebuild
```
if you modify the po files, run
```python
python generate.py -l zh -a update
```

##Notice
if you manage the doc on the readthedocs,mo files are not necessary,they only care po,rst,conf 