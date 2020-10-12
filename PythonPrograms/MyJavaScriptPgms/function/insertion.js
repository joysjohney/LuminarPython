
var arr=[];
function insert(n){
   arr.push(n);
}

var limit=Number(prompt("How many numbers to push :"));
for(var i=1;i<=limit;i++){
  var num=Number(prompt("Enter number "+i));
  insert(num)
}
console.log("Array = "+arr)