"use strict";

const cidade = document.getElementById("cidade");
const btnBuscar = document.getElementById("btnBuscar");
const btnLimpar = document.getElementById("btnLimpar");
const saida = document.getElementById("saida");
const spanLongitude = document.getElementById("longitude");
const spanLatitude = document.getElementById("latitude");
const spanCandicao = document.getElementById("condicao");
const spanDescricao = document.getElementById("descricao");
const spanTemp = document.getElementById("temp");
const spansensT = document.getElementById("senset");
const spanTempMin = document.getElementById("tempmin");
const spanTempMax = document.getElementById("tempmax");
const spanUmidade = document.getElementById("umidade");
const spanVelVento = document.getElementById("velvento");
const spanPais = document.getElementById("pais");
const spanLocal = document.getElementById("local");

const API_KEY = '0d03d7398ca2f928b965ba5c593360f3'
const BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?';


function apresentarDados(dados)
{
    let longitude = dados["coord"]["lon"]
    let latitude = dados["coord"]["lat"]
    let condicao = dados["weather"][0]["main"]
    let descricao = dados["weather"][0]["description"]
    let temperatura = dados["main"]["temp"]
    let sensação_termica = dados["main"]["feels_like"]
    let temp_min = dados["main"]["temp_min"]
    let temp_max = dados["main"]["temp_max"]
    let umidade = dados["main"]["humidity"]
    let velocidade_vento = dados["wind"]["speed"]
    let pais_sigla = dados["sys"]["country"]
    let local_nome = dados["name"]

    return [longitude, latitude, condicao, descricao, temperatura, sensação_termica, temp_min, temp_max, umidade, velocidade_vento, pais_sigla, local_nome];
}

function selecao()
{
    const cidadeSelecionada = cidade.value;
    if (cidadeSelecionada) 
    {
        return cidadeSelecionada;
    } 
    else 
    {
        return null;
    }
}

async function buscar_onClick()
{   
    const selecao_cidade = selecao()
    
    if (selecao_cidade !== null)
    {
        try
        {

            const urlCEP = `${BASE_URL}q=${selecao_cidade}&appid=${API_KEY}&units=metric&lang=pt_br`;
            const resposta = await fetch(urlCEP);
            
            if (resposta.ok)
            {   
                const dadosJSON = await resposta.json(); 
                const info = apresentarDados(dadosJSON);

                spanLongitude.innerText = info[0];
                spanLatitude.innerText = info[1];
                spanCandicao.innerText = info[2];
                spanDescricao.innerText = info[3];
                spanTemp.innerText = `${info[4]} °C`;
                spansensT.innerText = `${info[5]} °C`;
                spanTempMax.innerText = `${info[6]} °C`;
                spanTempMin.innerText = `${info[7]} °C`;
                spanUmidade.innerText = `${info[8]}%`;
                spanVelVento.innerText = `${info[9]} m/s`;
                spanPais.innerText = info[10];
                spanLocal.innerText = info[11];
                
                saida.textContent = "Dados encontrados!";
                saida.style.color = "green"

            }
            else
            {
                saida.textContent = "Cidade não encontrada. Verifique o nome e tente novamente.";
                saida.style.color = "red"
            }
        } catch(err) {
            saida.textContent = "Erro ao buscar informações. Verifique sua conexão com a internet.";
            saida.style.color = "red"

        }
    }
    else 
    {
        saida.textContent = "Por favor, selecione uma cidade.";
        saida.style.color = "navy"

    }
}

function limpar_onClick()
{
    spanLongitude.innerText = "-";
    spanLatitude.innerText = "-";
    spanCandicao.innerText = "-";
    spanDescricao.innerText = "-";
    spanTemp.innerText = "-";
    spansensT.innerText = "-";
    spanTempMax.innerText = "-";
    spanTempMin.innerText = "-";
    spanUmidade.innerText = "-";
    spanVelVento.innerText = "-";
    spanPais.innerText = "-";
    spanLocal.innerText = "-";
    
    saida.textContent = "";
}

btnBuscar.addEventListener("click", buscar_onClick);
btnLimpar.addEventListener("click", limpar_onClick);
