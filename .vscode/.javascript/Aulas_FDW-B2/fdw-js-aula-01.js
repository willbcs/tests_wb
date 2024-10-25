// "use strict";

// // Comentário
// /* Comentário 
// de multiplas linhas
// */

// console.log("Hello World");

// const n3 = 0;
// let n1 = 3;
// let n2 = 5;
// let s = n1 + n2;
// console.log(`A soma é ${s}`);

// if (s==8)
// {
//    let k = 100;
//    console.log(`A variável "k" possui o valor de ${k}.`);
// }

// let nome = "Vinicius Teixeira de Lima", idade = 19, foiAluno = true, altura;

//  console.log(`Nome: ${nome}`);
//  console.log(`Idade: ${idade}`);
//  console.log(`Foi Aluno? ${foiAluno}`);

let p1 = 8, p2 = 7.5, media, conceito, resultado;

media = (p1 + 2*p2)/3;

if (media >= 5)
{
    resultado = "aprovado"
}
else
{
    resultado = "de exame"
}

if (media >= 9)
{
   conceito = "A"
}
else if (media >= 7)
{
    conceito = "B"
} 
else if (media >= 5)
{
    conceito = "C"
}
else if (media >= 2)
{
    conceito = "D"
}
else
{
    conceito = "C"
}

console.log(`A média do aluno é ${media.toFixed(2)} e ele está ${resultado} com conceito ${conceito}.`);






