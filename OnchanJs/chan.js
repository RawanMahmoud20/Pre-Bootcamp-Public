function chooseLunch(element) {
    if (element.value !== "") {
        alert("لقد اخترت: " + element.value);
    }
}


var nameTag = document.querySelector("#name-tag");

    function setName(element) {
        console.log(element.value);        
        nameTag.innerText = element.value;
    }


    function onSelectLanguage(elem) {
    var outputSpan = document.querySelector("#language_output");
    
    // الشروط لتغيير النص المعروض بناءً على القيمة (Value)
    if (elem.value === "js") {
        outputSpan.innerText = "JavaScript";
    } else if (elem.value === "py") {
        outputSpan.innerText = "Python";
    } else if (elem.value === "csharp") {
        outputSpan.innerText = "CSharp";
    } else if (elem.value === "#") {
        outputSpan.innerText = "";
    }
}

function oninputChange(elem) {
    var outputSpan = document.querySelector("#OutputName");
    outputSpan.innerText = elem.value;
}