<?php
function temp_fahrenheit($mensagem)
{
    while (true)
    {
        $far = readline($mensagem);
        
        if (is_numeric($far))
        {
            return (float) $far;
        }

        else
        {
            echo "Caracteres inválidos foram digitados";
        }

    }   
}

function converter()
{
    while (true) 
    {
        $temp_f = temp_fahrenheit("Digite a temperatura em Fahrenheit:\n");
        $temp_c = (5 * ($temp_f - 32) /9);
        echo "A temperatura em Celsius é: " .number_format($temp_c, 2)."°\n";
        
        echo "Deseja continuar as conversões?";
        $end = strtolower(readline("Digite 's' para sair ou aperte qualquer tecla para continuar!\n"));

        if ($end == "s")
        {
            echo "Até logo!";
            break;
        }
    }
}
converter();
?>