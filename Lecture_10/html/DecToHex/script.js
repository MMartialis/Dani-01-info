function convert(){                                 // create a fuction which has no inputs
    let imp = document.getElementById("dec");
    let decimalnumber=Number(imp.value);            // casting the string to intiger and putting into the variable
    let hexnumb = decimalnumber.toString(16);
    document.getElementById("result").innerText = hexnumb;

}