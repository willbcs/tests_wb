"use strict"

// const arrayVariado = ["ADS", 2, true, 4.5, false];
const arrayProfs = [];

arrayProfs[0] = "Guerra";

arrayProfs.unshift("Claudio", "Rangel", "Avelino");
let removido = arrayProfs.shift();
console.log(removido);

arrayProfs.push("Léo", "Sobrino", "Mauá");
arrayProfs.pop();

arrayProfs.splice(3, 1);
arrayProfs.splice(0, 0, "Léo", "Mauá"); // Primeiro número é a posição, segundo número é o número de elemento que vou adicionar e o terceiro é o que vou adicionar
// arrayProfs.splice(0, 1, "Mauá");
arrayProfs.sort()

// let x = arrayProfs[0];
// console.log(x);

console.log(arrayProfs);
console.table(arrayProfs);

for (let i=0; i < arrayProfs.length; i++)
{
    console.log(arrayProfs[i])
}

//Função de Callback
//- Função passada como argumento para outra função
//- Chamada pode ser imediata ("callback síncrono") ou em outro momento ("callback assíncrono")

// arrayProfs.forEach(
//     function (element) {
//         console.log(element);
//     }    
// );

arrayProfs.forEach(element => {console.log(element); });

// console.log(arrayVariado);
// console.table(arrayVariado);
// console.log(typeof arrayVariado);
// console.log(arrayVariado.length);

