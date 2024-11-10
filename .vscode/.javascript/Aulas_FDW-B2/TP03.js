// Questão 1: 
const arr = [];

arr.unshift("Rafaela");// Adiciona "Rafaela" no início -> ["Rafaela"]
arr.push("Marcelo");// Adiciona "Marcelo" no final -> ["Rafaela", "Marcelo"]
arr.splice(1, 1, "Bianca", "Ricardo", "Marcela"); // Remove "Marcelo" e adiciona "Bianca", "Ricardo", "Marcela" no índice 1 -> ["Rafaela", "Bianca", "Ricardo", "Marcela"]
arr.splice(0, 0, "Carlos");// Adiciona "Carlos" no início -> ["Carlos", "Rafaela", "Bianca", "Ricardo", "Marcela"]
arr.splice(2, 1);// Remove "Bianca" no índice 2 -> ["Carlos", "Rafaela", "Ricardo", "Marcela"]
arr.pop();// Remove o último elemento "Marcela" -> ["Carlos", "Rafaela", "Ricardo"]
arr.shift();// Remove o primeiro elemento "Carlos" -> ["Rafaela", "Ricardo"]

console.log(arr);// Resultado final: ["Rafaela", "Ricardo"]

// Questão 2: letra a)
function contaOcorrencias(array, elemento) {
    let contador = 0;
    for (let item of array) 
    {
        if (item === elemento) contador++;
        
    }
    return contador;
}

const arr2 = ["William", "Bianca", "William", "Ricardo", "William"];
console.log();
console.log("Letra a)");
console.table(arr2);
console.log("Quantos 'William'?", contaOcorrencias(arr2, "William"));

// No meu exemplo a resposta será 3

//Letra b)
function alteraElemento(array, elemento, substituto)
{
    let indice = 0;
    let cont = 0;
    for (let item of array)
    {
        if (item === elemento)
        {
            array.splice(indice, 1, substituto);
            cont++
        }
        
        indice++;

    }
    return (cont > 0) ? true : false

}
console.log();
console.log("Letra b)");
console.log("Houve substituições?", alteraElemento(arr2, "William", "William Bruno"));
console.table(arr2);

//Letra c)
function incluirElemento (array, indice, elemento)
{

    if (indice <= (array.length - 1) && (elemento != null))
    {
        array.splice(indice, 0, elemento);
        return array
    }
    return false
}
console.log();
console.log("Letra c)");
console.table(incluirElemento(arr2, 3, "Alexandre"))

//letra d)
const arr3 = ["William", "Bianca", "william", "Ricardo", "WILLIAM"];
function contaOcorrencias(array, elemento) {
    let contador = 0;
    for (let item of array) 
    {
        if (item.toLowerCase() === elemento.toLowerCase()) contador++;
        
    }
    return contador;
}
console.log();
console.log("Letra d)");
console.table(arr3);
console.log("Quantos 'William' diferentes?", contaOcorrencias(arr3, "William"));

//letra e)
const arr4 = ["William Bruno", "Bianca", "josé william", "Ricardo", "WILLIAM BONNER"];
function contaOcorrencias(array, elemento) {
    let contador = 0;
    for (let item of array) 
    {
        if (item.toLowerCase().includes(elemento.toLowerCase())) contador++;
        
    }
    return contador;
}
console.log();
console.log("Letra d)");
console.table(arr4);
console.log("Quantos 'William' diferentes?", contaOcorrencias(arr4, "William"));


