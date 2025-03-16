<?php

function formato_valido($mensagem)
{
    while (true)
    {
        $numero = readline($mensagem);
        if (ctype_digit($numero))
        {
            return (int)$numero;
        }

        else
        {
            echo "\nVocê deve digitar somente números\n";
        }

    }    
}

function fibonacci()
{
    $a = 1; $b = 1;
    while (true)
    {
        $termos = formato_valido("Digite a quantidade de termos da sequência de Fibonacci que deseja visualizar:\n");

        if ($termos == 1)
        {
            echo "\nSequência de Fibonacci com 1 termo:\n$a";
            break;
        }
        elseif ($termos == 2)
        {
            echo "\nSequência de Fibonacci com 2 termos:\n$a, $b";
            break;
        }
        else
        {
            echo "\nSequência de Fibonacci com $termos termos: ";
            echo "$a, $b";
            for ($i=2; $i <= $termos - 1; $i++)
            {
                $next = $a + $b;
                echo ", $next";
                $a = $b; 
                $b = $next;
            }
            break;
        }
    }
}
fibonacci();
?>