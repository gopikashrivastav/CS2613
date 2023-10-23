function sharedFactors(val1, val2){
    let factors = []
    for(let i = 2; i <= (val1||val2); i++)
    {
        if((val1%i==0),(val2%i==0)){
            factors[i] = i;

        }
    }
    return factors;
}

list1 = sharedFactors(28,42)
console.log(list1);