arr = ["hello", "world", "test"];
data = "";

function writeStrings(arr, st){
    //creating whole string
    for(let i =0; i < length(arr); i++){
        data = data+arr[i];
    }
    f = open("Output.txt", w);
    
    print(arr)
}


writeStrings(arr, "output.txt")