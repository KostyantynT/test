_now=$(date +"%m_%d_%Y")
_file="$_now.dat"
python contact/manage.py printmodels 2> "$_file"
