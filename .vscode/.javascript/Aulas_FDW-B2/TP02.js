function qualASaida(num1=0, num2=0, num3=true) {
    let exp;
    if (num3==true) 
    {
        exp=num1+num2;
    } 
    else 
    {
        if (num1==num2) 
        {
            exp=num1**2;
        } 
        else if (num1>num2) 
        {
            exp=num1-num2;
        } 
        else 
        {
            exp=num2/2;
        }
    }
    return exp;
    }
    console.log(qualASaida(3, 6, true));
    console.log(qualASaida(5, 1, false));
    console.log(qualASaida(2, 4, true));
    console.log(qualASaida(0, 5, true));
    console.log(qualASaida(false));

    