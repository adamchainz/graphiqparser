# graphiqparser
custom corporation parser for Graphiq

### setup
```
git clone https://github.com/datamade/graphiqparser.git
cd graphiqparser
python setup.py develop
parserator train training/labeled.xml graphiqparser
```

### usage
```
>>> import graphiqparser as gp  
>>> gp.parse('Sitwell Housing Inc')
[('Sitwell', 'CorporationName'), ('Housing', 'CorporationName'), ('Inc', 'CorporationLegalType')]
```
