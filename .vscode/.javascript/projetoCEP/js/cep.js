"use strict";

const cep = document.getElementById("cep");
const btnPesquisar = document.getElementById("btnPesquisar");
const btnSalvar = document.getElementById("btnSalvar");
const btnExibir = document.getElementById("btnExibir");
const saida = document.getElementById("saida");
const URL = `https://viacep.com.br/ws/`
const arr = []

function obterCep()
{
    
    return cep.value;

}

async function pesquisar_onClick() 
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

function salvar_onClick()
{
    const localidade = saida.innerText.match(/Localidade: ([^\n]*)/);

    if (localidade)
    {
        arr.push(localidade[1]);
        saida.textContent = "Localidade salva com sucesso!"
    }
    else
    {
        saida.textContent = "Não há Localidade válida para salvar"
    }
}

function exibir_onClick() {
    if (arr.length === 0) {
        saida.textContent = "Não existem localidades salvas na lista!";
        return;
    }

    // Contabiliza a frequência de cada localidade
    const frequencias = arr.reduce((contagem, localidade) => {
        contagem[localidade] = (contagem[localidade] || 0) + 1;
        return contagem;
    }, {});

    // Calcula o percentual para cada localidade
    const totalCeps = arr.length;
    const porcentagens = Object.entries(frequencias)
        .map(([localidade, count]) => `${count} CEP's de ${localidade} = Equivale a ${(count / totalCeps * 100).toFixed(2)}% da lista!`)
        .join("\n");

    saida.innerText = porcentagens;
}

btnPesquisar.addEventListener("click", pesquisar_onClick);
btnSalvar.addEventListener("click", salvar_onClick);
btnExibir.addEventListener("click", exibir_onClick);