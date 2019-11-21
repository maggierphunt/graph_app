function validateForm(form) {
    var x = document.forms["Form"]["value_1"].value;
    if(form.inputfield.value == "") {
        alert("Error: Input is empty!");
        form.inputfield.focus();
        return false;
     }
    if (x == "number") {
       alert("Please only enter numerical values.");
       return false;}
    var x = document.forms["Form"]["value_2"].value;
    if (x == "number") {
       alert("Please only enter numerical values.");
       return false;}
    var x = document.forms["Form"]["value_3"].value;
    if (x == "number") {
       alert("Please only enter numerical values.");
       return false;}
    var x = document.forms["Form"]["value_4"].value;
    if (x == "number") {
       alert("Please only enter numerical values.");
       return false;}
       var x = document.forms["Form"]["value_5"].value;
       if (x == "number") {
          alert("Please only enter numerical values.");
          return false;}
       var x = document.forms["Form"]["value_6"].value;
       if (x == "number") {
          alert("Please only enter numerical values.");
          return false;}
       var x = document.forms["Form"]["value_7"].value;
       if (x == "number") {
          alert("Please only enter numerical values.");
          return false;}
       var x = document.forms["Form"]["value_8"].value;
       if (x == "number") {
          alert("Please only enter numerical values.");
          return false;}
        var x = document.forms["Form"]["value_9"].value;
        if (x == "number") {
            alert("Please only enter numerical values.");
            return false;}        
        var x = document.forms["Form"]["value_10"].value;
        if (x == "number") {
            alert("Please only enter numerical values.");
            return false;}
        
        var x = document.forms["Form"]["value_11"].value;
        if (x == "number") {
            alert("Please only enter numerical values.");
            return false;}
        
        var x = document.forms["Form"]["value_12"].value;
        if (x == "number") {
            alert("Please only enter numerical values.");
            return false;}

            return true;}