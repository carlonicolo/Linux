python hello.py | tee log.txt
#ssh <username>@<IP>
echo "Type your username, followed by [ENTER]:"
read username

echo ""

echo "IP, followed by [ENTER]:"
read ip

echo ""

#echo "This is your username"
#echo $username

#echo "This is your IP"
#echo $ip

scp log.txt $username@$ip:~/
echo "Done !!!"
