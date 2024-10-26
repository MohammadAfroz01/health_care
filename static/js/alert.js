function validateForm() {
    var department = document.getElementById("exampleFormControlSelect1").value;
    var doctor = document.getElementById("exampleFormControlSelect2").value;
    var date = document.getElementById("date").value;
    var time = document.getElementById("exampleFormControlSelect3").value;
    var name = document.getElementById("name").value;
    var phone = document.getElementById("phone").value;
    var message = document.getElementById("message").value;

    
    // Add validation for other fields if needed

    if (department === "" || doctor === "" || date === "" || time === "" || name === "" || phone === "" || message === "") {
        alert("Please fill in all fields.");
        return false;
    }
    return true;
}