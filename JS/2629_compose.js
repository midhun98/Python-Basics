/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {
  return function (x) {
    let result = x;
    for (i = functions.length - 1; i >= 0; i--) {
      result = functions[i](result);
    }
    return result;
  };
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */

const fn = compose([(x) => x + 1, (x) => 2 * x]);
console.log(fn(4));

/*

const double = x => 2 * x;

// Call the function with different inputs
console.log("Calling double(4):", double(4)); // Outputs: 8
console.log("Calling double(10):", double(10)); // Outputs: 20

let result = (x => 2 * x)(5);
console.log("Direct call with 5:", result); // Outputs: 10

let functions = [x => x + 1, x => 2 * x]; // Array from the compose example
let input = 4;
let output = functions[1](input); // Call x => 2 * x with input = 4
console.log("Calling functions[1](4) like in compose:", output); // Outputs: 8

*/