const tf = require('@tensorflow/tfjs');

// Crea un modelo secuencial
const model = tf.sequential();
model.add(tf.layers.dense({ units: 8, inputShape: [10], activation: 'relu' }));
model.add(tf.layers.dense({ units: 1, activation: 'sigmoid' }));

// Compila el modelo
model.compile({ optimizer: 'adam', loss: 'binaryCrossentropy', metrics: ['accuracy'] });

// Datos de entrenamiento (ficticios)
const trainingData = tf.tensor2d([
  [0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
  [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
  [0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]);

const outputData = tf.tensor2d([
  [0],
  [1],
  [0],
  [1]
]);

// Entrenar el modelo
model.fit(trainingData, outputData, { epochs: 100 })
  .then(() => {
    // Realizar una predicción con nuevos datos
    const newData = tf.tensor2d([[0, 0, 1, 1, 0, 0, 1, 0, 1, 1]]);
    const prediction = model.predict(newData);
    const result = prediction.arraySync()[0][0];

    console.log('Prediction: ', result);
  });
