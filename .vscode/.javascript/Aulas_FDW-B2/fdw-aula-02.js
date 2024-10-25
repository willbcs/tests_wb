"use strict";

// function Media(p1, p2)
// {
//     let media =(p1 + 2*p2)/3;
//     return media.toFixed(2);

// }

// console.log("Média do aluno 1:", Media(5, 8));
// console.log("Média do aluno 2:", Media(6, 7.5));
// console.log("Média do aluno 3:", Media(3, 4.5));

// // let p1, p2, media;
// // p1=5, p2=8;
// // media=(p1+2*p2)/3;
// // console.log("Media do aluno 1:", media.toFixed(2));

// // p1=6, p2=7.5;
// // media=(p1+2*p2)/3;
// // console.log("Media do aluno 2:", media.toFixed(2));

// // p1=3.5, p2=4.5;
// // media=(p1+2*p2)/3;
// // console.log("Media do aluno 3:", media.toFixed(2));

// let MediaAluno4 = Media(8, 5.5);
// console.log("Média do aluno 4:", MediaAluno4);

// // Expressão de função

// let soma = function (n1=0, n2=0)
// {
//     let soma = (n1 + n2);
//     return soma;
// };

// console.log("A soma dos elementos é", soma(5, 8));
// console.log("A soma dos elementos é", soma());
// console.log("A soma dos elementos é", soma(5));

for (let i = 0; i <= 10; i++)
{
    
    console.log(i);
    
}

console.log();

let i = 0;
while(i < 10)
{
    i++
    console.log(i)
}

console.log();

let j = 0;
do
{
    j = j + 2
    console.log(j);

}while(j < 10);



function numeroParImpar(num)
{

    if (num % 2 == 0)
    {
        return "Par"
    }
    else
    {
        return "Ímpar" 
    } 

}
console.log("O número 7 é:", numeroParImpar(7));

let numeroParImpar = (num) => (num%2==0)? "Par" : "Ímpar";






console.log("O número 10 é:", numeroParImpar(10));


let soma = function (n1=0, n2=0)
{
    let soma = (n1 + n2);
    return soma;
};

let somav2 = (n1=0, n2=0) => n1 + n2;


