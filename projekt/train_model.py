import tensorflow as tf
import numpy as np

def create_and_train_model(X_train, y_train, X_test, y_test):
   
    X_train = np.reshape(X_train, (X_train.shape[0], 150, 150, 3))
    X_test = np.reshape(X_test, (X_test.shape[0], 150, 150, 3))

    num_classes = len(np.unique(y_train))
    y_train = tf.keras.utils.to_categorical(y_train, num_classes)
    y_test = tf.keras.utils.to_categorical(y_test, num_classes)
    
    vgg16 = tf.keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(150, 150, 3))

    x = vgg16.output
    x = tf.keras.layers.Flatten()(x)

    x = tf.keras.layers.Dense(1024, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01))(x)

    x = tf.keras.layers.Dropout(0.5)(x)

    predictions = tf.keras.layers.Dense(num_classes, activation='softmax', kernel_regularizer=tf.keras.regularizers.l2(0.01))(x)

    model = tf.keras.models.Model(inputs=vgg16.input, outputs=predictions)

    for layer in vgg16.layers:
        layer.trainable = False

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        featurewise_center=True,
        featurewise_std_normalization=True,
        rotation_range=360,
        width_shift_range=0.5,
        height_shift_range=0.5,
        horizontal_flip=True)
    datagen.fit(X_train)
    model.fit_generator(datagen.flow(X_train, y_train, batch_size=64),
                        epochs=15, validation_data=(X_test, y_test))
    return model