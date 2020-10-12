var num=Number(prompt("Enter ur number"))
function fact(n)
{
    var f=1
    while(i<=n)
    {
        f*=i
        i++
    }
    return(f)
}
var data=fact(num)
console.log("fact="+data)