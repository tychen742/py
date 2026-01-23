## the project 
This project is based on Think Python, 3rd edition, by Allen B. Downey

## installations
- use jupyter book v1
  
```python
pip install "jupyter-book==1.0.4.post1"
pip install sphinx_new_tab_link
```


## downloads
```python
from os.path import basename, exists

def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve

        local, _ = urlretrieve(url, filename)
        print("Downloaded " + str(local))
    return filename

download('https://github.com/AllenDowney/ThinkPython/raw/v3/thinkpython.py');
download('https://github.com/AllenDowney/ThinkPython/raw/v3/diagram.py');
download('https://github.com/ramalho/jupyturtle/releases/download/2024-03/jupyturtle.py');
```
