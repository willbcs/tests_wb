"use strict";

const gerarCPF = document.getElementById("gerarCPF");
const limpar = document.getElementById("limpar");
const CPF = document.getElementById("CPF");

function gerarNoveNumeros() 
{
    const nove_numeros = [];
    for (let i = 0; i < 9; i++) {
        const numeroAleatorio = Math.floor(Math.random() * 10); // Gera um número entre 0 e 9
        nove_numeros.push(numeroAleatorio);
    }
    return nove_numeros;
}

function criar_penultimo_numero() 
{
    const nove_digitos = gerarNoveNumeros();
    let contadord1 = 10;
    let resultado = 0;
    let penultimo_digito = 0;
    for (let i = 0; i < nove_digitos.length; i++) {
        resultado += (nove_digitos[i] * contadord1);
        contadord1 -= 1;
    }
    penultimo_digito = ((resultado * 10) % 11 > 9) ? 0 : (resultado * 10) % 11;
    nove_digitos.push(penultimo_digito);

    return nove_digitos;
}

function criar_ultimo_digito() 
{
    let dez_digitos = criar_penultimo_numero();
    let contadord2 = 11;
    let resultado = 0;
    let ultimo_digito = 0;
    for (let i = 0; i < dez_digitos.length; i++) {
        resultado += (dez_digitos[i] * contadord2);
        contadord2 -= 1;
    }
    ultimo_digito = ((resultado * 10) % 11 > 9) ? 0 : (resultado * 10) % 11;
    dez_digitos.push(ultimo_digito);

    return dez_digitos;
}

function formatarCPF(cpfArray) 
{
    const cpf = cpfArray.join('');
    return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
}

function gerar_onClick() 
{
    const cpfArray = criar_ultimo_digito();
    CPF.innerText = formatarCPF(cpfArray);
}

function limpar_onClick() 
{
    CPF.innerText = "";
}

gerarCPF.addEventListener("click", gerar_onClick);
limpar.addEventListener("click", limpar_onClick);
