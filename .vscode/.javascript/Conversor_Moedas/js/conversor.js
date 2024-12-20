"use strict"
const saida = document.getElementById("saida");
const valor = document.getElementById("valorReais");
const converter = document.getElementById("converter");
const limpar = document.getElementById("limpar");

const saidaDolarUs = document.getElementById("dolarUS");
const saidaEuro = document.getElementById("euro");
const saidaLibra = document.getElementById("libra");
const saidaIene = document.getElementById("iene");
const saidaDolarAUS = document.getElementById("dolarAUS");
const saidaDolarCND = document.getElementById("dolarCND");
const saidaYuan = document.getElementById("yuan");
const saidaFranco = document.getElementById("franco");
const saidaPeso = document.getElementById("peso");

const API_KEY = "567c400e40df803fa1d650f5";
const BASE_URL = `https://v6.exchangerate-api.com/v6/${API_KEY}/latest/`;

valor.addEventListener("input", function () 
{
    this.value = this.value.replace(/[^0-9.]/g, "");
});

function limpar_onClick()
{

    saidaDolarUs.innerText = "-"
    saidaEuro.innerText = "-"
    saidaLibra.innerText = "-"
    saidaIene.innerText = "-"
    saidaDolarAUS.innerText = "-"
    saidaDolarCND.innerText = "-"
    saidaYuan.innerText = "-"
    saidaFranco.innerText = "-"
    saidaPeso.innerText = "-"

    valor.value = ""
    saida.textContent = ""

}

async function converter_onClick() 
{
    try{

        const urlConverter = `${BASE_URL}BRL`;
        const resposta = await fetch(urlConverter);
        const dadosJSON = await resposta.json(); //Objeto
        
        if (!dadosJSON["erro"] && (valor.value))
        {
            const cambio = apresentarDados(dadosJSON);

            saidaDolarUs.innerText = "$"+(cambio[0] * parseFloat(valor.value)).toFixed(2);
            saidaEuro.innerText = "€"+(cambio[1] * parseFloat(valor.value)).toFixed(2);
            saidaLibra.innerText = "£"+(cambio[2] * parseFloat(valor.value)).toFixed(2);
            saidaIene.innerText = "¥"+(cambio[3] * parseFloat(valor.value)).toFixed(2);
            saidaDolarAUS.innerText = "AU$"+(cambio[4] * parseFloat(valor.value)).toFixed(2);
            saidaDolarCND.innerText = "CA$"+(cambio[5] * parseFloat(valor.value)).toFixed(2);
            saidaYuan.innerText = "¥"+(cambio[6] * parseFloat(valor.value)).toFixed(2);
            saidaFranco.innerText = "CHF"+(cambio[7] * parseFloat(valor.value)).toFixed(2);
            saidaPeso.innerText = "AR$"+(cambio[8] * parseFloat(valor.value)).toFixed(2);

            saida.textContent = "Dados encontrados!"
        }
        else
        {
            saida.textContent = `Erro ao buscar dados!`;

        }
        
    } catch(err) {
        saida.textContent = `Erro ao buscar dados!`;
    }
}

function apresentarDados(dados)
{   
    
    let usd = dados['conversion_rates']['USD']
    let eur = dados['conversion_rates']['EUR']
    let gbp = dados['conversion_rates']['GBP']
    let jpy = dados['conversion_rates']['JPY']
    let aud = dados['conversion_rates']['AUD']
    let cad = dados['conversion_rates']['CAD']
    let cny = dados['conversion_rates']['CNY']
    let chf = dados['conversion_rates']['CHF']
    let ars = dados['conversion_rates']['ARS']
    

    return [usd, eur, gbp, jpy, aud, cad, cny, chf, ars]
   
}

converter.addEventListener("click", converter_onClick);
limpar.addEventListener("click", limpar_onClick);