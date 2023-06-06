function Show_pup(){
    document.getElementById('pup').classList.add('open')
}
function Hide_pup(){
    document.getElementById('pup').classList.remove('open')
}

function calculateBMI() {
    // Get weight and height values from input fields
    let weight = document.getElementById("weight").value;
    let height = document.getElementById("height").value;
  
    // Convert height to meters
    height /= 100;
  
    // Calculate BMI
    let bmi = weight / (height * height);
  
    // Round BMI to two decimal places
    bmi = bmi.toFixed(2);
  
    // Display BMI result
    document.getElementById("result").innerHTML = "Your BMI is: " + bmi;
  }

