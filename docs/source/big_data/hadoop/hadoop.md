# Apache Hadoop y Algoritmo Map/Reduce

```{toctree}
:caption: 'Temas:'
:maxdepth: 2
:hidden:
notebooks/1-01_
notebooks/1-02_
notebooks/1-03_
notebooks/1-04_

```

```console
docker run --rm -it \
    --name hadoop \
    -p 50070:50070 \
    -p 8088:8088 \
    -p 8888:8888 \
    -v "$PWD":/workspace \
    jdvelasq/hadoop:2.10.1
```




- {doc}`notebooks/1-01_`
- {doc}`notebooks/1-02_`
- {doc}`notebooks/1-03_`
- {doc}`notebooks/1-04_`

