"use strict"

const objVinicius = 
{

    nome: "Vinicius Teixeira",
    idade: 32,
    foiAluno: true

};

const objWilliam = 
{   

    nome: "William Bruno",
    idade: 35,
    foiAluno: true

}

const arrayObjetos = [objVinicius, objWilliam];

objWilliam.altura = 1.70;
objWilliam.idade = 28;
delete objWilliam.foiAluno;



// console.log(objVinicius);
// console.table(objWilliam);
// console.table(typeof objWilliam);
// console.table(typeof objWilliam.nome);
console.log(arrayObjetos);
console.table(arrayObjetos);
console.log(arrayObjetos[1].nome);
console.log(arrayObjetos[1].nome.length); //objeto quando pega para sair para outra linguagem ele vira string

const strJSON = JSON.stringify(arrayObjetos) ;
console.log(strJSON);

//https://jsonlint.com/ (Link para validar uma string JSON)

const arrayObjJSON = JSON.parse(strJSON);
console.log(arrayObjJSON);
console.table(arrayObjJSON);
