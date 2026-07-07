async function sendRequest(type){

const question=document.getElementById("question").value;

const response=document.getElementById("response");

const loading=document.getElementById("loading");

if(question.trim()===""){

alert("Please enter a question.");

return;

}

loading.style.display="block";

response.innerHTML="";

try{

const res=await fetch("/generate",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

question:question,

type:type

})

});

const data=await res.json();

loading.style.display="none";

response.innerHTML=marked.parse(data.response);

}

catch(error){

loading.style.display="none";

response.innerHTML="<b>Error:</b> "+error;

}

}