if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/starboihacks369/Auto-filter.git /Auto-filter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Auto-filter
fi
cd /Auto-filter
pip3 install -U -r requirements.txt
echo "Starting bot ❄️❄️ "
python3 bot.py
