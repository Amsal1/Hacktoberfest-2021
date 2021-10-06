function curryFunc(fn) {
    return function curry(...args) {
        if (fn.length <= args.length) {
            return fn.apply(this, args);
        } else {
            return function (...args2) {
                return curry.apply(this, args.concat(args2));
            };
        }
    };
}

// driver code
let sum = curryFunc(function (a, b, c, d) {
    return a + b + c + d;
});

sum(1)(2)(3)(4);                    // called like curried function
sum(1,2)(3,4);                      // called like partial application
