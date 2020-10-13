var words="hii hello hi"
var str=words.split(" ")
var data={}
for (item of str)
{
    if (item in data)
    {
    data[item]+=1
    }
    else
    {
    data[item]=1
    }
}
console.log(data)