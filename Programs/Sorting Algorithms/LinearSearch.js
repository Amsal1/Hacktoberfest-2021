let linearSearch = (list,value)=>{
    for (let i = 0; i < list.length; i++) {
        if (list[i] === value) {
            return i;
        }
    }
    return -1;
}

var list =  [ 1, 2, 3, 4, 5, 6 ]
var value = 3;

linearSearch(list , value) // result should 2
