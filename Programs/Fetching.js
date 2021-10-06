function fetchData(url) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", url);

        xhr.onload = function() {
            try {
                if(this.status === 200 ){
                    resolve(this);
                } else{
                    reject(this);
                }
            } catch(e){
                reject(e);
            }
        };

        xhr.onerror = function() {
            reject(this);
        };

        xhr.send();
    });
}

// driver code
fetchData("https://reqbin.com/echo/get/json")
.then(data => {
    console.log(data);
})
.catch(err => console.log(err));
