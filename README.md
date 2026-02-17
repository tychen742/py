## the project 
This project is based on Think Python, 3rd edition, by Allen B. Downey

## installations
Install jupyter-notebook and sphinx_new_tab_link and jb will build.
  
```python
pip install "jupyter-book==1.0.4.post1" ### same as pip install "jupyter-book<2"
pip install sphinx_new_tab_link ### current: 0.8.1
```

jupyter-book1.0.4.post1 will install:
```python
  - sphinx 7.4.7
  - sphinx_thebe
  - docutils 0.21.2
  - sphinx_external_toc 1.1.0
  - sphinx-thebe 0.3.1
```

If you want earlier versions:
```python
pip install "jupyter-book<2"
pip install "sphinx<7.2" "sphinx-new-tab-link<0.5" "docutils<0.21" "sphinx-external-toc~=1.0.1" jupyter-book==1.0.4.post1 sphinx==7.1.2 sphinx-new-tab-link==0.4.0 docutils==0.20.1 sphinx-external-toc==1.0.1
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
