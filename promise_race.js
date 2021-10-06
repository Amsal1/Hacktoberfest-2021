function asyncFunc1() {
    return new Promise(resolve =>
        setTimeout(() => {
            resolve('Resolved async1');
        }, 2000)
    );
}

function asyncFunc2() {
    return new Promise(resolve =>
        setTimeout(() => {
            resolve('Resolved async2');
        }, 3000)
    );
}

function asyncFunc3() {
    return new Promise((resolve, reject) =>
        setTimeout(() => {
            reject('Rejected async3');
        }, 1000)
    );
}

// driver code
const asyncArr = [asyncFunc1, asyncFunc2, asyncFunc3];
const promiseArr = asyncArr.map(async => async());
Promise.race(promiseArr).then(console.log).catch(console.log);    // Rejected async3 (catch block)
