var forms = ["container", "container-2", "container-3", "pred"];
var pointer = 0;
var submitBtn = document.getElementById("submit");
var predictions = document.getElementById("predictions")
var dataToSend = []
console.log('Working');

function InputCheck(inputValues) {
    for (const [key, value] of Object.entries(inputValues)) {
        if (value === "" || +value < 0 || +value > 100 || isNaN(+value)) {
            return false;
        }
    }
    return true;
}

function RadioCheck(radioValues){
    for (const [key, value] of Object.entries(radioValues)){
        if(value === "" || isNaN(+value) || value === null){
            return false;
        }
    }
    return true;
}

function CheckboxCheck(checkboxValues){
    var count = 0
    for (const [key, value] of Object.entries(checkboxValues)){
        if(value){
            count++;
        }
    }
    if(count === 2){
        return true;
    }
    else{
        return false;
    }
}

submitBtn.addEventListener("click", function() {
    if(pointer === 0){
        // Extracting input values
        const inputFields = document.querySelectorAll('.input-box input[type="number"]');
        const inputValues = {};
        inputFields.forEach(function(input) {
            inputValues[input.nextElementSibling.textContent.trim()] = input.value;
            // console.log(+input.value)
        });

        console.log("Input field values:", inputValues);
        if(InputCheck(inputValues)){
            dataToSend.push(inputValues)
            console.log(dataToSend);
            next();
        }
        else{
            alert("Enter The Marks in range of 0-100");
        }

    }

    else if (pointer === 1){
        // Extracting radio button values
        const psRadioButtons = document.querySelectorAll('.ps-radio input[name="Problem-Solving"]:checked');
        const creativityRadioButtons = document.querySelectorAll('.ps-radio input[name="creativity"]:checked');
        var psValue = null;
        var creativityValue = null;
        const radioValues = {
            "psval" : null,
            "cval" :null
        };

        if (psRadioButtons.length > 0) {
            psValue = psRadioButtons[0].value;
            radioValues["psval"] = psRadioButtons[0].value;
        }

        if (creativityRadioButtons.length > 0) {
            creativityValue = creativityRadioButtons[0].value;
            radioValues["cval"] = creativityRadioButtons[0].value;
        }

        // Displaying extracted values (for demonstration purposes)
        console.log("Problem-Solving value:", psValue);
        console.log("Creativity value:", creativityValue);
        if(RadioCheck(radioValues)){
            dataToSend.push(radioValues);
            console.log(dataToSend);
            next();
        }
        else{
            alert("Rate Your Problem-Solving and Creativity");
        }

    }

    else if(pointer === 2){
        // Extracting checkbox values
        const checkboxes = document.querySelectorAll('.checkbox-wrapper-47 input[type="checkbox"]');
        const checkboxValues = {};
        checkboxes.forEach(function(checkbox) {
            // console.log(checkbox)
            checkboxValues[checkbox.nextElementSibling.textContent.trim()] = checkbox.checked;
            // inputValues[checkbox.nextElementSibling.textContent.trim()] = checkbox.checked
            
        });

        console.log("Checkbox values:", checkboxValues);

        if(CheckboxCheck(checkboxValues)){
            dataToSend.push(checkboxValues)
            console.log(dataToSend)
            API()
            next();

        }
        else{
            alert("Choose Your Top 2 skills ");
        }

    }

    else{
        next()
    }
});

function next(){
        // Transitioning between form sections
        var curr = forms[pointer];
        var next = forms[(pointer + 1) % forms.length];
    
        var currentElement = document.querySelector("." + curr);
        var nextElement = document.querySelector("." + next);
    
        currentElement.style.opacity = '0';
        setTimeout(function() {
            currentElement.style.display = 'none'; 
            nextElement.style.display = 'flex'; 
    
            setTimeout(function() {
                nextElement.style.opacity = '1';
            }, 50);
        }, 500); 
    
        pointer = (pointer + 1) % forms.length;
}

function API(){
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Prediction:', data.prediction);
        dataToSend = [];
        predictions.textContent = String(data.prediction);
        console.log(typeof(data.prediction))
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function smoothScroll(target) {
    const destination = document.querySelector(target);
    const targetPosition = destination.getBoundingClientRect().top + window.pageYOffset;
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    const duration = 1000; // Adjust duration as needed
  
    let start = null;
    function animation(currentTime) {
      if (start === null) start = currentTime;
      const timeElapsed = currentTime - start;
      const run = ease(timeElapsed, startPosition, distance, duration);
      window.scrollTo(0, run);
      if (timeElapsed < duration) requestAnimationFrame(animation);
    }
  
    function ease(t, b, c, d) {
      // Easing function (here using easeInOutQuad)
      t /= d / 2;
      if (t < 1) return (c / 2) * t * t + b;
      t--;
      return (-c / 2) * (t * (t - 2) - 1) + b;
    }
  
    requestAnimationFrame(animation);
  }
s  