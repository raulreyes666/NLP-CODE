const fs = require('fs');
const util = require('util');
const readFile = util.promisify(fs.readFile);

// Función para contar palabras por letra
function contarPalabrasPorLetra(texto) {
  const cuentas = {};

  // Tokenizar el texto en palabras
  const palabras = texto.toLowerCase().match(/\b\w+\b/g);

  // Contar palabras por letra
  palabras.forEach(palabra => {
    const letraInicial = palabra[0];
    if (letraInicial.match(/[a-z]/)) {  // Ignorar palabras que comienzan con símbolos
      cuentas[letraInicial] = (cuentas[letraInicial] || 0) + 1;
    }
  });

  return cuentas;
}

// Leer el contenido del archivo
readFile('quijote.txt', 'utf-8')
  .then(contenido => {
    // Contar palabras por letra
    const resultado = contarPalabrasPorLetra(contenido);

    // Ordenar letras por frecuencia de mayor a menor
    const letrasOrdenadas = Object.entries(resultado)
      .sort((a, b) => b[1] - a[1])
      .reduce((obj, [letra, cantidad]) => {
        obj[letra] = cantidad;
        return obj;
      }, {});

    // Imprimir el resultado ordenado
    console.log("Palabras por letra A-Z");
    console.log("Número de palabras por letra (ordenado por frecuencia):");
    Object.entries(letrasOrdenadas).forEach(([letra, cantidad]) => {
      console.log(`${letra.toUpperCase()}: ${cantidad}`);
    });
  })
  .catch(error => console.error('Error al leer el archivo:', error));
