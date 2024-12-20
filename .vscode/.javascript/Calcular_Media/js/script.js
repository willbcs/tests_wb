"use strict";

const nome = document.getElementById("nome");
const p1 = document.getElementById("p1");
const p2 = document.getElementById("p2");
const btnCalcular = document.getElementById("btnCalcular");
const btnSalvar = document.getElementById("btnSalvar");
const btnExibir = document.getElementById("btnExibir");
const btnApagar = document.getElementById("btnApagar");

const saida = document.getElementById("saida");
const arr =[];

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
// function exibirSaida(mensagem) 
// {
//     mensagem = mediaCalculada.toFixed(2);
//     return mensagem

// }

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

function dados_aluno()
{

    if (parseFloat(saida.textContent))
        {   
            let status =''
            let media_valida = saida.textContent
            if (media_valida >= 5) status = "Aprovado"
            else if (media_valida <= 3 ) status = "Reprovado"
            else status = "Recuperação"
            const aluno = {
                aluno_nome: nome.value,
                media: saida.textContent,
                situacao: status
            }
            return aluno          
        }
    else
        {
            return null
        }

}

function calcul_onClick()
{
    const notaP1 = arredondarNota(p1.value);
    const notaP2 = arredondarNota(p2.value); // por .value para mostrar os valores. | Por o + na frente o torna ele número | pondo o objeto number como "Number(p1.Value);"
    // const mediaCalculada = CalcularMedia(obterP1(), obterP2()); | outra forma de fazer com menos linhas de programa
    // exibirSaida(saida.textContent)
    exibirSaida(validarNota(notaP1, notaP2));
    // saida.textContent = "Olá, Mundo!" ;
    
}

function salvar_onClick()
{
    if (dados_aluno())
    {
        arr.push(dados_aluno());
        saida.textContent = "Média Salva!"
        return saida.textContent;
    }
    else
    {
        saida.textContent = "Não há dados válidos para salvar!"
        return saida.textContent
    }
}

function exibir_onClick()
{

    if (arr.length === 0)
        {
            saida.textContent = "Não há dados para exibir!";
            return saida.textContent;
        }
    else
    {

        const formatar_saida = arr.map((aluno, index) => `Aluno ${index+1}: ${aluno.aluno_nome} / Média: ${aluno.media} / Situação: ${aluno.situacao}`).join('\n');
        saida.innerText = formatar_saida
        return saida.innerText

    }
}

function apagar_onClick()
{

    arr.length = 0
    saida.textContent = "Lista apagada!"
    return saida.textContent

}
/* Manipuladores de eventos ------------------------------ após escrever a ação primeiro entre (), escrever a função após a , e dentro dela o que ela deve fazer*/

btnCalcular.addEventListener("click", calcul_onClick);
btnSalvar.addEventListener("click", salvar_onClick);
btnExibir.addEventListener("click", exibir_onClick);
btnApagar.addEventListener("click", apagar_onClick);


/*saida.textContent = "Oi, mundo!"; textcontent imbute a string pedida no elemento HTML que ele está referenciando */