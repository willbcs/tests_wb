//Questão 01:
function padraoABNT(nome) 
{
    let iniciais = "";

    const partesNome = nome.trim().split(" ");

    const ultimoNome = partesNome.pop().toUpperCase();

    for (let i = 0; i < partesNome.length; i++) 
    {
        let inicial = partesNome[i].charAt(0).toUpperCase(); // Pega a primeira letra de cada parte
        iniciais += inicial + ". "; // Adiciona a inicial com um ponto
    }

    return `${ultimoNome}, ${iniciais}`;
}

console.log(padraoABNT("William Bruno Carlos Silva")); 

// Questão 02:
