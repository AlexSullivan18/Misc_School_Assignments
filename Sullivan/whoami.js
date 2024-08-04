let who = new XMLHttpRequest(); 
      
who.addEventListener("load",whoami); 
who.open("GET", "/exam/whoami", true); 
who.send();

function whoami(){
  let data = JSON.parse(who.response);
    let element =(
    <span>{data.user}</span>
  );
  
  ReactDOM.render(
    element,
    document.getElementById('whoami')
  );
}
