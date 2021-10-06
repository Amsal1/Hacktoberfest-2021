echo "Enter a number"
read num
function prime
{
for((i=2; i<=num/2; i++))
do
  if [ $((num%i)) -eq 0 ]
  then
    echo "$num is not a Prime Number."
    exit
  fi
done
echo "$num is a Prime Number."
}
r=`prime $number`
echo "$r"
 
