"use strict";



const p1 = document.getElementById("p1");
const p2 = document.getElementById("p2");
const btnCalcular = document.getElementById("btnCalcular");
const saida = document.getElementById("saida");

/* Outra forma de fazer as varíaveis abaixo é escrever dentro de um objeto. 

Exemplo:

const elementos = {
    p1: document.getElementById("p1");
    p2: document.getElementById("p2");
}

e para chamar algum elemento do objeto basta escrever:

elementos.p1
*/


/* Funções ----------------------------------- Nesse caso precisa por um nome na função */
function exibirSaida(mensagem) 
{
    mensagem = mediaCalculada.toFixed(2);
    return mensagem

}

function obterNotas(nota) 
{

   return parseFloat(nota); 

}


function validarNota(nota1, nota2){
    if (Number(nota1 && nota2))
    {
        return (nota1>=0 && nota1 <=10 && nota2>=0 && nota2 <=10) ? ((nota1+2*nota2)/3).toFixed(2) : "Não é uma nota válida!"
        
    } 
    else return "Digite apenas números!"

}

function arredondarNota(nota)
{
    let decimal = (obterNotas(nota) - parseInt(obterNotas(nota)))
    if (decimal >=0 && decimal < 0.25) return parseInt(obterNotas(nota))
    if (decimal >= 0,25 && decimal < 0.75) return parseInt(obterNotas(nota)) + 0.5
    else return parseInt(obterNotas(nota)) + 1

}

function exibirSaida(mensagem)
{
    saida.textContent = mensagem 
    return saida.textContent

}

function onClick()
{
    const notaP1 = arredondarNota(p1.value);
    const notaP2 = arredondarNota(p2.value); // por .value para mostrar os valores. | Por o + na frente o torna ele número | pondo o objeto number como "Number(p1.Value);"
    // const mediaCalculada = CalcularMedia(obterP1(), obterP2()); | outra forma de fazer com menos linhas de programa
    // exibirSaida(saida.textContent)
    exibirSaida(validarNota(notaP1, notaP2));
    // saida.textContent = "Olá, Mundo!" ;
    
}

/* Manipuladores de eventos ------------------------------ após escrever a ação primeiro entre (), escrever a função após a , e dentro dela o que ela deve fazer*/

btnCalcular.addEventListener("click", onClick);

/*saida.textContent = "Oi, mundo!"; textcontent imbute a string pedida no elemento HTML que ele está referenciando */