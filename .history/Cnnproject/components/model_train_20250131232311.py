from Cnnproject.config.config_entity import *
import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras.layers import Dense,Flatten
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
        
        X = Flatten()(vgg.output)
        prediction = Dense(2,activation = 'softmax')(X)
        
        model = tf.keras.models.Model(inputs=vgg.input,outputs = prediction)
        logging.info(model.summary())
        model.summary() 
        model.compile(loss='categorical_crossentropy',optimizer='adam',
                      metrics=['accuracy'])
        model.save(self.model_train.model_name)
        return model
        
    def Image_preprocess(self):
        train_datagen = ImageDataGenerator(rescale = 1/255,
                                           zoom_range = 0.1,
                                           horizontal_flip = True,
                                           validation_split =0.2,
                                           rotation_range=0.1)
        
        test_datagen = ImageDataGenerator(rescale = 1/255
            
        )    
        
        train_data = train_datagen.flow_from_directory(self.model_train.data_path,
                                                       batch_size =32,
                                                       subset = 'training',
                                                       target_size=(224, 224),
                                                       shuffle = True)       
        
        test_data = test_datagen.flow_from_directory(self.model_train.data_path,
                                                     batch_size =32,
                                                       subset = 'validation',
                                                       target_size=(224, 224),
                                                       shuffle = True)   
        
        model = tf.keras.models.load_model(self.model_train.model_name)
        model.fit(
            train_data,
            validation_data = test_data,
            epochs = 2,
            steps_per_epoch=len(train_data),
            validation_steps=len(test_data)
        )
    
    
