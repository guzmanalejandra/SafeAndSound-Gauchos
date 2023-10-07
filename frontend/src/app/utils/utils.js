export function postData(data){
  console.log(data);
    fetch('http://127.0.0.1:5000/computeImage', {
        method: "POST",
        body: JSON.stringify(data),
        headers: {"Content-type": "application/json; charset=UTF-8"}
      })
      .then(response => response.json()) 
      .then(json => console.log(json))
      .catch(err => console.log(err));

}

