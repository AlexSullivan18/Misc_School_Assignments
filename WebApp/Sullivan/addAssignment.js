let xhttp = new XMLHttpRequest(); 
      
xhttp.addEventListener("onchange",success); 
xhttp.addEventListener("error",error);  
xhttp.open("GET", "/exam/addAssignment", true); 
xhttp.send();

function success(){
    let element =(
      <h2>Assignment added Successfully</h2>
    );
    
    ReactDOM.render(
      element,
      document.getElementById('message')
    );
 
  
  }

function error(){
    let element =(
        <h2>User Does Not Exist </h2>
      );
    ReactDOM.render(
        element,
        document.getElementById('message')
      );

    console.log(xhttp.readyState);
    console.log(xhttp.status);
  }