"use strict"

// const arr = []; 
// arr.unshift("Rafaela"); 
// arr.push("Marcelo"); 
// arr.splice(1, 1, "Bianca", "Ricardo", "Marcela"); 
// arr.splice(0, 0, "Carlos"); 
// arr.splice(2, 1); 
// arr.pop(); 
// arr.shift(); 

// console.log(arr);

const arrayocorrencias = ["Alexandre", "Alexandre", "Robson", "alexandre", "ALEXANDRE"];

function contaOcorrencias(arr, item) { // Adicionei o nome da função
    let contador = 0; // Inicializa o contador em 0

    for (let i = 0; i < arr.length; i++) { // Percorre cada item do array
        if (arr[i] === item) { // Compara os itens do array
            contador++; // Incrementa o contador se encontrar uma correspondência
        }
    }

    return contador; // Retorna o total de ocorrências
}

const resultado = contaOcorrencias(arrayocorrencias, "Alexandre"); // Chama a função corretamente
console.log(resultado); // Exibe o resultado no console
