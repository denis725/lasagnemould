"""A hack for easier initialization of nolearn.lasagne neural nets.

To use this, import the layers from lasagnemould instead of lasagne
and initialize your layers like this:

    from lasagnemould import layers

    mylayers = [
        layers.InputLayer(shape=(None, 784)),
        layers.DenseLayer(100),
        layers.DenseLayer(10, nonlinearity=softmax)
    ]

The advantage of this is that you can directly instantiate the layers,
including the use of *args instead of using factories, and you can
omit the 'incoming' keyword.

"""

import lasagne
from lasagne import layers as lasagnelayers


def mould(Layer):
    def _init(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.is_init_ = True

    def initialize(self, *args, **kwargs):
        if 'incoming' in kwargs:
            self.incoming = kwargs['incoming']
            _init_with_incoming(self)
        else:
            _init_without_incoming(self)

        if 'name' in kwargs:
            self.name = kwargs['name']
        return self

    def _init_with_incoming(self):
        if not hasattr(self, 'incoming'):
            raise TypeError("Initialization requires the 'incoming' "
                            "attribute to be set beforehand.")
        self._old_init(self.incoming, *self.args, **self.kwargs)

    def _init_without_incoming(self):
        self._old_init(*self.args, **self.kwargs)

    def _len(self):
        return 2

    def _iter(self, *args, **kwargs):
        for i in range(2):
            yield self[i]

    @property
    def _name(self):
        return str(self).split('.')[2].split(' ')[0]

    def _getitem(self, idx):
        if idx == 0:
            return self
        elif idx == 1:
            return {}

    MouldLayer = type(Layer.__name__, (Layer,), {
        '_old_init': Layer.__init__,
        '__init__': _init,
        '_init': _init,
        '__call__': initialize,
        '__len__': _len,
        '__iter__': _iter,
        '__getitem__': _getitem,
        '__name__': _name,
    })

    return MouldLayer


all_layers = {key: val for key, val in lasagnelayers.__dict__.items()
              if 'Layer' in key}

layer_defs = ''
for name, layer in all_layers.items():
    layer_defs += '@mould\n'
    layer_defs += 'class {}({}):'.format(name, str(layer).split("'")[1]) + '\n'
    layer_defs += '    pass\n\n\n'

exec(layer_defs)
