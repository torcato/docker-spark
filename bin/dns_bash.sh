dns="dns.$1"
dns_dir="/tmp/dns_$1"
dns_file="$dns_dir/hosts.txt"

mkdir $dns_dir
touch $dns_file
echo "Please add extra hosts in $dns_file"

cmd="docker run -ti \
	--hostname $dns \
	--name  $dns \
	--volume=$dns_dir:/dns \
	-e CLUSTER=$1 \
	rawlabs/dns /bin/bash"
echo $cmd
$cmd
