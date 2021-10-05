function PromiseAll(promiseArr) {
    return new Promise((resolve, reject) => {
        const dataArr = new Array(promiseArr.length);
        let resolution = 'pending';

        for (let index in promiseArr) {
            promiseArr[index].then(
                data => {
                    if (resolution === 'pending') {
                        dataArr[index] = {
                            value: data,
                            status: 'fulfilled',
                        };
                        if (!dataArr.includes(undefined)) {
                            resolution = 'fulfilled';

                            resolve(dataArr);
                        }
                    }
                },
                err => {
                    if (resolution === 'pending') {
                        resolution = 'rejected';
                        reject({
                            reason: err,
                            status: 'rejected',
                        });
                    }
                }
            );
        }
    });
}

// driver code
PromiseAll([
    new Promise(resolve => setTimeout(resolve, 1000)),
    new Promise((resolve, reject) => setTimeout(reject, 2000)),
]).then(console.log, console.log);
