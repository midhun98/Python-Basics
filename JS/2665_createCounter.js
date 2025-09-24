/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let result = init
    let increment = function(){
        return ++result
    }
    let reset = function(){
        result = init
        return result
    }
    let decrement = function(){
        return --result
    }
    return {increment, reset, decrement}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */