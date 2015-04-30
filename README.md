# lasagnemould
A hack for less verbose initialization of [nolearn.lasagne](https://github.com/dnouri/nolearn)
neural nets.

To use this, import _layers_ from _lasagnemould_ instead of [_lasagne_](https://github.com/Lasagne/Lasagne)
and initialize your layers like this:

    from lasagnemould import layers

    mylayers = [
        layers.InputLayer(shape=(None, 784)),
        layers.DenseLayer(100),
        layers.DenseLayer(10, nonlinearity=softmax)
    ]

The advantage of this is that you can directly instantiate the layers,
including the use of *args instead of using factories without the need
to specify the _incoming_ keyword.

See [here](http://nbviewer.ipython.org/github/BenjaminBossan/lasagnemould/blob/master/example/mould.ipynb)
for how this initialization differs from the default initialization.
