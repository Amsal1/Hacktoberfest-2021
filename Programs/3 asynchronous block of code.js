function asyncFunc() {
    console.log('Started asyncFunc1');
    //Async1 code
    setTimeout(() => {
        console.log('Completed asyncFunc1');

        console.log('Started asyncFunc2');
        //Async2 code
        setTimeout(() => {
            console.log('Completed asyncFunc2');

            console.log('Started asyncFunc3');
            //Async3 function code
            setTimeout(() => {
                console.log('Completed asyncFunc3');
            }, 1000);
        }, 2000);
    }, 3000);
}

asyncFunc();
