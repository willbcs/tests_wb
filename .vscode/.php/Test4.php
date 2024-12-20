<?php 

function valor($mensagem)
{
    while (true)
    {
        $num1 = readline($mensagem);
        try
        {
            $num_1 = (int) $num1;
            if ($num_1 >0)
            {
                return $num_1;
            }
            else
            {
                echo "Digite um valor maior que zero!";

            }

        } 
        catch (Exception $e)
        {
            echo "Digite um número válido";
        }
    }
}

function Numeros()
{

    $soma = 0;
    $maior = PHP_INT_MIN; 
    $menor = PHP_INT_MAX; 
    $numero = [];

    for ($i = 0; $i < 20; $i ++)
    {
        $num = valor("Digite um número inteiro e positivo: ");
        $numero [] = $num;
        $soma += $num;

        $maior = ($num > $maior) ? $num : $maior;
        $menor = ($num < $menor) ? $num : $menor;
                
    }
    return [
        'soma' => $soma,
        'maior' => $maior,
        'menor' => $menor,
        'numeros' => $numero
    ];

}

function Med_Mai() 
{
    $resultado = Numeros();

    $media = $resultado['soma'] / count($resultado['numeros']);

    echo "Soma dos números: " . $resultado['soma'] . PHP_EOL;
    echo "Maior número: " . $resultado['maior'] . PHP_EOL;
    echo "Menor número: " . $resultado['menor'] . PHP_EOL;
    echo "Média dos números: " . $media . PHP_EOL;
    echo "Números digitados: " . implode(", ", $resultado['numeros']) . PHP_EOL;
}

Med_Mai();


?>