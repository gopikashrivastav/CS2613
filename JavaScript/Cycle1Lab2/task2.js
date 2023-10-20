
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


const prompt = require('prompt-sync')({sigint: true});
console.log('Select a command: n: Check a value');
let readVal =  (prompt(''));

if(readVal=='n'){
    target = Number(prompt('Enter a value'));
    let status = is_factorial(target);
    if(status<0){
        console.log(target + "is a negative number");

    }
    else if(status==0){
        console.log(target + "is not a factorial of any number");
    }
    else{
        console.log(target + "is the factorial of" + status);
    }
    
}





