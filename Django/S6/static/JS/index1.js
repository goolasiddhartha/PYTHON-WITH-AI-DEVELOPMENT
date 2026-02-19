function Test_case1() {
  var username = document.getElementById("A").value;
  var p1 = document.getElementById("B").value;
  var obj1 = username.match(/[A-Z]{1}[a-z]*[_]{1}[0-9]{5}/g);
  var obj2 = p1.match(/[A-Z]{2}[_]{1}[0-9]{5}/g);
  if (username == "" || username == null) {
    window.alert("Username is required");
    document.getElementById("ABC").innerHTML = "***Username is Required****";
    return false;
  } else if (obj1 == "" || obj1 == null) {
    window.alert("Invalid user name");
    document.getElementById("ABC").innerHTML =
      username + ":Invalid username EX:User_1234";
    return false;
  }
  if (p1 == "" || p1 == null) {
    window.alert("password is required");
    document.getElementById("abc").innerHTML = "***Password is required***";
    return false;
  } else if (obj2 == "" || obj2 == null) {
    window.alert("Invalid Password");
    document.getElementById("abc").innerHTML =
      P1 + ":Invalid Password Ex:JA_12345";
    return false;
  }
}
