var ary=[10,20,30,40,50]
ele=Number(prompt("Enter num for search"))
flg=0
for (item of ary)
{
    if(item==ele)
    {
        flg=1
        break
    }

}
if(flg>0)
{
    prompt("element found")
}
else
{
    prompt("not found")
}