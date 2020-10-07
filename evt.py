from tensorflow import keras
from tensorflow.keras import layers
def EVT(nin, hidden_sizes, nout):
    input_layer = [layers.Input(shape=nin)]
    hidden_layers = [layers.Dense(hidden_sz, activation='tanh',
                                  kernel_initializer='he_normal') for hidden_sz in hidden_sizes]
    output_layer = [layers.Dense(nout, activation='linear')]
    model = keras.Sequential(input_layer + hidden_layers + output_layer)
    return model
# default values takes from `https://github.com/VadimSokolov/Energy-EVT/blob/master/load_evt.py`
default_params = {
    'seed': 39,
    'hidden': [3],
    'learning_rate': 1e-2,
    'decay': 1e-4,
    'u': 31000,
    'nepoch': 15,
    'nin': 36,
    'nout': 1,
    'loss_function': 'mean_squared_error'
}
model = EVT(
    nin=default_params['nin'],
    hidden_sizes=default_params['hidden'],
    nout=default_params['nout']
)
model.compile(optimizer=keras.optimizers.Adam(learning_rate=default_params['learning_rate'], 
                                              decay=default_params['decay']),
              loss=default_params['loss_function'])
model.summary()
