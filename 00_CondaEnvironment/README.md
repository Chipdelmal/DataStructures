
## Useful Commands

To install from *yml* file:

```bash
conda env create -f DataStructures.yml
```

To create from scratch the *conda* environment run the following command in terminal (requires _Anaconda_):

```bash
conda create -n DataStructures python=3.7.2
```

To run the environment:

```bash
source activate DataStructures
```

To close the environment:

```bash
source deactivate
```

Adding the environment to Hydrogen (atom):

```bash
source activate DataStructures
python -m ipykernel install --user --name DataStructures
```

To export environment to *YML* (after activating):

```bash
conda env export > DataStructures.yml
```
