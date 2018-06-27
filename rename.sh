#copy files from library/ to photo/ and rename them
path_from=library/bingdian
path_from=library/lib3
path_to=photo

i=328
echo strat from i = $i
for entry in "$path_from"/* 
do
    if [ -f "$entry" ];then
	#echo "$entry"
	cp "$entry" ${path_to}/photo$i.jpg
	let i=i+1
    fi
done
let i=i-1
echo the last one is i = $i