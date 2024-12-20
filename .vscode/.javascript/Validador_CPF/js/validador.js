"use strict"

const saida = document.getElementById("saida");
const limpar = document.getElementById("limpar");
const validar = document.getElementById("validar");
const digiteCPF = document.getElementById("digiteCPF");

function validarEntradaCPF(event) 
{
    const input = event.target;
    input.value = input.value.replace(/\D/g, ''); 
}

function validar_penultimo_digito(cpf) 
{
    const nove_digitos = cpf.slice(0, 9);
    let contadord1 = 10;
    let resultado = 0;
    for (let i = 0; i < nove_digitos.length; i++) 
    {
        resultado += parseInt(nove_digitos[i]) * contadord1;
        contadord1 -= 1;
    }
    let penultimo_digito = ((resultado * 10) % 11 > 9) ? 0 : (resultado * 10) % 11;
    return penultimo_digito;
}

function validar_ultimo_digito(cpf) 
{
    const digitos = cpf.slice(0, 10);
    let contadord2 = 11;
    let resultado = 0;
    for (let i = 0; i < digitos.length; i++) 
    {
        resultado += parseInt(digitos[i]) * contadord2;
        contadord2 -= 1;
    }
    let ultimo_digito = ((resultado * 10) % 11 > 9) ? 0 : (resultado * 10) % 11;
    return ultimo_digito;
}

function validador(cpf) 
{
    if (cpf.length !== 11) 
    { 
        saida.innerText = "O CPF deve conter 11 números!";
        saida.style.color ="navy"
        return saida.innerText;
    }
    let penultimo_digito_calculado = validar_penultimo_digito(cpf);
    let penultimo_digito_original = parseInt(cpf[9]);
    let ultimo_digito_calculado = validar_ultimo_digito(cpf);
    let ultimo_digito_original = parseInt(cpf[10]);

    let sucesso = ((penultimo_digito_calculado === penultimo_digito_original) && (ultimo_digito_calculado === ultimo_digito_original));

    if (sucesso) 
    {
        saida.innerText = "O CPF é VÁLIDO!";
        saida.style.color = "green"; 

    }
    else 
    {
        saida.innerText = "O CPF é INVÁLIDO!";
        saida.style.color = "red"; 
    }
    return saida.innerText;
    
}

function validar_onClick() 
{
    validador(digiteCPF.value);
}

function limpar_onClick() 
{
    saida.innerText = "";
    digiteCPF.value = "";
}

validar.addEventListener("click", validar_onClick);
limpar.addEventListener("click", limpar_onClick);
digiteCPF.addEventListener("input", validarEntradaCPF);