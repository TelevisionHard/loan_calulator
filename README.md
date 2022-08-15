## Loan Payment Calculator

Simple command line loan calculator. 

### Usage Examples
#### Differential Payments:
```python
python main.py --type=diff --principal=1000000 --periods=10 --interest=10
```

#### Annuity Payment:
```python
python main.py --type=annuity --principal=1000000 --periods=60 --interest=10
```

#### Loan term:
```python
python main.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
```

#### Loan Principal:
```python
python main.py --type=annuity --payment=8722 --periods=120 --interest=5.6
```
