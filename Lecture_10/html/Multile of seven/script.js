function isMultipleOf7(){
    let imp = document.getElementById("decimalInput");
    let decimalnumber=Number(imp.value); 
    if (decimalnumber %7 == 0){
        document.getElementById("result").textContent = "yes";
    }
    else{
        document.getElementById("result").textContent = "not";
    }
}