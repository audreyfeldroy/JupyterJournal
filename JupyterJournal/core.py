"""Core functionality for JupyterJournal"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['hdrs', 'app', 'rt', 'nbs', 'foo']

# %% ../nbs/00_core.ipynb 4
hdrs = (MarkdownJS(),HighlightJS(langs=['python', 'javascript', 'html', 'css',]),)

# %% ../nbs/00_core.ipynb 5
app,rt = fast_app(hdrs=hdrs)

# %% ../nbs/00_core.ipynb 6
nbs = L(Path('../nbs').glob('*.ipynb')).sorted()

# %% ../nbs/00_core.ipynb 10
def foo(): pass
