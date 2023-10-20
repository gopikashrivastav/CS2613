
const prompt = require('prompt-sync')({sigint: true});
var st = prompt("Enter string");
var stArr = st.split(',');
console.log(stArr);

var age = parseInt(stArr[0]);
var height = parseInt(stArr[1]);
var weight = parseInt(stArr[2]);
var mood = stArr[3];
var view = stArr[4];

function validTime(){
    var now = new Date(); 
    var datetime = "Current date and time " + now.getDate() + "/"
                + (now.getMonth()+1)  + "/" 
                + now.getFullYear() + " @ "  
                + now.getHours() + ":"  
                + now.getMinutes() + ":" 
                + now.getSeconds();
    if(11 <= now.getHours() <= 23){
        console.log(now.getHours() + ":" 
        + now.getMinutes(), 
        "The amusement park is OPEN! Recommended Rides:");

}
}

function rideSelection()
{
    var checkRide = 0;
    mood = (mood.toLowerCase()).trim();
    view = (view.toLowerCase()).trim();

    if(age<4){

        checkRide = -1;
        
    }
    if(age>=4 , mood=="calm"){
        if(age<12){
            console.log("Merry-Go-Round");
        }
        if(age>10, height>=152.4, view=="yes"){
            console.log("Ferris Wheel");   

        }
    }
    if(age>=4, mood=="exciting"){
        if(height>=152.4, weight>36.29){
            console.log("Tilt-A-Whirl");
        }
        if(age>10, height>=152.4)
            if(view=="yes"||view=="n/a"){
                console.log("Rollercoaster");
            }
            if(weight>=36.29){
                console.log("Bumper Cars");
            }
    }
}

validTime();
rideSelection();

