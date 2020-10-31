function double(x) {
    return x*2;
}
function doubleNumbers(arr) {
    return arr.map(double);
  }


console.log(doubleNumbers([1,2,3,4,5]))
  
// console.log(doubleNumbers([2, 5, 100])); // [4, 10, 200]

// function stringItUp(arr){
//     return arr.map(num => num.toString());
//   }

// console.log(stringItUp([2, 5, 100])); // ["2", "5", "100"]

// function capitalizeNames(arr){
//     return arr.map(name =>
//         name[0].toUpperCase() + name.slice(1).toLowerCase())
//   }
  
// console.log(capitalizeNames(["john", "JACOB", "jinGleHeimer", "schmidt"])); // ["John", "Jacob", "Jingleheimer", "Schmidt"]

// function namesOnly(arr){
//     return arr.map(getName);
// }

// const getName = function(obj) {
//     return obj.name;
// }

  
//   console.log(namesOnly([
//       {
//           name: "Angelina Jolie",
//           age: 80
//       },
//       {
//           name: "Eric Jones",
//           age: 2
//       },
//       {
//           name: "Paris Hilton",
//           age: 5
//       },
//       {
//           name: "Kayne West",
//           age: 16
//       },
//       {
//           name: "Bob Ziroll",
//           age: 100
//       }
//   ])); 
//   // ["Angelina Jolie", "Eric Jones", "Paris Hilton", "Kayne West", "Bob Ziroll"]

// function total(arr) {
//     return arr.reduce((total, num) => {
//         return total + num;   // Redid this with an arrow function
//     })
// };
 
//  console.log(total([6,7,8])); // 21

//  function stringConcat(arr) {
//     return arr.reduce(stringify);
//  };
 
//  function stringify (string, char) {
//      return string + char.toString();
//  }
//  console.log(stringConcat([1,2,3])); // "123"

// function fiveAndGreaterOnly(arr) {
//     return arr.filter((num) => num >= 5);
//   }
//   // test
//   console.log(fiveAndGreaterOnly([3, 6, 8, 2])); /// [6, 8]