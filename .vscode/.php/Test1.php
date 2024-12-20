<?php
function formato_valido($mensagem)
{
    while (true)
    {
        $numero = readline($mensagem);
        if (strlen($numero) == 8 && ctype_digit($numero))
        {
            return (int)$numero;
        }

        else
        {
            echo "\nA senha deve conter 8 números positivos\n";
        }

    }    
}

function senha_conta()
{
    $senha = 16041989;
    $tentativas = 3;

    while ($tentativas >= 0)
    {
        $numero = formato_valido("Digite sua senha de 8 números positivos:\n");

        if ($numero == $senha)
        {
            echo "\nAcesso concedido! Bem-vindo!";
            break;
        }
        else
        {
            $tentativas--;
            echo "\nSenha incorreta. Você tem mais $tentativas tentativa(s)\n";
        }
        if ($tentativas == 0)
        {
            echo "\nTentativas excedidas! Adeus!";
            break;
        }
    }
}
senha_conta();
?>