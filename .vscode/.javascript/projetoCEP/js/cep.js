"use strict";

const cep = document.getElementById("cep");
const btnPesquisar = document.getElementById("btnPesquisar");
const saida = document.getElementById("saida");
const URL = `https://viacep.com.br/ws/`

function obterCep()
{
    
    return cep.value;

}

async function onClick() 
{
    try{

        const urlCEP = `${URL}${obterCep()}/json/`;
        const resposta = await fetch(urlCEP);
        const dadosJSON = await resposta.json(); //Objeto
        saida.innerText = apresentarDadosCep(dadosJSON);
        
    } catch(err) {

        saida.textContent = `Erro ao buscar CEP.`;

    }
}

function apresentarDadosCep(dados)
{   
    if (!dados["erro"])
    {
        let cep = dados["cep"];
        let logradouro = dados["logradouro"];
        let complemento = dados["complemento"];
        let localidade = dados["localidade"];
        let uf = dados["uf"];

        
        return `CEP: ${cep}\nLogradouro: ${logradouro}\nComplemento: ${complemento}\nLocalidade: ${localidade}\nUF: ${uf}`;

    } 
    else
    {

        return "CEP inexistente!"

    }

}

btnPesquisar.addEventListener("click", onClick);