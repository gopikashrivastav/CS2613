
function factorial(num){
    let fact=1;
    for(let i = num; i >1; i--){
        fact = fact*i; 
    }
    return fact;
}

function is_factorial(num){

    let check = 1;
    let val = 1;
    let result =0;

    if(num<0){
        return -1;
    }

    else{
        for(let i = 1; i < num; i++){
            check=factorial(i);
            if(check==num){
                result = 1;
                val = i;
                break;
            }
            else{
                result = 0;
            }
        
        }
        if(result==1){
            return val;
        }
        else{
            return 0;
        }

    }
}


let x = is_factorial(720);
console.log("720 is the factorial of", x);

