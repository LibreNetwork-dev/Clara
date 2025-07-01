# clean up from preexisting
rm -rf bin

# Install lua (latest, update it when new stuff comes out)

mkdir bin
curl -L -R -O https://www.lua.org/ftp/lua-5.4.8.tar.gz
tar zxf lua-5.4.8.tar.gz
cd lua-5.4.8
make all test
cd src 
cp -r lua ../../bin/lua
cd ../..
# clean up
rm -rf lua-5.4.8
rm -rf lua-5.4.8.tar.gz

# YT-dlp
git clone https://github.com/yt-dlp/yt-dlp.git
cd yt-dlp
python3 -m pip install -r requirements.txt
python3 -m pip install pyinstaller
pyinstaller -F -n yt-dlp -p . -c -y yt_dlp/__main__.py
cp dist/yt-dlp ../bin/yt-dlp
cd .. 
rm -rf yt-dlp

# Train the ai (gen data + train)
cd AI
rm -rf data
mkdir data
cd generation
python gen.py
python conversion.py
python music.py
python math.py
python mcontrol.py
python timer.py
cd ..
python train.py
cd ..

# package that stuff together 
rm -rf dist
mkdir dist 
cp -r bin dist/bin
cp -r scripts dist/scripts 
cp -r AI/fine_tuned dist/fine_tuned
cp -r AI/exec.py dist/exec.py
mkdir -p dist/cache/music
