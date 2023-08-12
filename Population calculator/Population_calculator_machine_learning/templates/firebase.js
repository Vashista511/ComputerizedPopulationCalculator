const firebase = require("https://www.gstatic.com/firebasejs/9.14.0/firebase-app.js");
const firebaseConfig = {
  apiKey: "AIzaSyBqbJxj3dubD-n8rIr8oSJrNgsYinWGQdk",
  authDomain: "softwareengineering-a35b6.firebaseapp.com",
  projectId: "softwareengineering-a35b6",
  storageBucket: "softwareengineering-a35b6.appspot.com",
  messagingSenderId: "449785318210",
  appId: "1:449785318210:web:f3b05bddcd80f97e6456db",
  measurementId: "G-YJSFGPZ7PZ",
  databaseURL : " "
};

// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig);
const auth = app.auth()


function signUp(){
  var email = document.getElementById("email");
  var password = document.getElementById("password");

  const promise = auth.createUserWithEmailAndPassword(email.value,password.value);
  //
  promise.catch(e=>alert(e.message));
  alert("SignUp Successfully");
}



function  signIn(){
  var email = document.getElementById("email");
  var password  = document.getElementById("password");
  const promise = auth.signInWithEmailAndPassword(email.value,password.value);
  if(promise){
    window.location.replace("./index.html")
  }  
}




function signOut(){
  auth.signOut();
  alert("SignOut Successfully from System");
}



firebase.auth().onAuthStateChanged((user)=>{
  if(user){
    var email = user.email;
    alert("Active user "+email);

  }else{
    alert("No Active user Found")
  }
})
