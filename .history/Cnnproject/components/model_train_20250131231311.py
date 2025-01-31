from Cnnproject.config.config_entity import *
import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras.layers import Dense,Faltten
from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from Cnnproject.utility.common import create_folder
from Cnnproject import logging


class ModelTrain:
    def __init__(self):
        self.model_train = ModelTrainingConfig()

        create_folder(self.model_train.root_dir)
        
    def Prepare_BaseModel(self):
        vgg = tf.keras.applications.VGG16(input_shape=(224,224,3),weights='imagenet',include_top=False)

        for layer in vgg.layers:
            layer.trainable = False
        
        X = Faltten()(vgg.output)
        prediction = Dense(2,activation = 'softmax')(X)
        
        model = tf.keras.models.Model(inputs=vgg.input,outputs = prediction)
        logging.info(model.summary())
        model.summary() 
        model.compile(loss='categorical_crossentropy',optimizer='adam',
                      metrics=['accuracy'])
        model.save(self.model_train.model_name)
        
            
    
    
