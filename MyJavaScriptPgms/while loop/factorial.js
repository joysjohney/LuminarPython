
var num=Number(prompt("enter number"))
var fact=1;
var i=1;
while (i<=num){
    fact*=i;
    i++;
}
alert("Factorial of "+num+"="+fact)