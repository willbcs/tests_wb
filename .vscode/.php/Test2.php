<?php

function valor($mensagem)
{
    while (true)
    {
        $v = readline($mensagem);
        
        if (is_numeric($v) && $v > 0)
        {
            return (float)$v;
        }
        else
        {
            echo "Inválido. Digite apenas números e um valora maior que zero";
        }
    }
}

function Menu()
{
    while (true)
    {
        echo "\nESCOLHA A OPÇÃO DE PAGAMENTO DESEJADA:";
        echo "\n1 - DINHEIRO\n";
        echo "2 - À VISTA NO CARTÃO\n";
        echo "3 - PARCELADO NO CARTÃO EM 2X\n";
        echo "4 - PARCELADO NO CARTÃO EM 3X OU MAIS\n";
        echo "5 - SAIR\n";
        $pagamento = readline("Escolha uma opção:\n");

        if (ctype_digit($pagamento) && (int)$pagamento > 0 && (int)$pagamento < 6)
        {
            return $pagamento;
        }
        else
        {
            echo "Inválido! Escolha uma opção das opções válidas!";
        }
    }
}

function Pagamento()
{
    while (true)
    {    
        $preco = valor("Digite o valor do produto:\n");
        $opcao = Menu();

        if ($opcao == 1)
        {
            $total_1 = $preco - ($opcao * 0.15);
            echo "\nÀ vista e em dinheiro, o valor total é de R$$total_1";
        }
        elseif ($opcao == 2)
        {
            $total_2 = $preco - ($opcao * 0.1);
            echo "\nÀ vista no cartão, o valor total é de R$$total_2";
        }
        elseif ($opcao == 3)
        {
            echo "\nÀ vista e em dinheiro, o valor total é de R$$preco";
        }
        elseif ($opcao == 4)
        {
            $total_3 = $preco - ($opcao * 0.1);
            echo "\nParcelado em 3x ou mais, o valor total é de R$total_3";
        }
        else
        {
            echo "Até breve!";
            break;
        }

        echo "\nDeseja realizar uma nova operação?";
        $fim = readline("Digite 's' para sair ou qualquer tecla para continuar:\n");

        if (strtolower($fim) === 's') 
        {
            echo "Saindo...\n";
            break; 
        } 
        else 
        {
            echo "Continuando...\n";
        }
    }
}
Pagamento()
?>