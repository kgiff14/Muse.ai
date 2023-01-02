import glob
import pickle
import numpy
import tensorflow as tf
from music21 import converter, instrument, note, chord
from tf.keras.models import Sequential
from tf.keras.layers import Dense