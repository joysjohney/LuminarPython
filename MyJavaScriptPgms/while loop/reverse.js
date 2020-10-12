var num=Number(prompt(("enter number :"));
var rev=0;
while(num!=0){
    rem=num%10;
    rev = (rev * 10) + rem;
    num=parseInt(num/10);
}
alert("Reverse : "+rev)