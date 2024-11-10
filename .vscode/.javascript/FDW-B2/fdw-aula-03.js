"use strict";

// const arrayAmigos = ["William", "William2", "Kauã", "Kauã", "Felipe", "Felipe"];

// const arrayMedias = [5.5, 7.5, 2, 10, 9.5, 9];

// // console. log (arrayAmigos.includes("William"));
// let existeWilliam = arrayAmigos.includes("William");
// console.log("Existe William no array?", existeWilliam);

// let indiceFelipe =  arrayAmigos.indexOf("Felipe");
// console.log("Índice do Felipe no array?", indiceFelipe);


// function existeElemento(arr, item)
// {
//     return (arr.includes(item))? 'sim' : 'não';
    
// } 

// let existeWilliam2 = existeElemento(arrayAmigos, "William2");
// console.log("Existe William2 no array?", existeWilliam2);

// function excluirElemento(arr, item)
// {
//     let position = arr.indexOf(item)
//     return (position != -1)? arr.splice(position) : "False"
    
// }

// let excluirNome = excluirElemento(arrayAmigos, 'Will');
// console.log(excluirNome);


const arrayOriginal = ["William", "William2", "Kauã", "Kauã", "Felipe", "Felipe"];


function excluirElementos (array, item)
{
    const arrayCopia = array.slice();
    let position = arrayCopia.indexOf(item);

    while (position != -1)
    {
        arrayCopia.splice(position, 1);
        position = arrayCopia.indexOf(item);
    }    
    return arrayCopia;
}


console.log("Array original antes:", arrayOriginal);
console.log();
let excluirKaua = excluirElementos(arrayOriginal, "Kauã");
console.log(excluirKaua);
console.log()
console.log("Array original depois:", arrayOriginal);
