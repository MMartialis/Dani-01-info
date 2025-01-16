document.addEventListener("DOMContentLoaded", function(){   /* This callback function will run when all elements of the page are loaded*/
    var paragElement = document.getElementById("text");   // find the element on the page with id "text"

    var wholeText = paragElement.textContent;   // select the contet of that element
    var words = wholeText.split(" ");      //  Devided the text into words, the diviseer is a space " "
    paragElement.innerHTML="";      // delete everything inside the element
    words.forEach(function(word){  // for every word run the function
        var myspanel = document.createElement("span");  // create a new <span></span> element 
        myspanel.textContent=word + " ";  // write the word plus a space inside the span element
        paragElement.appendChild(myspanel);     // put this into the p element

    });
    paragElement.addEventListener("click", function(event){  // every time the user click the p elemnt 
        if (event.target.tagName === "SPAN"){       // we check that we clicked on a span
            event.target.classList.add("highlight"); // if yes add class highlight
        }
    })

});