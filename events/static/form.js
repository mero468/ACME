function validateForm() {
  let x = document.getElementById("githubform").getElementsByTagName("username")
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }
}